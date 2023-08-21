#!/usr/bin/python3
"""Script to export data in the CVS format"""
import requests
import sys
import csv


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

    # Extract employee information
    user_id = user_data.get("id")
    username = user_data.get("username")

    # Create a CSV file with the specified filename
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header row to the CSV file
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task as a CSV record
        for task in todos_data:
            task_id = task.get("id")
            task_title = task.get("title")
            task_completed = task.get("completed")

            # Write the task data as a row in the CSV file
            csv_writer.writerow(
                [user_id, username, task_completed, task_title])

    print(f"CSV file '{csv_filename}' has been created.")


if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python 1-export_to_CSV.py employee_id")
        sys.exit(1)

    # Parse the employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Fetch and export the TODO list data in CSV format
    fetch_employee_todo_list(employee_id)
