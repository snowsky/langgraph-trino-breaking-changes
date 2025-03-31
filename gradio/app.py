# Required for running the app locally
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gradio as gr
import my_agent.agent as agent

def check_trino_breaking_changes(version_start, version_end):
    # Input validation for breaking changes
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
    summary, breaking_changes = agent.check_breaking_changes(version_start=version_start, version_end=version_end)
    print(breaking_changes)
    
    return summary, breaking_changes

def summarize_release_version(version, summary_prompt):
    # Input validation
    if not version:
        raise gr.Error("Version is required")

    try:
        version = int(version)
    except ValueError:
        raise gr.Error("Version must be an integer")

    # Add your actual processing logic here.
    summary = agent.summarize_release_version(version=version, summary_prompt=summary_prompt)
    print(summary)

    return summary

def combined_interface(choice, version_start=None, version_end=None, version=None, summary_prompt=None):
    if choice == "Check Breaking Changes":
        # Call the breaking changes function
        summary, breaking_changes = check_trino_breaking_changes(version_start=version_start, version_end=version_end)
        return summary, breaking_changes

    elif choice == "Summarize Release Version":
        # Call the summarize function
        summary = summarize_release_version(version, summary_prompt)
        return summary, None

    else:
        raise gr.Error("Invalid choice")

def update_inputs(choice):
    if choice == "Check Breaking Changes":
        # Show "Start Version" and "End Version", hide "Version" and "Summary Prompt", and show "Breaking Changes"
        return (
            gr.update(visible=True),  # Start Version
            gr.update(visible=True),  # End Version
            gr.update(visible=False),  # Version
            gr.update(visible=False),  # Summary Prompt
            gr.update(visible=True),   # Breaking Changes
            gr.update(value=""),       # Clear Summary
            gr.update(value="")        # Clear Breaking Changes
        )
    elif choice == "Summarize Release Version":
        # Show "Version" and "Summary Prompt", hide "Start Version", "End Version", and "Breaking Changes"
        return (
            gr.update(visible=False),  # Start Version
            gr.update(visible=False),  # End Version
            gr.update(visible=True),   # Version
            gr.update(visible=True),   # Summary Prompt
            gr.update(visible=False),  # Breaking Changes
            gr.update(value=""),       # Clear Summary
            gr.update(value="")        # Clear Breaking Changes
        )
    else:
        # Hide all fields
        return (
            gr.update(visible=False),  # Start Version
            gr.update(visible=False),  # End Version
            gr.update(visible=False),  # Version
            gr.update(visible=False),  # Summary Prompt
            gr.update(visible=False),  # Breaking Changes
            gr.update(value=""),       # Clear Summary
            gr.update(value="")        # Clear Breaking Changes
        )

with gr.Blocks() as iface_combined:
    choice = gr.Dropdown(
        choices=["Check Breaking Changes", "Summarize Release Version"],
        label="Choose an Action",
        value="Check Breaking Changes"  # Default value
    )
    start_version = gr.Textbox(label="Start Version", placeholder="Enter the starting version", visible=True, interactive=True)
    end_version = gr.Textbox(label="End Version", placeholder="Enter the ending version", visible=True, interactive=True)
    version = gr.Textbox(label="Version", placeholder="Enter the version to summarize", visible=False, interactive=True)
    summary_prompt = gr.Textbox(label="Summary Prompt", placeholder="Enter a custom summary prompt", visible=False, interactive=True)
    summary_output = gr.Textbox(label="Summary", show_copy_button=True)
    breaking_changes_output = gr.Textbox(label="Breaking Changes", show_copy_button=True, visible=True)

    # Update inputs and outputs dynamically based on the dropdown choice
    choice.change(
        fn=update_inputs,
        inputs=[choice],
        outputs=[start_version, end_version, version, summary_prompt, breaking_changes_output, summary_output, breaking_changes_output]
    )

    # Submit button to call the combined_interface function
    submit_button = gr.Button("Submit")
    submit_button.click(
        fn=combined_interface,
        inputs=[choice, start_version, end_version, version, summary_prompt],
        outputs=[summary_output, breaking_changes_output]
    )

    # Enable "Enter" key to submit
    start_version.submit(
        fn=combined_interface,
        inputs=[choice, start_version, end_version, version, summary_prompt],
        outputs=[summary_output, breaking_changes_output]
    )
    end_version.submit(
        fn=combined_interface,
        inputs=[choice, start_version, end_version, version, summary_prompt],
        outputs=[summary_output, breaking_changes_output]
    )
    version.submit(
        fn=combined_interface,
        inputs=[choice, start_version, end_version, version, summary_prompt],
        outputs=[summary_output, breaking_changes_output]
    )
    summary_prompt.submit(
        fn=combined_interface,
        inputs=[choice, start_version, end_version, version, summary_prompt],
        outputs=[summary_output, breaking_changes_output]
    )

if __name__ == "__main__":
    iface_combined.launch(server_name="0.0.0.0", share=True)
