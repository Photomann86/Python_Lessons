def stepen_of_num(a, b):
    if b == 0:
        return 1 #любое число в степени 0 вернёт единицу
    if b<0:
        return stepen_of_num(a, b+1)*1/a #a в степени -b = 1/a^b
    return stepen_of_num(a, b-1)*a 
print('вбейте основание и показатель через Enter')
print(stepen_of_num(int(input()), int(input())))