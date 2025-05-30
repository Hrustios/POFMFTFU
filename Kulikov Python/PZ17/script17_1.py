import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Создайте заказ")
root.geometry("600x600")
root.resizable(False, False)

# Заголовок
title = tk.Label(root, text="Создайте заказ", font=("Arial", 16, "bold"), bg="#15CEAF", fg="white", pady=10)
title.pack(fill=tk.X)

# Секция 1: Информация о заказе
frame_order = tk.LabelFrame(root, text="1 Информация о заказе", font=("Arial", 12, "bold"))
frame_order.pack(padx=10, pady=10, fill="x")

tk.Label(frame_order, text="Номер заказа *").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_order_number = tk.Entry(frame_order, width=40)
entry_order_number.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_order, text="Название товара").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_product = tk.Entry(frame_order, width=40)
entry_product.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_order, text="Количество *").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_quantity = tk.Entry(frame_order, width=10)
entry_quantity.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Секция 2: Контактная информация
frame_contact = tk.LabelFrame(root, text="2 Контактная информация", font=("Arial", 12, "bold"))
frame_contact.pack(padx=10, pady=10, fill="x")

tk.Label(frame_contact, text="Ваше имя").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_name = tk.Entry(frame_contact, width=40)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_contact, text="Ваш email *").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_email = tk.Entry(frame_contact, width=40)
entry_email.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_contact, text="Ваш телефон *").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_phone = tk.Entry(frame_contact, width=40)
entry_phone.insert(0, "+7 (")
entry_phone.grid(row=2, column=1, padx=5, pady=5)
tk.Label(frame_contact, text="Формат: +7 (999) 999-99-99", font=("Arial", 8, "italic")).grid(row=3, column=1, sticky="w", padx=5)

# Секция 3: Информация о доставке
frame_delivery = tk.LabelFrame(root, text="3 Информация о доставке", font=("Arial", 12, "bold"))
frame_delivery.pack(padx=10, pady=10, fill="x")

tk.Label(frame_delivery, text="Адрес *").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
text_address = tk.Text(frame_delivery, width=45, height=3)
text_address.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_delivery, text="Время доставки").grid(row=1, column=0, sticky="w", padx=5, pady=5)
combo_hour = ttk.Combobox(frame_delivery, values=[f"{i:02}" for i in range(8,19)], width=5)
combo_hour.grid(row=1, column=1, sticky="w", padx=5, pady=5)
combo_hour.set("08")
combo_minute = ttk.Combobox(frame_delivery, values=[f"{i:02}" for i in range(0,60,10)], width=5)
combo_minute.grid(row=1, column=1, sticky="w", padx=60, pady=5)
combo_minute.set("00")

root.mainloop()
