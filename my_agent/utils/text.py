import json
from typing import Dict, List

def json_to_markdown(json_str: str) -> str:
    """Convert JSON string of breaking changes to markdown format."""
    try:
        data = json.loads(json_str)
        if not data:
            return "No breaking changes found. (json is empty)"

        markdown = "# Breaking Changes Summary\n\n"
        for change in data:
            markdown += f"## Version {change['version']}\n"
            markdown += f"[Release Notes]({change['link']})\n\n"
            if change.get('contents'):
                markdown += "Breaking changes:\n"
                for item in change['contents']:
                    markdown += f"* {item}\n"
            markdown += "\n"

        return markdown
    except json.JSONDecodeError:
        return "Error: Invalid JSON data"
    except Exception as e:
        return f"Error converting to markdown: {str(e)}"
