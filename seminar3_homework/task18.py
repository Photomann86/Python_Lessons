from random import randint
list_num = [randint(1,51) for _ in range(int(input('количество элементов рандомного списка: ')))]
print(list_num)
num = int(input('введите число для поиска ближайшего из списка: '))
right_num = list_num[0]
for i in list_num:
    if abs(num - i) < abs(num - right_num):
        right_num = i
print('число, близкое к введённому: ',right_num)