import os
import json

# Use absolute imports
from my_agent.my_graph.nodes import analyze_changes, summarize_breaking_changes
from my_agent.models.schemas import ExtractionState, ReleaseLinks, VersionInput
from my_agent.services.llm import create_llm_model
from my_agent.utils.text import json_to_markdown
from my_agent.utils.load_page import load_page_contents
from my_agent.config import (
    TRINO_RELEASE_URL,
    TRINO_VERSION_URL,
    VERSION_SUMMARY_PROMPT
)
from my_agent.utils.logging_config import logger

from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage


# Graph nodes
def validate_input(state: ExtractionState) -> ExtractionState:
    """Validate the initial input"""
    if not state["page_contents"] or "Error" in state["page_contents"]:
        state["release_links"].error = "Invalid or empty page_contents content"
    return state

# Build the graph with model injected into the process node
def create_extraction_graph(model: ChatOllama):
    workflow = StateGraph(ExtractionState)

    workflow.add_node("validate_input", validate_input)
    workflow.add_node("analyze_changes", analyze_changes)
    workflow.add_node("summarize_breaking_changes", lambda state: summarize_breaking_changes(state, model))

    workflow.set_entry_point("validate_input")
    workflow.add_edge("validate_input", "analyze_changes")
    workflow.add_edge("analyze_changes", "summarize_breaking_changes")
    workflow.add_edge("summarize_breaking_changes", END)

    return workflow.compile()

# Main function
def extract_release_details(page_contents: str, version_start: str, version_end: str, model: ChatOllama) -> ExtractionState:
    """Extract release note URLs for two specified Trino versions from page_contents."""
    try:
        # Validate inputs using Pydantic
        versions = VersionInput(version_start=str(version_start), version_end=str(version_end))
        
        # Initialize state
        initial_state: ExtractionState = {
            "page_contents": page_contents,
            "versions": versions,
            "release_links": ReleaseLinks(),
            "context": None
        }
        
        # Execute graph with dependencies injected
        graph = create_extraction_graph(model)
        result = graph.invoke(initial_state)
        
        return result
        
    except Exception as e:
        return {"error": f"Input validation error: {str(e)}"}

def check_breaking_changes(version_start: str, version_end: str):
    logger.debug(f"Starting analysis for versions {version_start} to {version_end}")
    
    # Initialize services
    model = create_llm_model()
    logger.debug("LLM model initialized")
    
    # Load content in markdown format
    large_prompt = load_page_contents(TRINO_RELEASE_URL)
    if not large_prompt:
        logger.error(f"Error loading page contents from {TRINO_RELEASE_URL}")
        return None
    
    logger.debug(f"Content loaded, size: {len(large_prompt)}")
    
    # Process breaking changes
    result = extract_release_details(large_prompt, version_start, version_end, model)
    if "breaking_changes" not in result or "summary" not in result:
        logger.error("No breaking changes or summary found")
        logger.debug(f"Result: {result}")
        return None

    logger.info(f"Analysis complete for versions {version_start} to {version_end}")
    markdown_output = json_to_markdown(json.dumps(result["breaking_changes"]))

    # Write outputs to files
    output_dir = "./output"
    summary_file = os.path.join(output_dir, "summary_breaking_changes.md")
    breaking_changes_file = os.path.join(output_dir, "breaking_changes.md")
    with open(summary_file, "w") as f:
        f.write(f"Summary:\n\n{result['summary']}\n")
        logger.info(f"Results written to {summary_file}")
    with open(breaking_changes_file, "w") as f:
        f.write(markdown_output)
        logger.info(f"Results written to {breaking_changes_file}")

    return result["summary"], markdown_output

def summarize_release_version(version: str, summary_prompt: str = None):
    """Summarize the version release notes."""
    logger.debug(f"Starting analysis for version {version}")
    
    # Initialize services
    model = create_llm_model()
    logger.debug("LLM model initialized")
    
    # Load content in markdown format
    full_version_url = f"{TRINO_VERSION_URL}-{version}.html"
    large_prompt = load_page_contents(full_version_url)
    if not large_prompt:
        logger.error(f"Error loading page contents from {full_version_url}")
        return None
    
    logger.debug(f"Content loaded, size: {len(large_prompt)}")
    
    # Use the provided summary prompt or the default one
    prompt = f'{summary_prompt or VERSION_SUMMARY_PROMPT}: {version}'
    message = HumanMessage(content=f"{prompt}\nContext: {large_prompt}")
    response = model.invoke([message])
    summary_response = response.content
    print(summary_response)

    # Write outputs to files
    output_dir = "./output"
    summary_file = os.path.join(output_dir, f"summary_release_{version}.md")
    with open(summary_file, "w") as f:
        f.write(f"Summary:\n\n{summary_response}\n")
        logger.info(f"Results written to {summary_file}")

    return summary_response

if __name__ == "__main__":
    try:
        version_start = os.environ["VERSION_START"]
        version_end = os.environ["VERSION_END"]
    except KeyError:
        print("Environment variable 'VERSION_START' or 'VERSION_END' is not defined!")
        os.exit(1)
    check_breaking_changes(version_start=version_start, version_end=version_end)
