#!/usr/bin/python3
"""Queries the Reddit API and
returns the number of total subscribers for a given subreddit"""
import requests
from requests.exceptions import HTTPError


client_id = "6YmHWBdlASK8HtHgAOwJ8A"
client_secret = "NPiEFJ5bqOKcPOI7DfvT-AMPzU6Pug"
user_agent = "MerchApi by FitInspection9287"
username = "FitInspection9287"
password = "ckent2535"

headers = {'User-Agent': 'MyApi/1'}


def get_access_token(client_id, client_secret):
    """Retrieve auth token"""
    data = {
        'grant_type': 'client_credentials',
        'username': username,
        'passowrd': password
    }
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    url = 'https://www.reddit.com/api/v1/access_token'
    response = requests.post(url, auth=auth, data=data, headers=headers)
    token = response.json()['access_token']
    return token


headers['Authorization'] = "bearer {}".format(
   get_access_token(
    client_id=client_id, client_secret=client_secret))


def number_of_subscribers(subreddit):
    """Return subscriber count"""
    try:
        response = requests.get(
            f'https://oauth.reddit.com/r/{subreddit}/about', headers=headers,
            allow_redirects=False)
        response.raise_for_status()
    except HTTPError as http_err:
        return 0
    except Exception as err:
        return 0
    else:
        total_sub = response.json().get('data')['subscribers']
        return total_sub
