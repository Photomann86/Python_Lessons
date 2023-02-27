n = int(input())
count_1 = count_0 = 0
for i in range(n):
    coin = int(input())
    if coin:
        count_1 += 1
    else:
        count_0 += 1

if count_1 > count_0:
    print(count_1)
else:
    print(count_0)
