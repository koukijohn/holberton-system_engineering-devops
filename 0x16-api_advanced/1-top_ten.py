#!/usr/bin/python3
'''
    This module will queries the Reddit API and print the titles of the
    first 10 hot posts listed for a given subreddit.
'''
import json
import requests


api_url_base = 'https://api.reddit.com/r/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'UnknownKouki'}


def top_ten(subreddit):
    '''
        This function will get the first 10 hot posts listed for a subreddit.
    '''
    get_url_request = requests.get('{}{}/hot?limit=10'.format
                                   (api_url_base, subreddit), headers=headers)
    json_data = get_url_request.json().get('data').get('children')

    try:
        for x in json_data:
            title = x.get('data').get('title')
            print(title)
        '''
            x = 0
            while x < 10:
                 print(get_url_request['data']['children'][x]['data']['title'])
                 x += 1
        '''

    except Exception:
        print(None)
