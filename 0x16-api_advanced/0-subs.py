#!/usr/bin/python3
"""Queries the Reddit API and
returns the number of total subscribers for a given subreddit"""
import requests
from requests.exceptions import HTTPError
import praw

app_id = "6YmHWBdlASK8HtHgAOwJ8A"
app_secret = "NPiEFJ5bqOKcPOI7DfvT-AMPzU6Pug"
reddit_username = "FitInspection9287"
reddit_pass = "ckent2535"


def number_of_subscribers(my_subreddit):
    """Return the number of subscribers"""
    reddit = praw.Reddit(
        client_id=app_id,
        client_secret=app_secret,
        user_agent=f'MerchApi by {reddit_username}')

    # Get top posts from a subreddit
    subreddit = reddit.subreddit(my_subreddit)
    if subreddit:
        sub_total = subreddit.subscribers
    else:
        sub_total = 0
    return sub_total
