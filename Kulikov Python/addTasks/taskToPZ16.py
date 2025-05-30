class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.history = []

    def show_balance(self):
        print(f'Баланс Вашего счета: {self.balance}')

    def show_history(self):
        print('\nИстория операций')
        for trans,amount in self.history:
            if amount > 0:
                print(f'{trans} \033[32m{amount}\033[0m')
            else:
                print(f'{trans} \033[31m{amount}\033[0m') 

    def deposit(self, amount:int):
        self.balance += amount
        self.show_balance()
        self.history.append(['Пополнение:', amount])

if __name__ == "__main__":
    account = BankAccount()
    account.show_balance()
    account.deposit(int(input("Пополняемая сумма: ")))
    account.show_history()