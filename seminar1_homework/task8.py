"""Задача 8: Требуется определить, можно ли от шоколадки размером 
n x m долек отломить k долек, если разрешается сделать один разлом 
 по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no"""
m = int(input('введите m долек: '))
n = int(input('введите n долек: '))
k = int(input('введите количество долек, которое хотите отломить за один раз: '))
if k % m == 0 or k % n == 0:
    print('данное количество долек можно отломить за один раз ')
else:
    print('не по-братски делишь, однако!')