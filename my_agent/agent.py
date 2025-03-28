import os
import json

# Use absolute imports
from my_agent.my_graph.nodes import analyze_changes, summarize
from my_agent.models.schemas import ExtractionState, ReleaseLinks, VersionInput
from my_agent.services.llm import create_llm_model
from my_agent.utils.text import json_to_markdown
from my_agent.utils.load_page import load_page_contents
from my_agent.config import (
    TRINO_RELEASE_URL,
)
from my_agent.utils.logging_config import logger

from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama


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
    workflow.add_node("summarize", lambda state: summarize(state, model))

    workflow.set_entry_point("validate_input")
    workflow.add_edge("validate_input", "analyze_changes")
    workflow.add_edge("analyze_changes", "summarize")
    workflow.add_edge("summarize", END)
    
    return workflow.compile()

# Main function
def extract_release_links(page_contents: str, version_start: str, version_end: str, model: ChatOllama) -> ExtractionState:
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

def main(version_start: str, version_end: str):
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
    result = extract_release_links(large_prompt, version_start, version_end, model)
    if "breaking_changes" not in result or "summary" not in result:
        logger.error("No breaking changes or summary found")
        logger.debug(f"Result: {result}")
        return None

    logger.info(f"Analysis complete for versions {version_start} to {version_end}")
    markdown_output = json_to_markdown(json.dumps(result["breaking_changes"]))

    # Write output to a file
    output_dir = "./output"
    output_file = os.path.join(output_dir, "result_output.txt")
    with open(output_file, "w") as f:
        f.write(f"Summary:\n{result['summary']}\n\nMarkdown Output:\n{markdown_output}")
    logger.info(f"Results written to {output_file}")

    return result["summary"], markdown_output

if __name__ == "__main__":
    try:
        version_start = os.environ["VERSION_START"]
        version_end = os.environ["VERSION_END"]
    except KeyError:
        print("Environment variable 'VERSION_START' or 'VERSION_END' is not defined!")
        os.exit(1)
    main(version_start=version_start, version_end=version_end)
