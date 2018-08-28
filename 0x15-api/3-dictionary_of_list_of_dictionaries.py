#!/usr/bin/python3
"""
    This is a module that will export to JSON.
"""
from json import dump
from requests import get
from sys import argv


def export_all_to_json():
    """
        This will export our data to JSON format and record all tasks owned
        by all of our employees.
        Args:
            employee_id: This is our employee_id.
    """

    all_users = get("https://jsonplaceholder.typicode.com/users/").json()
    to_do_list = get("https://jsonplaceholder.typicode.com/todos").json()

    user_tasks = {}

    with open("todo_all_employees.json", "w") as json_file:
        for user in all_users:
            user_tasks["{}".format(user["id"])] = []
            for x in to_do_list:
                if x["userId"] == user["id"]:
                    dictionary = {}
                    dictionary["username"] = user["username"]
                    dictionary["task"] = x["title"]
                    dictionary["completed"] = x["completed"]
                    user_tasks["{}".format(user["id"])].append(dictionary)
        dump(user_tasks, json_file)


if __name__ == "__main__":
    export_all_to_json()
