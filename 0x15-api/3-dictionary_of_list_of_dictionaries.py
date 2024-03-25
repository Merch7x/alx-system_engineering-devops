#!/usr/bin/python3
"""Fetches data from an api and transforms it"""
import json
import requests
from requests.exceptions import HTTPError


if __name__ == "__main__":
    try:
        users_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/')
        base_url = "https://jsonplaceholder.typicode.com/"
        # todos_response = requests.get(
        #     f'https://jsonplaceholder.typicode.com/todos')

        users = users_response.json()
        # todos = todos_response.json()

        users_response.raise_for_status()
        # todos_response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
    else:
        with open("todo_all_employees.json", "w") as file:
            json.dump({user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(base_url + "todos",
                                       params={"userId": user.get("id")}).json()]
                for user in users}, file)
