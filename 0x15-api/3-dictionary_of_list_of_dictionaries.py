#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""

import json
import requests

def all_to_json():

    """fetch data"""
    USERS = []
    userss = requests.get("https://jsonplaceholder.cypress.io/users")
    for u in userss.json():
        USERS.append((u.get('id'), u.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("https://jsonplaceholder.cypress.io/todos")
    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))
    """converting file to csv"""
    data = dict()
    for u in USERS:
        t = []
        for task in TASK_STATUS_TITLE:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)
if __name__ == "__main__":
    all_to_json()
