tasks = []

def add_task(task_list):
    task = input("Enter a new task: ")
    task_list.append(task)
    print(f"Added task: {task}")

def remove_task(task_list):
    task = input("Enter task to remove: ")
    if task in task_list:
        task_list.remove(task)
        print(f"Removed task: {task}")
    else:
        print(f"{task} not found")

def view_tasks(task_list):
    print("To-Do List:")
    for task in task_list:
        print(task)

while True:
    print("What do you want to do?")
    print("1. Add task")
    print("2. Remove task")
    print("3. View all tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        remove_task(tasks)
    elif choice == "3":
        view_tasks(tasks.copy())  # Make a copy before printing
    elif choice == "4":
        print(":)")
        break
    else:
        print("Invalid choice!")