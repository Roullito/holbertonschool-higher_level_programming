def generate_invitations(template, attendees):
    if not isinstance(template, str):
        return "template is not a string"

    if not isinstance(attendees, list):
        return "attendees is not a list"

    for attendee in attendees:
        if not isinstance(attendee, dict):
            return "attendees dont containe dictionaries"

    if not (template):
        return "template is empty"

    if not (attendees):
        return "attendees is empty"

    for idx, attendee in enumerate(attendees):
        copy_template = template
        value_name = attendee.get("name") or "N/A"
        copy_template = copy_template.replace("{name}", value_name)

        value_title = attendee.get("event_title") or "N/A"
        copy_template = copy_template.replace("{event_title}", value_title)

        value_date = attendee.get("event_date") or "N/A"
        copy_template = copy_template.replace("{event_date}", value_date)

        value_location = attendee.get("event_location") or "N/A"
        copy_template = copy_template.replace(
            "{event_location}", value_location)

        filename = f"output_{idx+1}.txt"
        with open(filename, "w") as f:
            f.write(copy_template)
