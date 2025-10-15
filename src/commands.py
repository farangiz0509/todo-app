from datetime import datetime
from rich.console import Console
from rich.table import Table
from .storage import create_task, get_tasks


def add_task():
    nom = input("Vazifa nomi: ").strip().capitalize()
    tarif = input("Ta’rif: ").strip().capitalize()
    turkum = input("Kategoriya: ").strip().title()
    muddat = input("Muddat (masalan: 2025-10-11): ")

    muddat = datetime.strptime(muddat, "%Y-%m-%d")
    if muddat < datetime.now():
        print("❗ Sana hozirgi kundan kichik bo‘lmasligi kerak.")
        return

    create_task(nom, tarif, turkum, muddat)
    print("✅ Vazifa muvaffaqiyatli qo‘shildi!")


def show_tasks():
    vazifalar = get_tasks()

    console = Console()

    jadval = Table(title="Barcha vazifalar")
    jadval.add_column("Raqam")
    jadval.add_column("Nomi")
    jadval.add_column("Kategoriya")
    jadval.add_column("Muddat")

    for raqam, vazifa in enumerate(vazifalar, start=1):
        muddat = vazifa["due_date"].strftime("%d/%m/%Y")
        jadval.add_row(str(raqam), vazifa["name"], vazifa["category"], muddat)
    
    console.print(jadval)

    raqam = int(input("Tafsilotlarni ko‘rish uchun vazifa raqamini kiriting: "))
    vazifa = vazifalar[raqam - 1]
    
    holat = "❌ Tugallanmagan"
    if vazifa["status"]:
        holat = "✅ Tugallangan"
    muddat = vazifa["due_date"].strftime("%d/%m/%Y")
    yaratilgan_sana = vazifa["created_date"].strftime("%d/%m/%Y, %H:%M:%S")

    print(f"Vazifa nomi: {vazifa['name']}")
    print(f"Tarif: {vazifa['description']}")
    print(f"Kategoriya: {vazifa['category']}")
    print(f"Holati: {holat}")
    print(f"Muddat: {muddat}")
    print(f"Yaratilgan sana: {yaratilgan_sana}")
    
    print()
