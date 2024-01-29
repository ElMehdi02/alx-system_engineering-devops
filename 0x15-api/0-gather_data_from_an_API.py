import requests
import sys

def get_employee_todo_list_progress(employee_id):
    # Fetch user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch todo data
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = len([task for task in todos_data if task['completed']])

    # Display the employee's progress
    print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')
    for task in todos_data:
        if task['completed']:
            print('\t ' + task['title'])

if __name__ == "__main__":
    get_employee_todo_list_progress(sys.argv[1])

