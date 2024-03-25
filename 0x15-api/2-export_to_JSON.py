#!/usr/bin/python3
"""Fetches data from an api and transforms it"""
import json
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

        users_response.raise_for_status()
        todos_response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
    else:
        username = users.get("username")
        file_path = "USER_ID.csv"
        with open("{}.json".format(id), "w") as file:
            json.dump({id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todos]}, file)
