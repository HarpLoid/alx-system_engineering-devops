#!/usr/bin/python3
"""
Queries the Reddit API recursively
and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], next="next"):
    """
    returns all hot articles for a given subreddit
    return None if invalid subreddit is given
    """
    headers = {'User-Agent': 'Harploid/10.2'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if next != "next":
        url = url + f"?next={next}"

    resp = requests.get(url, headers=headers).json()
    result = resp.get('data', {}).get('children', [])
    if not result:
        return hot_list
    for i in result:
        hot_list.append(i.get('data').get('title'))

    next = resp.get('data').get('next')
    if not next:
        return hot_list
    return (recurse(subreddit, hot_list, next))
