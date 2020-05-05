#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(url, argv[1])).json()
    todos = requests.get("{}/users/{}/todos".format(url, argv[1])).json()
    file_name = "{}.csv".format(argv[1])
    with open(file_name, "w") as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        list_todo = [
            [argv[1],
             user["username"],
             task.get("completed"),
             task.get("title")] for task in todos
        ]
        write.writerows(list_todo)
