
import os
import json
from datetime import datetime, date

DATABASE_URL = "database.json"

if not os.path.exists(DATABASE_URL):
    with open(DATABASE_URL, "w") as f:
        f.write("[]")


def read_database() -> list[dict]:
    with open(DATABASE_URL) as f:
        data = json.load(f)
    return data


def save_database(tasks: list[dict]):
    with open(DATABASE_URL, "w") as f:
        json.dump(tasks, f, indent=4)


def create_task(name: str, description: str, category: str, due_date: date):
    tasks = read_database()

    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1

    new_task = {
        "id": new_id,
        "name": name,
        "description": description,
        "category": category,
        "due_date": due_date.strftime("%d/%m/%Y"),
        "created_date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "status": False
    }

    tasks.append(new_task)
    save_database(tasks)


def get_tasks():
    tasks = read_database()
    result = []
    for t in tasks:
        result.append({
            "id": t["id"],
            "name": t["name"],
            "description": t["description"],
            "category": t["category"],
            "due_date": datetime.strptime(t["due_date"], "%d/%m/%Y"),
            "created_date": datetime.strptime(t["created_date"], "%d/%m/%Y, %H:%M:%S"),
            "status": t["status"]
        })
    return result


def save_tasks(tasks: list[dict]):
    new_tasks = []
    for t in tasks:
        new_tasks.append({
            "id": t["id"],
            "name": t["name"],
            "description": t["description"],
            "category": t["category"],
            "due_date": t["due_date"].strftime("%d/%m/%Y"),
            "created_date": t["created_date"].strftime("%d/%m/%Y, %H:%M:%S"),
            "status": t["status"]
        })
    save_database(new_tasks)
