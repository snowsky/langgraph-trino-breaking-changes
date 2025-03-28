import json

# Function to convert JSON to Markdown
def json_to_markdown(json_data: str):
    markdown = ""
    
    for entry in json.loads(json_data):
        # Create header with version and link
        markdown += f"## Version {entry['version']}\n\n"
        markdown += f"[Release Notes]({entry['link']})\n\n"
        
        # Add contents as list items
        markdown += "### Breaking Changes\n\n"
        for content in entry['contents']:
            # Replace newlines with spaces for cleaner output
            cleaned_content = content.replace('\n', ' ')
            markdown += f"- {cleaned_content}\n"
        
        markdown += "\n"  # Add spacing between versions
    
    return markdown