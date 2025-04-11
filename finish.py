name_user = input("Привіт, я твій бот помічник. Як до тебе звертатися? ")
print(f"Приємно чути, {name_user}")

tasks_user = []

def menu():
    print("Меню")
    print("1. Додати завдання")
    print("2. Видалити завдання")
    print("3. Відкрити список завдань")
    print("4. Вийти з програми")

def function():
    while True:
        menu()
        choice = input("Виберіть пункт меню: ")

        if choice == "1":
            task = input("Надрукуйте своє завдання: ")
            tasks_user.append(task)
            print("Завдання додано до вашого списку!")
        elif choice == "2":
            if not tasks_user:
                print("Список порожній")
            else:
                remove_task = input("Будь ласка, скопіюйте завдання яке ви хочете видалити та вставте сюди: ")
                tasks_user.remove(f"{remove_task}")
                print("Ваше завдання було видалено!")
        elif choice == "3":
            if not tasks_user:
                print("Список порожній")
            else:
                print("Ось ваш список завдань")
                print(tasks_user)
        elif choice == "4":
            print("До зустрічі!")
            break
        else:
            print("Будь ласка, уведіть номер 1, 2 або 3!")

function()