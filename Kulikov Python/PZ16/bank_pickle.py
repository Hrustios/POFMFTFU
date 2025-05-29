# Блок 3
# Условие: Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохранять
# информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.

import pickle
from bank import Bank

def save_def(bank_objects, filename):#Сохраняет список объектов Bank в файл    
    with open(filename, 'wb') as f:
        pickle.dump(bank_objects, f)
    print(f"Сохранено {len(bank_objects)} объектов в файл '{filename}'.")


def load_def(filename):#Загружает список объектов Bank из файла
    with open(filename, 'rb') as f:
        bank_objects = pickle.load(f)
    print(f"Загружено {len(bank_objects)} объектов из файла '{filename}'.")
    return bank_objects

if __name__ == "__main__":
    bank1 = Bank(1000, 5)
    bank2 = Bank(2000, 4)
    bank3 = Bank(1500, 6)

    save_def([bank1, bank2, bank3], 'banks.pkl')

    loaded_banks = load_def('banks.pkl')
    ch = 1
    for i in loaded_banks:
        print(f"Банк {ch}: Баланс = {i.balance}, Процентная ставка = {i.procent_rate}")
        ch+=1
