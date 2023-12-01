import itertools
import datetime

# Mock function to simulate creating a meeting link
def create_meeting_link():
    return "https://example-meeting-link.com"

# Function to find common time slots
def find_common_times(slots):
    common_times = set(slots[0])
    for slot in slots[1:]:
        common_times.intersection_update(slot)
    return list(common_times)

# Function to handle the meeting scheduling
def schedule_meeting(attendees):
    availability = {}
    for attendee in attendees:
        print(f"Enter available times for {attendee} in HH:MM format (e.g., 09:00-10:00, 11:00-12:00):")
        times = input().split(", ")
        availability[attendee] = [tuple(map(str.strip, time.split("-"))) for time in times]

    common_slots = find_common_times(list(availability.values()))
    if common_slots:
        print("Common available times:", common_slots)
        print("Choose a time for the meeting (e.g., 09:00-10:00):")
        chosen_time = input()
        meeting_link = create_meeting_link()
        print(f"Meeting scheduled for {chosen_time}. Meeting link: {meeting_link}")
    else:
        print("No common time slots available.")

# Example usage
attendees = ["Alice", "Bob", "Charlie"]
schedule_meeting(attendees)
