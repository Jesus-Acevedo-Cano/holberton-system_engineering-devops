#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, argv[1])).json()
    todos = requests.get("{}/users/{}/todos".format(url, argv[1])).json()
    file_name = "{}.json".format(argv[1])
    dic_todo = {
        argv[1]:
        [
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user['username']
            } for task in todos
        ]
    }
    with open(file_name, 'w') as f:
        json.dump(dic_todo, f)
