#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to CSV
"""
import csv
import requests
from sys import argv


def csv_export():
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

    file_name = "{}.csv".format(user_json.get('id'))
    with open(file_name, "w") as file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(file, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPETED_STATUS": task[1],
                             "TASK_TITLE": task[0]})


if __name__ == "__main__":
    csv_export()
