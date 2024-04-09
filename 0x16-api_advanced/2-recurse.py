#!/usr/bin/python3
"""queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
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


def recurse(subreddit, count=0, after=None, hot_list=[]):
    """Use recursion to count hot posts"""
    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json'

    if after:
        url += f'?after={after}'

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False)
        response.raise_for_status()
    except HTTPError as http_err:
        return None
    except Exception as err:
        return None
    else:
        data = response.json()['data']
        hot_posts = data['children']
        count += len(hot_posts)

        hot_list.extend([post['data']['title'] for post in hot_posts])

        if data['after']:
            return recurse(
                subreddit, count, after=data['after'],
                hot_list=hot_list)

        return hot_list
