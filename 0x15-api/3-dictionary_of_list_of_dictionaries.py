#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    file_name = "todo_all_employees.json"
    dic_todo = {}
    for user in users:
        todos = requests.get(url + '/{}/todos'.format(user['id'])).json()
        dic_todo[user['id']] = [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user['username']
            } for task in todos]
    with open(file_name, 'w') as f:
        json.dump(dic_todo, f)
