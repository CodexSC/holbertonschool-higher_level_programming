import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ['name', 'event_title', 'event_date', 'event_location']

    for idx, attendee in enumerate(attendees, 1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace(f'{{{key}}}', str(value))
        filename = f"output_{idx}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
