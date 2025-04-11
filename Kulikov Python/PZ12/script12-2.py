# Составить генератор (yield), который выводит из строки только буквы

def main():
    _str = input("Введите строку для обработки: \n")
    text = AlphaOut(_str)
    literals = [x for x in text]
    print("\nБуквы из введённой строки:\n"," ".join(literals))
    
def AlphaOut(_str):
    for x in _str:
        if x.isalpha():
            yield x
            
main()