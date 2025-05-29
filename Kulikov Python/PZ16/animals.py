# Блок 2
# Условие: Создайте класс "Животное", который содержит информацию о виде и возрасте животного.
# Создайте классы "Собака" и "Кошка", которые наследуются от класса "Животное" и содержат информацию о породе.

def dev():
    sel = input('У вас кот или собака?[ответ: "кот" или "собака"]\n')
    if sel.lower() == "кот" or sel.lower() == "кошка":
        cat = Cat(int(input("Введите возраст кошки: ")),input("Введите породу кошки: "))
        print(cat.info())
    elif sel.lower() == "собака" or sel.lower() == "пёс":
        dog = Dog(int(input("Введите возраст собаки: ")),input("Введите породу собаки: "))
        print(dog.info())
    else: 
        print("Вы некорректно ввели вид животного")
        dev()
class Animal:
    def __init__(self, species: str, age: int):
        self.species = species
        self.age = age

    def info(self):
        return f"Вид: {self.species}, возраст: {self.age} лет"


class Dog(Animal):
    def __init__(self, age: int, breed: str):
        super().__init__('Собака', age)
        self.breed = breed

    def info(self):
        return f"{super().info()}, порода: {self.breed}"


class Cat(Animal):
    def __init__(self, age: int, breed: str):
        super().__init__('Кошка', age)
        self.breed = breed

    def info(self):
        return f"{super().info()}, порода: {self.breed}"


if __name__ == "__main__":
    dev()
