#!/usr/bin/python3
""" prints the titles of the first 10 hot posts """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts """
    headers = {"User-Agent": "Yissus"}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    info = requests.get(url, headers=headers)
    if info:
        data = info.json().get("data").get("children")
        for value in range(10):
            print(data[value].get("data").get("title"))
    else:
        print(None)
