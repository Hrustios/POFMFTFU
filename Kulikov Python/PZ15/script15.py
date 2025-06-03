# Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для
# автоматизированного контроля затрат на производство продукции.
# БД содержит таблицу Расходы со следующей структурой записи:
# Дата, Код продукта, Наименование продукта, Расходы, Сумма.

import sqlite3 , random , datetime

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

def auto_commands():
    import random

    print("\n=== Автоматическая демонстрация всех функций ===")

    # Автозаполнение таблицы
    print("\nАвтозаполнение 10 строк...")
    auto_fill_data()
    select_data()

    # Автопоиск (по разным критериям)
    print("\nАвтопоиск записей:")
    curs.execute('SELECT product_id, product_name, data FROM "Расходы" LIMIT 3;')
    rows = curs.fetchall()
    if rows:
        # Поиск по коду продукта
        print(f"\nПоиск по коду продукта {rows[0][0]}:")
        for row in curs.execute(f'SELECT * FROM "Расходы" WHERE product_id == {rows[0][0]};'):
            print(" , ".join(map(str, row)))

        # Поиск по названию продукта
        print(f"\nПоиск по названию продукта '{rows[1][1]}':")
        for row in curs.execute(f'SELECT * FROM "Расходы" WHERE product_name == "{rows[1][1]}";'):
            print(" , ".join(map(str, row)))

        # Поиск по дате
        print(f"\nПоиск по дате {rows[2][2]}:")
        for row in curs.execute(f'SELECT * FROM "Расходы" WHERE data == "{rows[2][2]}";'):
            print(" , ".join(map(str, row)))

    # Автоудаление (по разным критериям)
    print("\nАвтоудаление записей:")
    if rows:
        curs.execute(f'DELETE FROM "Расходы" WHERE product_id == {rows[0][0]};')
        curs.execute(f'DELETE FROM "Расходы" WHERE product_name == "{rows[1][1]}";')
        curs.execute(f'DELETE FROM "Расходы" WHERE data == "{rows[2][2]}";')
        con.commit()
        print("Удалены 3 записи по разным критериям.")

    select_data()

    # Автообновление (по разным критериям)
    print("\nАвтообновление записей:")
    curs.execute('SELECT product_id, data FROM "Расходы" LIMIT 3;')
    update_rows = curs.fetchall()
    if update_rows:
        # Изменить расходы по коду продукта
        new_exp = random.randint(200, 1500)
        curs.execute(f'UPDATE "Расходы" SET expences = {new_exp} WHERE product_id == {update_rows[0][0]};')
        print(f"Изменены расходы на {new_exp} по коду {update_rows[0][0]}.")

        # Изменить название продукта по коду продукта
        new_name = random.choice(["Кетчуп", "Йогурт", "Курица", "Сок"])
        curs.execute(f'UPDATE "Расходы" SET product_name = "{new_name}" WHERE product_id == {update_rows[1][0]};')
        print(f"Изменено название на {new_name} по коду {update_rows[1][0]}.")

        # Изменить сумму по дате
        new_summ = random.randint(5000, 20000)
        curs.execute(f'UPDATE "Расходы" SET summ = {new_summ} WHERE data == "{update_rows[2][1]}";')
        print(f"Изменена сумма на {new_summ} по дате {update_rows[2][1]}.")

        con.commit()

    select_data()

    print("\n=== Автодемонстрация завершена ===")


def auto_fill_data():
    product_names = ["Кофе", "Чай", "Сахар", "Мука", "Молоко", "Шоколад", "Мед", "Мармелад"]
    for _ in range(10):
        data = (datetime.date.today() - datetime.timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        product_id = random.randint(100, 999999)
        product_name = random.choice(product_names)
        expences = random.randint(100, 10000)
        summ = random.randint(1000, 100000)
        curs.execute(f'INSERT INTO "Расходы" VALUES ("{data}", {product_id}, "{product_name}", {expences}, {summ});')
    con.commit()
    print("Таблица заполнена случайными данными.")

def main_menu():
    create_table()
    while True:
        print("\nВыберите действие:")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Поиск записей")
        print("4. Удаление записей")
        print("5. Редактирование записей")
        print("6. Автовыполнение всех команд")
        print("7. Автозаполнение строками")
        print("8. Выход")
        choice = input("Ваш выбор: ")
        match choice:
            case "1":
                insert_data()
            case "2":
                select_data()
            case "3":
                search_data()
            case "4":
                delete_data()
            case "5":
                update_data()
            case "6":
                auto_commands()
            case "7":
                auto_fill_data()
            case "8":
                print("Завершение работы.")
                con.close()
                break
            case _ :
                print("Некорректный выбор. Попробуйте снова.")
            

main_menu()
