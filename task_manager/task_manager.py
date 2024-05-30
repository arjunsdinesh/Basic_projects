import json
import os

TASKS_FILE = 'tasks.json'

tasks = []


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            global tasks
            tasks = json.load(file)
    else:
        tasks = []


def save_tasks():
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)


def add_task():
    description = input("Enter task description: ")
    task = {'id': len(tasks) + 1, 'description': description, 'is_done': False}
    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if not tasks:
        print("No tasks to show.")
    for task in tasks:
        status = "Done" if task['is_done'] else "Not Done"
        print(
            f"ID: {task['id']}\nDescription: {task['description']}\nStatus: {status}\n"
        )


def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print("Task deleted successfully.")


def mark_task_as_done():
    task_id = int(input("Enter task ID to mark as done: "))
    for task in tasks:
        if task['id'] == task_id:
            task['is_done'] = True
            print("Task marked as done.")
            return
    print("Task not found.")


def show_menu():
    print("\nTo-Do Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("0. Exit")
    return int(input("Choose an option: "))


def main():
    load_tasks()  # Load tasks on start
    while True:
        choice = show_menu()
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_task_as_done()
        elif choice == 5:
            save_tasks()
        elif choice == 6:
            load_tasks()
        elif choice == 0:
            save_tasks()  # Save tasks on exit
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
