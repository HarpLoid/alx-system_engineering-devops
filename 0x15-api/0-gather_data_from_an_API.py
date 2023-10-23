#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
Uses 'https://jsonplaceholder.typicode.com/todos/'
for a given employee ID to return the
information about his or her TODO list progress
"""
import requests
from sys import argv


def render():
    """
    Returns Emloyee Information and TODO list
    """
    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    users = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    user_json = users.json()
    EMPLOYEE_NAME = user_json.get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME,
                  NUMBER_OF_DONE_TASKS,
                  TOTAL_NUMBER_OF_TASKS))

    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    render()
