from traceback import print_tb

print("Привіт, я твій бот-помічник. Я потрібний для того щоб допомагати тобі з функціоналом програми мого розробника😙\nЯк мені до тебе звертатися?")
name_user = input()
print(f"Приємно чути {name_user}. Отож, тепер ми можемо приступити до створення твого першого рецепту😝")

list_recepts = []

def first_creation_list():
    print("Тут все дуже просто, просто надрукуй свій рецепт, але не забудь його підписати!(наприклад: салат, огірки,зелень,капуста")
    first_recept = input()
    list_recepts.append(first_recept)
    print("Чудово, в тебе є твій перший рецепт😋\nТепер ти можеш повноцінно користуватися всіма функціями цієї програми😃")

def main():
    while True:
        print("Вибери дію!\n1.Створити список з рецептом\n2.Переглянути списки з рецептами\n3.Змінити список(додати, видалити, тощо)\n4.Вийти з програми\n(напиши число відповідне до дії нижче)")
        try:
            choice_user = int(input())
        except ValueError:
            print("Ти не правильно увів число, спробуй ще раз!\n(спробуй увести число без крапок, дужок та тощо)")
            continue
        if choice_user == 1:
            print("Окей, просто напиши рецепт та незабудь його підписати!(друкувати нижче)")
            name_recept = input()
            list_recepts.append(name_recept)
            print("Рецепт створено!")
        if choice_user == 2:
            list_without = f"Ось список твоїх рецептів😋: {', '.join(list_recepts)}"
            print(list_without)
        if choice_user == 3:
            while True:
                print("Добре, обери список з рецептами, з яким ти хочеш взаємодіяти!(просто уведи назву списку):")
                list_without_second = f"Ось список твоїх рецептів😋: {', '.join(list_recepts)}"
                print(list_without_second)
                choice_list_with_recept = input()
                if choice_list_with_recept in list_recepts:
                    print("Тепер обери дію, яку ти хочеш виконати з ним\n1.Додати до списку\n2.Видалити елемент в списку\n3.Вийти")
                    try:
                        choice_user_in_section_third = int(input())
                    except ValueError:
                        print("Ти не правильно увів варіант відповіді, спробуй ще раз!\n(потрібно надрукувати 1, 2 або 3)")
                        continue
                    if choice_user_in_section_third == 1:
                        print("Добре, ти можеш додати новий елемент до свого рецепту(надрукувати нижче)")
                        add_to_recept = input()
                        list_recepts.append(add_to_recept)
                        print("Додано!")
                        break
                    elif choice_user_in_section_third == 2:
                        print("Добре, надрукуй елемент, який ти хочеш видалити(друкувати нижче)")
                        remove_element_in_list = input()
                        if remove_element_in_list in list_recepts:
                            list_recepts.remove(remove_element_in_list)
                            print("Елемент видалено!")
                        else:
                            print("Ти не правильно увів назву елементу, спробуй ще раз!\n(перевір чи все правильно або просто скопіюй потрібний тобі елемент")
                    elif choice_user_in_section_third == 3:
                        print("Вихід...")
                        break
                else:
                    print("Ти не правильно увів назву списку, спробуй ще раз!\n(перевір чи правильно ти надрукував всі літери або просто скопіюй назву потрібного списку")
        if choice_user == 4:
            print("До зустрічі!😊")
            break

first_creation_list()
main()
#В коді є багато недоліків, частину побачите ви а частиною я хотів бі поділитися
#Перше це досить важкий функціонал програми але я не витрачивав багато зусиль на його поліпшення через те що сам проєкт є MVP
#Друге це нелогічне продовження коду в деяких його частинках, наприклад коли вибриаєш "Змінити список" а потім вибираєш дію з ним та в разі некоректного вводу користувачем
#дії з списком рецепту цикл повторюється з моменту коли користувач тільки вибирає список який він хоче відрегувати хоча краще було б якщо починалось з моменту вибору дії зі списком
#Третє це граматичні помилки, їх може бути досить багато але що зробиш коли маєш з української мови 7 балів😥

#Я гадаю що для проєкта MVP це досить непогано та я хочу його вдосконалювати в ході вивчення нових модулей по курсу:)