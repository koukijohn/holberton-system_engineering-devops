#!/usr/bin/python3
"""
    This is a module that will export to JSON.
"""
from json import dump
from requests import get
from sys import argv


def export_to_json(employee_id):
    """
        This will export our data to JSON format and record all tasks owned
        by this employee.
        Args:
            employee_id: This is our employee_id.
    """

    users = get("https://jsonplaceholder.typicode.com/users/{}"
                .format(employee_id)).json()
    USERNAME = users["username"]
    to_do_list = get("https://jsonplaceholder.typicode.com/todos").json()

    user_tasks = {}
    user_tasks[str(employee_id)] = []

    with open("{}.json".format(employee_id), "w") as json_file:
        for x in to_do_list:
            if x["userId"] == employee_id:
                dictionary = {}
                dictionary["tasks"] = x["title"]
                dictionary["completed"] = x["completed"]
                dictionary["username"] = USERNAME
                user_tasks[str(employee_id)].append(dictionary)
        dump(user_tasks, json_file)


if __name__ == "__main__":
    export_to_json(int(argv[1]))
