from datetime import datetime
from rich.console import Console
from rich.table import Table
from .storage import create_task, get_tasks, save_tasks


def add_task():
    name = input("Task name: ").strip().capitalize()
    description = input("Description: ").strip().capitalize()
    category = input("Category: ").strip().title()
    due_date = input("Due date (YYYY-MM-DD): ").strip()

    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    if due_date < datetime.now():
        print("Date should be greater than or equal to now.")
        return

    create_task(name, description, category, due_date)
    print("✅ Task added successfully!\n")


def show_tasks():
    tasks = get_tasks()
    if len(tasks) == 0:
        print(" No tasks found.\n")
        return

    console = Console()
    table = Table(title="All Tasks")

    table.add_column("No.")
    table.add_column("Name")
    table.add_column("Category")
    table.add_column("Due Date")

    for i, task in enumerate(tasks, start=1):
        table.add_row(str(i), task["name"], task["category"], task["due_date"].strftime("%d/%m/%Y"))

    console.print(table)

    num = int(input("Task detail number (0 to exit): "))
    if num == 0:
        return

    task = tasks[num - 1]
    status = "✅ Completed" if task["status"] else "❌ Incomplete"

    print("\n--- Task Detail ---")
    print(f"Name: {task['name']}")
    print(f"Description: {task['description']}")
    print(f"Category: {task['category']}")
    print(f"Status: {status}")
    print(f"Due Date: {task['due_date'].strftime('%d/%m/%Y')}")
    print(f"Created: {task['created_date'].strftime('%d/%m/%Y, %H:%M:%S')}")
    print()


def update_task():
    tasks = get_tasks()
    if len(tasks) == 0:
        print("No tasks to update.\n")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']}")

    num = int(input("Select task number to update: "))
    task = tasks[num - 1]

    print("Press Enter to keep old value.")
    name = input(f"New name ({task['name']}): ").strip()
    description = input(f"New description ({task['description']}): ").strip()
    category = input(f"New category ({task['category']}): ").strip()
    due_date = input(f"New due date ({task['due_date'].strftime('%Y-%m-%d')}): ").strip()

    if name != "":
        task["name"] = name
    if description != "":
        task["description"] = description
    if category != "":
        task["category"] = category
    if due_date != "":
        task["due_date"] = datetime.strptime(due_date, "%Y-%m-%d")

    save_tasks(tasks)
    print("✅ Task updated successfully!\n")


def delete_task():
    tasks = get_tasks()
    if len(tasks) == 0:
        print("No tasks to delete.\n")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']}")

    num = int(input("ochirmoqchi bolgan tasni tanlang: "))
    task = tasks.pop(num - 1)

    save_tasks(tasks)
    print(f" Task '{task['name']}' deleted.\n")


def mark_completed():
    tasks = get_tasks()
    if len(tasks) == 0:
        print("task topilmadi.\n")
        return

    for i, task in enumerate(tasks, start=1):
        mark = "✅" if task["status"] else "❌"
        print(f"{i}. {task['name']} ({mark})")

    num = int(input("tugatilgan task nomerini tanlang: "))
    task = tasks[num - 1]
    task["status"] = True

    save_tasks(tasks)
    print(f" Task '{task['name']}' tugatilgan deb belgilandi\n")
