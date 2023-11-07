#!/usr/bin/python3
"""
Queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for subreddit
    return 0 if invalid subreddit is given
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Harploid/10.2'}

    resp = requests.get(url, headers=headers).json()
    subs = resp.get('data', {}).get('subscribers')
    if subs:
        return subs
    return 0
