# Необходимо создать таблицу "Расходы" со следующей структурой:
# дата ,код продукта ,наименование продукта ,расходы ,сумма.
# - добавление 10 записей
# - поиск (3 SQL-запроса с WHERE)
# - удаление (3 SQL-запроса с WHERE)
# - редактирование (3 SQL-запроса с WHERE)

import sqlite3
con = sqlite3.connect('expenses.db')
cursor = con.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Расходы (
                   data TEXT,
                   product_id INTEGER,
                   product_name TEXT,
                   expences INTEGER,
                   summ INTEGER
                   )''')
    con.commit()


def insert_data():
    data_to_insert = [
        ("2025-06-01", 1, "Хлеб", 200, 500),
        ("2025-06-01", 2, "Молоко", 150, 300),
        ("2025-06-01", 3, "Масло", 100, 700),
        ("2025-06-01", 4, "Сахар", 250, 450),
        ("2025-06-01", 5, "Мука", 180, 600),
        ("2025-06-01", 6, "Крупа", 130, 350),
        ("2025-06-01", 7, "Яйца", 90, 400),
        ("2025-06-01", 8, "Соль", 70, 100),
        ("2025-06-01", 9, "Мясо", 500, 1500),
        ("2025-06-01", 10, "Овощи", 220, 800)
    ]
    try:
        cursor.executemany('''INSERT INTO Расходы
                            VALUES (?, ?, ?, ?, ?)
                            ''', data_to_insert)
        con.commit()
    except sqlite3.Error as e:
        print("Ошибка вставки:", e)


def search_examples():
    print("Поиск по product_name = 'Молоко'")
    cursor.execute("SELECT * FROM Расходы WHERE product_name = 'Молоко'")
    print("\n".join(map(str, cursor.fetchall())))

    print("\nПоиск по summ > 800")
    cursor.execute("SELECT * FROM Расходы WHERE summ > 800")
    print("\n".join(map(str, cursor.fetchall())))

    print("\nПоиск по expences BETWEEN 100 AND 200")
    cursor.execute("SELECT * FROM Расходы WHERE expences BETWEEN 100 AND 200")
    print("\n".join(map(str, cursor.fetchall())))


def delete_examples():
    print(" Удаление по product_id = 10")
    cursor.execute("DELETE FROM Расходы WHERE product_id = 10")

    print(" Удаление по summ < 200")
    cursor.execute("DELETE FROM Расходы WHERE summ < 200")

    print(" Удаление по product_name = 'Крупа'")
    cursor.execute("DELETE FROM Расходы WHERE product_name = 'Крупа'")
    con.commit()


def update_examples():
    print("- Обновление summ на 1000 для product_id = 2")
    cursor.execute("UPDATE Расходы SET summ = 1000 WHERE product_id = 2")

    print("- Обновление expences на 300, если product_name = 'Сахар'")
    cursor.execute("UPDATE Расходы SET expences = 300 WHERE product_name = 'Сахар'")

    print("- Обновление product_name на 'Ржаной хлеб' при summ = 500")
    cursor.execute("UPDATE Расходы SET product_name = 'Ржаной хлеб' WHERE summ = 500")
    con.commit()


def show_all():
    cursor.execute("SELECT * FROM Расходы")
    records = cursor.fetchall()
    print("\n --- Все записи в таблице:")
    for row in records:
        print(" , ".join(map(str,row)))


def main():
    create_table()
    insert_data()
    print("\n== Выполняем поисковые запросы ==")
    search_examples()
    print("\n== Выполняем обновления ==")
    update_examples()
    print("\n== Выполняем удаления ==")
    delete_examples()
    show_all()
    input()
    exit()

main()