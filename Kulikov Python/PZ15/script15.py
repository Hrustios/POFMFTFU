# Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для
# автоматизированного контроля затрат на производство продукции.
# БД содержит таблицу Расходы со следующей структурой записи:
# Дата, Код продукта, Наименование продукта, Расходы, Сумма.

import sqlite3

con = sqlite3.connect("expences.db")
curs = con.cursor()

def create_table():
    try:
        curs.execute('''CREATE TABLE IF NOT EXISTS "Расходы"(
                        data TEXT,
                        product_id INTEGER,
                        product_name TEXT,
                        expences INTEGER,
                        summ INTEGER
                        );''')
        con.commit()
        print("Таблица успешно создана или уже существует.")
    except sqlite3.Error as e:
        print(f"Ошибка создания таблицы: {e}")

def insert_data():
    try:
        data = input("Введите дату: ")
        product_id = int(input("Введите код продукта: "))
        product_name = input("Введите название продукта: ")
        expences = int(input("Введите расходы: "))
        summ = int(input("Введите сумму: "))
        curs.execute(f'INSERT INTO "Расходы" VALUES ("{data}",{product_id},"{product_name}",{expences},{summ});')
        con.commit()
        print("Запись успешно добавлена.")
    except Exception as e:
        print(f"Ошибка при добавлении записи: {e}")

def select_data():
    try:
        for row in curs.execute('SELECT * FROM "Расходы";'):
            print(" , ".join(map( str,row)))
    except sqlite3.Error as e:
        print(f"Ошибка выборки: {e}")

def search_data():
    print("1. По коду продукта")
    print("2. По наименованию продукта")
    print("3. По дате")
    choice = input("Выберите критерий поиска: ")
    match choice:
        case "1":
            pid = input("Введите код продукта: ")
            for row in curs.execute(f'SELECT * FROM "Расходы" WHERE product_id == "{pid}";'):
                print(" , ".join(map( str,row)))
        case "2":
            name = input("Введите название продукта: ")
            for row in curs.execute(f'SELECT * FROM "Расходы" WHERE product_name == "{name}";'):
                print(" , ".join(map( str,row)))
        case "3":
            date = input("Введите дату: ")
            for row in curs.execute(f'SELECT * FROM "Расходы" WHERE data == "{date}";'):
                print(" , ".join(map( str,row)))
        case _:
            print("Некорректный выбор.")
        
def delete_data():
    print("1. По коду продукта")
    print("2. По наименованию продукта")
    print("3. По дате")
    choice = input("Выберите критерий удаления: ")
    match choice:
        case "1":
            pid = input("Введите код продукта: ")
            curs.execute(f'DELETE FROM "Расходы" WHERE product_id == "{pid}";')
        case "2":
            name = input("Введите название продукта: ")
            curs.execute(f'DELETE FROM "Расходы" WHERE product_name == "{name}";')
        case "3":
            date = input("Введите дату: ")
            curs.execute(f'DELETE FROM "Расходы" WHERE data == "{date}";')
        case _:
            print("Некорректный выбор.")
            return
    con.commit()
    print("Записи успешно удалены.")

def update_data():
    print("1. Изменить расходы по коду продукта")
    print("2. Изменить название продукта по коду продукта")
    print("3. Изменить сумму по дате")
    choice = input("Выберите действие: ")
    if choice == "1":
        pid = input("Введите код продукта: ")
        new_exp = input("Введите новые расходы: ")
        curs.execute(f'UPDATE "Расходы" SET expences={new_exp} WHERE product_id== {pid};')
    elif choice == "2":
        pid = input("Введите код продукта: ")
        new_name = input("Введите новое название продукта: ")
        curs.execute(f'UPDATE "Расходы" SET product_name="{new_name}" WHERE product_id == {pid};')
    elif choice == "3":
        date = input("Введите дату: ")
        new_summ = input("Введите новую сумму: ")
        curs.execute(f'UPDATE "Расходы" SET summ={new_summ} WHERE data=="{date}";')
    else:
        print("Некорректный выбор.")
        return
    con.commit()
    print("Записи успешно обновлены.")

def main_menu():
    create_table()
    while True:
        print("\nВыберите действие:")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Поиск записей")
        print("4. Удаление записей")
        print("5. Редактирование записей")
        print("6. Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            insert_data()
        elif choice == "2":
            select_data()
        elif choice == "3":
            search_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            update_data()
        elif choice == "6":
            print("Завершение работы.")
            con.close()
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")
        


main_menu()
