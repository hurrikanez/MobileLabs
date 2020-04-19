# Конева Ксения Павловна 243125, группа N3347, вариант 11
# Протарифицировать абонента с IP-адресом 17.248.150.51
# с коэффициентом k: 0,5руб/Мб
# td - flow duration [2]
# ibyt - input bytes [12]
# obyt - output bytes [14]
import csv
import matplotlib.pyplot as plt


ipadr = '17.248.150.51'
k = 0.5

# Функция тарификации
def tarif(lst):
    ibyt = 12
    obyt = 14
    traffic = 0
    cost = 0
    for row in lst:
        traffic += (float(row[ibyt]) + float(row[obyt]))
    traffic /= (1024 ** 2)
    cost = round((traffic * k), 4)
    return cost


lst = []
with open('nfcapd_20200.csv') as file:
    data = csv.reader(file)
    for row in data:
        for item in row:
            if item == ipadr:
                lst.append(row)
pcost = tarif(lst)
print(f'Total for {ipadr}: {pcost} rubles.')
# Рисуем график
data_x = []
data_y = []
plt.title('График зависимости объема трафика от времени')
plt.ylabel('Объем трафика, байты')
plt.xlabel('Время, c')
traf = 0
time = 0
data_x.append(time)
data_y.append(traf)
for row in lst:
    time += float(row[2]) 
    traf += (float(row[12]) + float(row[14]))
    data_y.append(traf)
    data_x.append(time)
plt.plot(data_x, data_y)
plt.grid()
plt.show()
