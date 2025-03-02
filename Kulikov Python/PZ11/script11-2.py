file = open("text18-15.txt",'r',encoding='utf-16')
summary = file.read() #переменная, хранящая содержимое файла
sum_lit = 0 #sum of literals

for x in summary:
    if x.islower():
        sum_lit += 1
        # print(sum_lit)
        # print(x)

print(summary)
print(f'\nОбщее количество букв в нижнем регистре: {sum_lit}')

file_new = open('new_text18-15.txt','w',encoding="utf-8")
file_new.write(summary.upper())

file.close()
file_new.close()
input()