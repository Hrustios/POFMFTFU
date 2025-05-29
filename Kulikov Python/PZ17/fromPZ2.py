#Дано трехзначное число. Вывести вначале его последнюю цифру
#(единицы), а затем — его среднюю цифру (десятки)

import tkinter as tk

def process_number():
    num_str = entry_number.get()
    if not num_str.isdigit() or len(num_str) != 3:
        result_label.config(text="Ошибка! Введите трехзначное число.",fg="red")
    else:
        num = int(num_str)
        last_num = num % 10
        middle_num = (num // 10) % 10
        result_label.config(text=f"Последняя цифра: {last_num}\nСредняя цифра: {middle_num}",fg="blue")

root = tk.Tk()
root.title("Обработка трехзначного числа")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Введите трехзначное число:", font=("Arial", 12)).pack(pady=10)

entry_number = tk.Entry(root, font=("Arial", 12))
entry_number.pack(pady=5)

process_button = tk.Button(root, text="Показать результат", command=process_number, font=("Arial", 12))
process_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

root.mainloop()