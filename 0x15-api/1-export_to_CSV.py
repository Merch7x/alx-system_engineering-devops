#!/usr/bin/python3
"""Fetches data from an api and transforms it"""
import csv
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
        with open("{}.csv".format(id), "w", newline="") as csv_file:
            fieldnames = ["USER_ID", "USERNAME",
                          "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

            [writer.writerow(
                [id, username, task.get("completed"), task.get("title")]
            )for task in todos]
