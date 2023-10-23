#!/usr/bin/python3
"""
Request from API; Return TODO list progress of all employees
Export this data to JSON
"""
import json
import requests


def export_all():
    """
    returns API data
    """
    USERS = []
    TASK_TITLE = []

    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    for user in users.json():
        USERS.append((user.get('id'), user.get('username')))

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for todo in todos.json():
        TASK_TITLE.append((todo.get('userId'),
                           todo.get('title'),
                           todo.get('completed')))

    data = {}
    for user in USERS:
        task = []
        for tsk in TASK_TITLE:
            task.append({"username": user[1],
                         "task": tsk[1],
                        "completed": tsk[2]})
        data[str(user[0])] = task

    file_name = "todo_all_employees.json"

    with open(file_name, "w") as file:
        json.dump(data, file,
                  indent=2)


if __name__ == "__main__":
    export_all()
