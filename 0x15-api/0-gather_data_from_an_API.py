#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, argv[1])).json()
    todos = requests.get("{}/users/{}/todos".format(url, argv[1])).json()
    tasks = [task.get('title') for task in todos if task.get('completed')]
    first_line = "Employee {} is done with tasks({}/{}):".format(
        user["name"], len(tasks), len(todos))
    print(first_line)
    [print("\t {}".format(task)) for task in tasks]
