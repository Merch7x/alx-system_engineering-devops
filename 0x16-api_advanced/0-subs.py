#!/usr/bin/python3
"""Queries the Reddit API and returns the number of total subscribers for a given subreddit"""
import requests
from requests.exceptions import HTTPError
import praw

app_id ="6YmHWBdlASK8HtHgAOwJ8A"
app_secret ="NPiEFJ5bqOKcPOI7DfvT-AMPzU6Pug"
reddit_username = "FitInspection9287"
reddit_pass = "ckent2535"

# def get_access_token(app_id, app_secret):
#     data = {
#         'grant_type': 'password',
#         'username': reddit_username,
#         'password': reddit_pass
#     }
#     headers={'user-agent': f'MerchApi by {reddit_username}'}
#     auth = requests.auth.HTTPBasicAuth(app_id, app_secret)
#     response = requests.post('https://www.reddit.com/api/v1/access_token', 
#                              data=data, 
#                              auth=auth)
#     return response.json().get('access_token')


# def number_of_subscribers(subreddit):
#   try:
#     url = f'https://https://oauth.reddit.com/api/r/{subreddit}/about'
#     token = 'bearer ' + get_access_token(app_id=app_id, app_secret=app_secret)
#     headers = {
#        'Authorization': token,
#        'User-Agent': f'MerchApi by {reddit_username}'
#     }
#     response = requests.get(url, headers=headers, allow_redirects=False).json()

#     response.raise_for_status()
#   except HTTPError as http_err:
#     print(f"Http error occured: {http_err}")
#     return 0
#   except Exception as err:
#     print(f"Error Ocurred: {err}")
#     return 0
#   else:
#         sub_total = response.get("subscriber_count")
#   return sub_total


# Authenticate with Reddit API
def number_of_subscribers(my_subreddit):
  reddit = praw.Reddit(client_id=app_id,
                      client_secret=app_secret,
                      user_agent=f'MerchApi by {reddit_username}')

  # Get top posts from a subreddit
  subreddit = reddit.subreddit(my_subreddit)
  if subreddit:
    sub_total = subreddit.subscribers
  else:
    sub_total = 0
  return sub_total
