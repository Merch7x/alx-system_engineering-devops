#!/usr/bin/python3
"""Fetches data from an api and transforms it"""
import requests
from requests.exceptions import HTTPError
import sys

if __name__ == "__main__":
    id = sys.argv[1]

    try:
        users_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{id}/')
        todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{id}/todos')

        users = users_response.json()
        todos = todos_response.json()

        completed_tasks = [
            t.get("title") for t in todos if t.get("completed") is True]

        users_response.raise_for_status()
        todos_response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
    else:
        print("Employee {} is done with tasks({}/{}):".format(
            users.get("name"), len(completed_tasks), len(todos)
        ))
        [print("\t {}".format(c)) for c in completed_tasks]
