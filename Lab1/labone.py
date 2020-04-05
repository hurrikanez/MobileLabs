# Конева Ксения Павловна 243125, группа N3347, вариант 11
# Протарифицировать абонента с номером 911926375 с коэффициентом k: 
# 1руб/минута исходящие звонки, 1руб/минута входящие, 
# смс - первые 5шт бесплатно, далее 1руб/шт

import csv

#Функция для тарификации
def tarif(lst):
    callcost = 0
    smscost = 0
    cost = 0
    for row in lst:
        callcost += float(row[calldur]) * k
    for row in lst:
        if float(row[smsnum]) <= freesms:
            smscost == 0
        else:
            smscost += (float(row[smsnum]) - 5) * k
    callcost = round(callcost, 2)
    smscost = round(smscost, 2)
    cost = callcost + smscost 
    listcost = [callcost, smscost, cost]
    return listcost


num = '911926375' 
k = 1
freesms = 5
origin = 1
dest = 2
calldur = 3
smsnum = 4

# Создаем список из нужных для обработки строк (Парсинг CSV)
lst = []
with open('data.csv') as file:
    data = csv.reader(file)
    for row in data:
        for item in row:
            if item == num:
                lst.append(row)

# Вывод:
totalcost = tarif(lst)
print(f'''Number: {num} 
Call Cost: {totalcost[0]}
Message cost: {totalcost[1]}
Total Cost: {totalcost[2]}''')
