
import os
import json
from datetime import datetime, date

DATABASE_URL = "database.json"

if not os.path.exists(DATABASE_URL):
    with open(DATABASE_URL, "w") as f:
        f.write("[]")


def read_database() -> list[dict]:
    with open(DATABASE_URL) as f:
        tasks = json.load(f)
    return tasks


def save_database(tasks: list[dict]):
    with open(DATABASE_URL, "w") as f:
        json.dump(tasks, f, indent=4)


def create_task(nom: str, tarif: str, turkum: str, muddat: date) -> bool:
    vazifalar = read_database()

    oxirgi_vazifa = max(vazifalar, key=lambda v: v['id'], default={"id": 0})
    vazifalar.append({
        "id": oxirgi_vazifa["id"] + 1,
        "name": nom,
        "description": tarif,
        "category": turkum,
        "due_date": muddat.strftime("%d/%m/%Y"),
        "created_date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "status": False,
    })

    save_database(vazifalar)


def get_tasks():
    vazifalar = list(map(
        lambda v: {
            "id": v["id"],
            "name": v["name"],
            "description": v["description"],
            "category": v["category"],
            "due_date": datetime.strptime(v["due_date"], "%d/%m/%Y"),
            "created_date": datetime.strptime(v["created_date"], "%d/%m/%Y, %H:%M:%S"),
            "status": v["status"]
        },
        read_database(),
    ))

    return vazifalar
