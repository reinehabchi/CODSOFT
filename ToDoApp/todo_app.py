#Reinehabchi
#habchyreine@gmail.com
#https://www.linkedin.com/in/reine-habchi-716272234/
def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def update_task(task_number, new_task):
    tasks = []
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number")
        return

    tasks[task_number - 1] = new_task + "\n"

    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

def mark_task_as_done(task_number):
    tasks = []
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number")
        return

    tasks[task_number - 1] = "[DONE] " + tasks[task_number - 1]

    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

def list_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("No tasks found.")
        return

    print("List of Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")

while True:
    print("1. Add Task\n2. Update Task\n3. Mark Task as Done\n4. List Tasks\n5. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        task = input("Enter task description: ")
        add_task(task)
    elif choice == "2":
        task_number = int(input("Enter task number to update: "))
        new_task = input("Enter new task description: ")
        update_task(task_number, new_task)
    elif choice == "3":
        task_number = int(input("Enter task number to mark as done: "))
        mark_task_as_done(task_number)
    elif choice == "4":
        list_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
