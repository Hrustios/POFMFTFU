#Создать список на 10 элементов 
# Найти сумму чисел кратных 7
import random

listik = []
i = 0
sum_list_numbers = 0

while len(listik) < 10 :
    listik.append(random.randint(0,1000))
    
print(listik)

for i in listik:
    if (i%7) == 0:
        sum_list_numbers += i

print(sum_list_numbers) 