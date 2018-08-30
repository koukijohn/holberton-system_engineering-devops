#!/usr/bin/python3
'''
    This module queries the Reddit API and returns the total number of
    subscribers for a given subreddit.
'''
import json
import requests


api_url_base = 'https://api.reddit.com/r/'

headers = {'Content-Type': 'application/json',
           'User-Agent': 'UnknownKouki'}


def number_of_subscribers(subreddit):
    '''
        This will return the number of subscribers.
        Return: 0, if not valid.
    '''
    get_url_request = requests.get('{}{}/about'.format
                                   (api_url_base, subreddit), headers=headers)
    try:
        json_data = get_url_request.json().get('data')
        subscribers = json_data.get('subscribers')
        return subscribers
    except Exception as e:
        return 0
