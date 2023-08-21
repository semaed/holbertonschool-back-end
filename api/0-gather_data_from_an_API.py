#!/usr/bin/python3
"""Script to return information of todo list"""
import requests
import sys


def fetch_employee_todo_list(employee_id):
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # URLs for fetching user data and TODO list for the given employee ID
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data and TODO list from the API
    response_user = requests.get(user_url)
    response_todos = requests.get(todos_url)

    # Extract JSON data from the responses
    user_data = response_user.json()
    todos_data = response_todos.json()

    # Extract employee name and calculate completed tasks
    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task["completed"]]

    # Display TODO list progress information
    print(
        f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py employee_id")
        sys.exit(1)

    # Parse the employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Fetch and display the TODO list progress for the specified employee ID
    fetch_employee_todo_list(employee_id)
