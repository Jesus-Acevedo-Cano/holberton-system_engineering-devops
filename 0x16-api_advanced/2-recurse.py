#!/usr/bin/python3
""" returns a list containing the titles of all hot articles """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns a list containing the titles of all hot articles """
    headers = {"User-Agent": "Yissus"}
    url = "http://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    info = requests.get(url, headers=headers)
    if info:
        info = info.json().get("data")
        after = info.get("after")
        info = info.get("children")
        for item in info:
            hot_list.append(item["data"].get("title"))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    else:
        return(None)
