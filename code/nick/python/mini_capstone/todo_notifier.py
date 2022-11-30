import requests
from secrets import TELEGRAM_TOKEN
TODO_LIST = []  # set global variable for todo list


def doing_extractor(children, spaces=0):
    '''
    search through all children of all pages and all children of all children for priority tasks marked 'DOING',
    and add them to a todo list
    '''
    for child in children:
        if "content" in child.keys():  # some children do not contain content
            if "DOING" in child["content"]:  # check for keyword
                # add task to todo list with appropriate spacing
                TODO_LIST.append(' '*spaces + child["content"])
        if "children" in child.keys():
            if len(child["children"]):  # if a child has children
                # reassign new children for recursion
                children = child["children"]
                if "DOING" in child["content"]:
                    spaces += 4  # add an indent for tasks that are children of other tasks
                # use recursion to access children of initial children
                doing_extractor(children, spaces)


def main(TODO_LIST):
    '''
    format the todo list, and send it to my telegram
    '''
    TODO_LIST = [item.split('\n')[0]
                 for item in TODO_LIST]  # remove metadata from task
    # remove 'DOING' tag and just leave the task
    TODO_LIST = [item.replace("DOING", '') for item in TODO_LIST]
    # turn todo list into a string, prep for push
    todo_string = '\n'.join(TODO_LIST)
    token = TELEGRAM_TOKEN  # access private token
    url = f"https://api.telegram.org/bot{token}"  # set request url
    # set parameters with my telegram user id and the text I want to receive (my todo list)
    params = {"chat_id": "5049168231", "text": todo_string}
    requests.get(url + "/sendMessage", params=params)  # make API call
