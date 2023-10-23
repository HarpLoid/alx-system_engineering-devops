#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to CSV
"""
import json
import requests
from sys import argv


def json_export():
    """
    returns API data
    """
    USERNAME = ""
    TASK_TITLE = []

    users = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    user_json = users.json()
    USERNAME = user_json.get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TASK_TITLE.append((todo.get('title'), todo.get('completed')))

    task = []
    for tsk in TASK_TITLE:
        task.append({"task": tsk[0],
                     "completed": tsk[1],
                     "username": USERNAME})

    data = {str(argv[1]): task}
    file_name = "{}.json".format(user_json.get('id'))
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    json_export()
