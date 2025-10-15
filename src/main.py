from .commands import (
    add_task,
    show_tasks,
)


def main():
    while True:
        print("--- MENYU ---")
        print("1. Vazifa qoshish")
        print("2. Vazifalarni korish")
        print("3. Vazifani yangilash")
        print("4. Vazifani ochirish")
        print("5. Tugallangan deb belgilash")
        print("6. Chiqish")
        
        tanlov = input("Tanlovni kiriting: ")
        if tanlov == "1":
            add_task()
        elif tanlov == "2":
            show_tasks()
        elif tanlov == "6":
            print(" Dasturdan chiqildi.")
            break
        else:
            print("Notogri tanlov, qayta urinib ko‘ring.\n")
