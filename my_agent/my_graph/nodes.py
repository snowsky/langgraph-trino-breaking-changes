import requests
from bs4 import BeautifulSoup
from langchain_core.messages import HumanMessage
from models.schemas import ExtractionState
from my_agent.utils.logging_config import logger

def validate_input(state: ExtractionState) -> ExtractionState:
    """Validate the initial input"""
    if not state["page_contents"] or "Error" in state["page_contents"]:
        state["release_links"].error = "Invalid or empty page_contents content"
    return state

def summarize(state: ExtractionState, model) -> ExtractionState:
    """Summarize the changes"""
    prompt = f'Summarize the changes from version {state["versions"].version_start} to {state["versions"].version_end}'
    message = HumanMessage(content=f"{prompt}\nContext: {state['breaking_changes']}")
    response = model.invoke([message])
    state["summary"] = response.content
    return state

def analyze_changes(state: ExtractionState) -> ExtractionState:
    """Analyze breaking changes between releases"""
    if not state["release_links"]:
        return {
            "messages": [{"role": "assistant", "content": "Error: No release links to analyze"}]
        }

    breaking_changes = []
    start = int(state["versions"].version_start)
    end = int(state["versions"].version_end)

    for version in range(start, end + 1):
        url = f"https://trino.io/docs/current/release/release-{version}.html"
        try:
            content = requests.get(url).text
            soup = BeautifulSoup(content, 'html.parser')
            changes = [li.text for li in soup.find_all('li') if '⚠️' in li.text]
            if changes:
                breaking_changes.append({
                    "version": str(version),
                    "link": url,
                    "contents": changes
                })
        except Exception as e:
            logger.error(f"Failed to fetch or parse URL {url}: {e}")
            continue

    state["breaking_changes"] = breaking_changes 
    return state
