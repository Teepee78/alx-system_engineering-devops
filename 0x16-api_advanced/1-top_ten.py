#!/usr/bin/python3
"""
This module queries the reddit API for the titles of
hot posts in a particular subreddit
"""
import requests


def top_ten(subreddit):
    """
    Sends a query to reddit api for the number of subscribers
    """
    api_url = "https://api.reddit.com/r/{}/?sort=hot&limit=10".format(
        subreddit)
    headers = {
        "User-Agent": "CustomClient/1.0",
    }

    hot = requests.get(api_url, headers=headers, allow_redirects=False)
    if hot.status_code != 200:
        print(None)
    else:
        posts = hot.json().get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    print(None)
