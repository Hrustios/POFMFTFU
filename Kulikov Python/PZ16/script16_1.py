# Блок 1
# Условие: Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег.
from random import randint as rd

def withdr():
    _amount = int(input("Сколько снять со счёта: "))
    if _amount>_bank.balance :
        print("Недостаточно средств на балансе")
        withdr()
    elif _amount<= _bank.balance:
        _bank.getMoney(_amount)

class Bank:
    def __init__(self, balance: float, procent_rate: float): #инициализация атрибутов класса
        self.balance = balance
        self.procent_rate = procent_rate

    def procents(self):#добавление процентной ставки
        procent = self.balance * self.procent_rate / 100 #вычисление процентной надбавки
        self.balance += procent
        print(f"Начислены проценты: {procent:.2f}. Новый баланс: {self.balance:.2f}")

    def getMoney(self, amount: float):#снятие денег со счёта
            self.balance -= amount
            print(f"Снято {amount:.2f}. Новый баланс: {self.balance:.2f}")

if __name__ == "__main__":
    _sum = rd(400,5000)
    print(f"Ваш текущий баланс: {_sum}")
    _proc = rd(8,30)
    print(f"Ваша процентная ставка: {_proc}\n\nКалькуляция процентов...\n")
    _bank = Bank(_sum,_proc)
    _bank.procents()
    withdr()
    
     
