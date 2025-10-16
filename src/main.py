from .commands import add_task, show_tasks, update_task, delete_task, mark_completed


def main():
    while True:
        print("------ MENU ------")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Completed")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_completed()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("Invalid option. Try again.\n")
