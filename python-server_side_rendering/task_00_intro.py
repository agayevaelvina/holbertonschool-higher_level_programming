import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # For each attendee, generate invitation and write to file
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A"
        filled_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            replacement = str(value) if value else "N/A"
            filled_template = filled_template.replace(f"{{{key}}}", replacement)

        # Write to output_X.txt
        try:
            with open(f"output_{idx}.txt", "w") as outfile:
                outfile.write(filled_template)
        except Exception as e:
            print(f"Error writing file output_{idx}.txt: {e}")
