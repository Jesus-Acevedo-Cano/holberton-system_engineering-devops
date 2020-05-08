#!/usr/bin/python3
""" number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ number of subscribers """
    headers = {"User-Agent": "Yissus"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    info = requests.get(url, headers=headers)
    if info:
        return(info.json().get("data").get("subscribers"))
    return 0
