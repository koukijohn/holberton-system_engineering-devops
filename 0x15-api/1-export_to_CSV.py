#!/usr/bin/python3
"""
    This module is based off of the previous module
    '0-gather_data_from_an_API.py', and will extend our Python script to
    export data in the CSV format.
"""
import csv
from requests import get
from sys import argv


def export_to_csv(employee_id):
    """
        This will export our data to CSV format.
        Args:
            employee_id: This is the employee id of our user we are grabbing
                         data from.
    """
    USER_ID = employee_id
    users = get("https://jsonplaceholder.typicode.com/users/{}"
                .format(employee_id)).json()
    USERNAME = users["username"]

    with open("{}.csv".format(USER_ID), "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        to_do_list = get("https://jsonplaceholder.typicode.com/todos").json()
        for TASK in to_do_list:
            if TASK["userId"] == employee_id:
                writer.writerow([USER_ID, USERNAME,
                                TASK["completed"], TASK["title"]])

if __name__ == "__main__":
    export_to_csv(int(argv[1]))
