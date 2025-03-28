import requests
from typing import Optional
from my_agent.config import BACKEND_CRAWLSVC_URL

def load_page_contents(website_url: str) -> Optional[str]:
    """Fetch the HTML content of a given URL."""
    try:
        response = requests.get(BACKEND_CRAWLSVC_URL, params={"url": website_url})
        # print(response.json()["markdown"])
        return response.json()["markdown"]
    except Exception as e:
        print(f"Error loading website: {str(e)}")
        return None
