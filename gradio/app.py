# Required for running the app locally
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gradio as gr
import my_agent.agent as agent

def check_trino_breaking_changes(version_start, version_end):
    # Input validation
    if not version_start or not version_end:
        raise gr.Error("Both version start and end are required")
    
    try:
        version_start = int(version_start)
        version_end = int(version_end)
    except ValueError:
        raise gr.Error("Versions must be integers")
    
    if version_start >= version_end:
        raise gr.Error("Start version must be less than end version")

    # Add your actual processing logic here.
    summary, breaking_changes = agent.main(version_start=version_start, version_end=version_end)
    print(breaking_changes)
    
    return summary, breaking_changes

iface = gr.Interface(
    fn=check_trino_breaking_changes,
    inputs=[
        gr.Textbox(label="Start Version", placeholder="Enter the starting version"),
        gr.Textbox(label="End Version", placeholder="Enter the ending version")
    ],
    outputs=[
        gr.Textbox(label="Summary", show_copy_button=True),
        gr.Textbox(label="Breaking Changes", show_copy_button=True)
    ],
    title="Trino Breaking Changes",
    description="An app to show breaking changes upgrading Trino from \"Start Version\" to \"End Version\"."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", share=True)
