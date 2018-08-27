#!/usr/bin/python3
"""
    This is a python script that will grab information from this REST APT
    <https://jsonplaceholder.typicode.com/> and it will, for a given
    employee ID, returns information about his or her TODO list progress.
"""
from requests import get
from sys import argv


def to_do_list_progress(employee_id):
    """
        This is a python script gives us information about their todo list.
        Args:
            EMPLOYEE_NAME: name of the employee.
            NUMBER_OF_DONE_TASKS: number of completed tasks.
            TOTAL_NUMBER_OF_TASKS: sum of completed and non-completed tasks
    """
    users = get("https://jsonplaceholder.typicode.com/users/{}"
                .format(employee_id)).json()
    EMPLOYEE_NAME = users["name"]
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    to_do_list = get("https://jsonplaceholder.typicode.com/todos").json()
    TASK_TITLE = []

    for x in to_do_list:
        if x["userId"] == employee_id:
            TOTAL_NUMBER_OF_TASKS += 1
            if x["completed"]:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(x["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for title in TASK_TITLE:
        print("\t {}".format(title))

if __name__ == "__main__":
    to_do_list_progress(int(argv[1]))
