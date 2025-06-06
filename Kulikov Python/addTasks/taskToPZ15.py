#создать таблицу в бд 
# заполнить тремя записями и
# выполнить запрос на обновление любой записи по условию
# 
# Табоица Товары : Код товара, Наименование, количество товара на складе, оптовая цена

import sqlite3

con = sqlite3.connect('products.db')
cursor = con.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS "Товары" (
            "Код_товара" INTEGER ,
            "Наименование" TEXT ,
            "Количество_на_складе" INTEGER ,
            "Оптовая_цена" INTEGER )''')
    con.commit()

def insert_data():
    cursor.executemany('''INSERT INTO Товары (Код_товара, Наименование, Количество_на_складе, Оптовая_цена)
        VALUES (?, ?, ?, ?)''',
        [(1, 'Товар 1', 100, 10.5),
        (2, 'Товар 2', 200, 20.5),
        (3, 'Товар 3', 300, 30.5)])
    con.commit()

def update_data():
    cursor.execute('''UPDATE Товары
        SET Количество_на_складе = 150
        WHERE Код_товара = 1''')
    con.commit()

def display_data():
    cursor.execute('SELECT * FROM Товары')
    rows = cursor.fetchall()
    for row in rows:
        print(" , ".join(map(str,row)))

def main():
    create_table()
    insert_data()
    print("Таблица:")
    display_data()
    update_data()
    print("Данные после обновления:")
    display_data()
    input()
    con.close()
    
main()
