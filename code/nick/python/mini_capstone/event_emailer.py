from trycourier import Courier
import datetime
from secrets import COURIER_TOKEN
SCHEDULED_TASKS = []  # set global variable for scheduled tasks


def schedule_extractor(children):
    '''
    search through all children of all pages and all children of all children for scheduled tasks marked 'SCHEDULED',
    and add them to a scheduled task list
    '''
    for child in children:
        if "content" in child.keys():  # some children do not contain content
            if "SCHEDULED" in child["content"]:  # check for keyword
                # ignore events that have already been completed
                if "DONE" not in child["content"]:
                    # add the even to the scheduled tasks
                    SCHEDULED_TASKS.append(child["content"])
        if "children" in child.keys():
            if len(child["children"]):  # if a child has children
                # reassign new children for recursion
                children = child["children"]
                # use recursion to access children of initial children
                schedule_extractor(children)


def main(SCHEDULED_TASKS):
    '''
    format the scheduled tasks, ensure they have not already been amailed to me, 
    email them to me if not already, and add them to the event history
    '''
    client = Courier(
        auth_token=COURIER_TOKEN)  # retrieve my personal token and instantiate Courier
    relative_path = 'code/nick/python/notes/scheduled_events_log.txt'  # path to event log
    with open(relative_path, 'r', encoding='utf-8') as file:
        PAST_EVENTS = file.read()  # open the event log
    # separate events into a list with the event and the time
    SCHEDULED_TASKS = [item.split("\nSCHEDULED:") for item in SCHEDULED_TASKS]
    FINAL_TASK_LIST = []
    for item in SCHEDULED_TASKS:
        # remove the metadata from the scheduled time
        item[1] = item[1].split("\n:LOGBOOK")[0]
        # convert the date from <yyyy-mm-dd day time> into ['yyyy', 'mm', 'dd']
        date_list = ((item[1].split("<")[1]).split(" ")[0]).split('-')
        year = int(date_list[0])  # access year as int
        month = int(date_list[1])  # access month as int
        day = int(date_list[2])  # access day as int
        # only work with events scheduled for today and later
        if datetime.date(year, month, day) >= datetime.date.today():
            # isolate events that have not already passed
            FINAL_TASK_LIST.append(item)

    TASKS_TO_EMAIL = []
    for task in FINAL_TASK_LIST:
        # check each event to see if it has already been sent to me for scheduling
        if ''.join(task) not in PAST_EVENTS:
            TASKS_TO_EMAIL.append(task)  # if it has not, isolate it for email

    PAST_EVENTS_LIST = [PAST_EVENTS]  # prep the events log for saving
    for event in TASKS_TO_EMAIL:  # send each event separately
        client.send_message(
            message={
                "to": {
                    "email": "nmurdaugh42@gmail.com"
                },
                "content": {
                    "title": "Scheduled task",
                    "body": '\n'.join(event)
                },
                "data": {
                    "data": "data"
                }
            }
        )
        # add each event to the event history log as it is sent
        PAST_EVENTS_LIST.append(''.join(event))

    PAST_EVENTS = '\n'.join(PAST_EVENTS_LIST)  # format events for logging
    with open(relative_path, 'w') as f:  # save event log to the same path from which it was pulled
        f.write(PAST_EVENTS)
