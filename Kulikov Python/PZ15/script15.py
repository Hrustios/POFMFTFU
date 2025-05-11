import sqlite3

#Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для 
# автоматизированного контроля 
# затрат на производство продукции. 
# БД должна содержать таблицу 
# Расходы со следующей структурой записи: 
# Дата, Код продукта, 
# Наименование продукта, Расходы, Сумма.

def osn():
    con = sqlite3.connect("expences.db")
    cur = con.cursor()
    print("Успешное подключение к базе данных!")
    print("Создание таблицы...")
    cur.execute('''CREATE TABLE IF NOT EXISTS "Расходы"(
                data TEXT,
                product_id INTEGER,
                product_name TEXT,
                expences INTEGER,
                summ INTEGER
                );''')
    print("Успешное создание таблицы!")
    exe()
    con.close()

def exe():
    con = sqlite3.connect("expences.db")
    curs = con.cursor()
    print("Желаете ввести данные в таблицу? [Да/Нет]")
    res=input()
    
    if res.lower()=="да":
        data = input("Введите дату: ")
        product_id = int(input("Введите код продукта: "))
        product_name = input("Введите название продукта: ")
        expences = int(input("Введите расходы: "))
        summ = int(input("Введите сумму: "))
        curs.execute(f'INSERT INTO "Расходы" VALUES ("{data}",{product_id},"{product_name}",{expences},{summ});')
        con.commit()
        for row in curs.execute('SELECT * FROM "Расходы";'):
            print(row)
        exe()
    elif res.lower() == "нет":
        con.close()
        input("Завершение работы скрипта, нажмите Enter")
        exit()
    else: 
        print("Вы ввели некорректное значение в консоль")
        exe()

osn()