n = int(input()) #количество кустов
# ввод количества ягод на каждом кусте через пробел. 
# Внимание! Количество введённых значений должно быть равно количеству кустов
kusty = [int(i) for i in input().split()] 
kust_max = 0
for i in range(-1, n-1):
    kust_sum = kusty[i-1]+kusty[i]+kusty[i+1]
    if kust_sum > kust_max:
        kust_max = kust_sum
print(kust_max)