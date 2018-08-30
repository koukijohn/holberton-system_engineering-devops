#!/usr/bin/python3
"""
    This module contains a recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles for a given
    subreddit.
"""
import json
import requests


base_api_url = "https://api.reddit.com/r/"
headers = {'Content-Type': 'application/json',
           'User-Agent': 'UnknownKouki'}


def recurse(subreddit, hot_list=[], after=""):
    """

    """
    get_url_request = requests.get('{}{}/hot?after={}'.format
                                   (base_api_url, subreddit, after),
                                   headers=headers)
    try:
        json = get_url_request.json()

        for x in json.get('data').get('children'):
            hot_list.append(x.get('data').get('title'))

        after = json.get('data').get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    except Exception as e:
        return (None)
