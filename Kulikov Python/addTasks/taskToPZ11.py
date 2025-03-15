try:
    f_example = open("example.txt", 'r',encoding='utf-8')
    summary = f_example.read()
    f_copy_example = open("copy_example.txt",'w',encoding='utf-8')
    f_copy_example.write(summary)
    print("Копирование файла успешно завершено")
    print(f'Содержимое файла: \n{summary}')
    input()
except FileNotFoundError:
    print("Файл не обнаружен")
    input()
