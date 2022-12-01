import json
from logseq_json_export_bot import logseq_json_export
import todo_notifier
import event_emailer

logseq_json_export()  # retrieve current Logseq data
with open("C:/Users/Nick/Downloads/daily-logseq.json", 'r', encoding='utf-8') as file:
    contents = file.read()
pages = json.loads(contents)['blocks']  # access logseq data pages


for page in pages:  # iterate through every page
    page_name = page["page-name"]
    children = page['children']  # access each pages children
    if len(children):
        # retrieve all priority todo items
        todo_notifier.doing_extractor(children)
        # retrieve all scheduled events
        event_emailer.schedule_extractor(children)

todo_notifier.main(todo_notifier.TODO_LIST)  # push todo list to my phone
# send each scheduled event to my email for scheduling in Google
event_emailer.main(event_emailer.SCHEDULED_TASKS)
