#!/usr/bin/python3
"""
document define this project of count number of subscriber
"""

import requests


import sys


"""
Write a function that queries the Reddit API and returns
the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns
the number of subscribers"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (requests.json().get('data').get('subscribers'))
    return 0
