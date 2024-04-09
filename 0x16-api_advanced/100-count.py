#!/usr/bin/python3
"""queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests
from requests.exceptions import HTTPError


# client_id = "6YmHWBdlASK8HtHgAOwJ8A"
# client_secret = "NPiEFJ5bqOKcPOI7DfvT-AMPzU6Pug"
# user_agent = "MerchApi by FitInspection9287"
# username = "FitInspection9287"
# password = "ckent2535"

# headers = {'User-Agent': 'MyApi/1'}


# def get_access_token(client_id, client_secret):
#     """Retrieve auth token"""
#     data = {
#         'grant_type': 'client_credentials',
#         'username': username,
#         'passowrd': password
#     }
#     auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
#     url = 'https://www.reddit.com/api/v1/access_token'
#     response = requests.post(url, auth=auth, data=data, headers=headers)
#     token = response.json()['access_token']
#     return token


# headers['Authorization'] = "bearer {}".format(
#    get_access_token(
#     client_id=client_id, client_secret=client_secret))


# def count_words(subreddit, after=None, word_list=None):
#     """Use recursion to count hot posts"""

#     if word_list is None:
#         word_list = []

#     url = f'https://oauth.reddit.com/r/{subreddit}/hot.json'

#     if after:
#         url += f'?after={after}'

#     try:
#         response = requests.get(
#             url,
#             headers=headers,
#             allow_redirects=False)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         return None
#     except Exception as err:
#         return None
#     else:
#         data = response.json()['data']
#         hot_posts = data['children']
#         count += len(hot_posts)

#         hot_list = ([post['data']['title'] for post in hot_posts])
#         count = 0

#         for title in hot_list:
#             title_lower = title.lower()
#             for word in word_list:
#                 if word.lower() in title_lower:
#                     count += 1

#         if data['after']:
#             return count  + count_words(
#                 subreddit, after=data['after'],
#                 word_list=word_list)

#         print (count)


def count_words(subreddit, word_list, found_list=[], after=None):
    """Prints counts of given words found in hot posts of a given subreddit."""
    user_agent = {'User-agent': 'test45'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
