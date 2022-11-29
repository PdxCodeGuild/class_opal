import requests
import json
# import telegram_send
from logseq_json_export_bot import logseq_json_export

logseq_json_export()
with open("C:/Users/Nick/Downloads/daily-logseq.json", 'r', encoding='utf-8') as file:
    contents = file.read()

pages = json.loads(contents)['blocks']


def doing_extractor(children, spaces=0):
    for child in children:
        if "content" in child.keys():
            if "DOING" in child["content"]:
                TODO_LIST.append(' '*spaces + child["content"])
        if "children" in child.keys():
            if len(child["children"]):
                children = child["children"]
                if "DOING" in child["content"]:
                    spaces += 4
                doing_extractor(children, spaces)


TODO_LIST = []
for page in pages:
    page_name = page["page-name"]
    children = page['children']
    if len(children):
        doing_extractor(children)


TODO_LIST = [item.split('\n')[0] for item in TODO_LIST]
TODO_LIST = [item.replace("DOING", '') for item in TODO_LIST]
todo_string = '\n'.join(TODO_LIST)
# print(todo_string)
# telegram_send.send(messages=[todo_string])

token = "5903167406:AAHSU8vJPaM98OwPyzIs-q-HRm_pJiRAC-k"
url = f"https://api.telegram.org/bot{token}"
params = {"chat_id": "5049168231", "text": todo_string}
requests.get(url + "/sendMessage", params=params)
