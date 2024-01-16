#!/usr/bin/python3
"""
Queries the Reddit API and prints
the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    returns top ten titles for a given subreddit
    return None if invalid subreddit is given
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'Harploid/10.2'}

    resp = requests.get(url, headers=headers).json()
    top_ten = resp.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for t in top_ten:
        print(t.get('data').get('title'))
