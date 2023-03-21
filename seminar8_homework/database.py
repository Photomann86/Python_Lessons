from os import path
# "/Users/ivanchevardin/Python_lessons/Python_Lessons/seminar8_homework"

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    """Чтение конкретной записи из книги"""

    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])

        return all_data


def show_all():
    """Функция показа всех записей книги"""

    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    #Добавление новой записи в книгу

    global last_id

    array = ['surname', 'name', 'patronymic', 'phone number']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Данные успешно добавлены в вашу телефонную книгу!\n")
    else:
        print("Эти данные уже есть!")


def del_contact():
    #удаление записи из телефонной книги

    global all_data

    symbol = "\n"
    show_all()
    del_record = input("введите id записи: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена!\n")
    else:
        print("Данные некорректны!")


def change_contact(data_tuple):
    
    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Такие данные уже в базе!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("запись изменена!\n")


def search_contact():
    search_data = exist_contact(0, input("Введите данные для поиска: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Данные некорректны!")


def exist_contact(rec_id, data):

    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):

    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Данные некорректны!\n"
                       f"Используйте только символы алфавита\n"
                       f"формат номера телефона - 11 цифр\n"
                       f"введите {num}: ")
    return answer


def main_menu():
    """основное меню"""

    play = True
    while play:
        read_records()
        answer = input("Телефонная книга:\n"
                       "1. показать все записи\n"
                       "2. создать запись\n"
                       "3. найти\n"
                       "4. заменить\n"
                       "5. удалить\n"
                       "6. экспорт/импорт\n"
                       "7. выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
                exp_imp_menu()
            case "7":
                play = False
            case _:
                print("Попробуйте снова!\n")


def edit_menu():
    """меню редактирования записей в БД"""

    add_dict = {"1": "surname", "2": "name", "3": "patronymic", "4": "phone number"}

    show_all()
    record_id = input("введите идентификатор записи: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. Фамилия\n"
                           "2. Имя\n"
                           "3. Отчество\n"
                           "4. номер телефона\n"
                           "5. выход\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("Данные неопознаны! Повторите попытку.")
    else:
        print("данные некорректны! Повторите ввод")


def exp_bd(name):
    """экспорт базы"""

    symbol = "\n"

    change_name = f"{name}.txt"
    if not path.exists(change_name):
        with open(change_name, "w", encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')


def ipm_bd(name):
    global file_base

    if path.exists(name):
        file_base = name
        read_records()


def exp_imp_menu():
    """экспорт/импорт'"""

    while True:
        print("\nМеню экспорта/импорта:")
        move = input("1. импортировать\n"
                     "2. экспортировать\n"
                     "3. выйти\n")

        match move:
            case "1":
                ipm_bd(input("введите имя файла: "))
            case "2":
                exp_bd(input("введите имя файла: "))
            case "3":
                return 0
            case _:
                print("неопознанный формат записи! Повторите ввод")


main_menu()
