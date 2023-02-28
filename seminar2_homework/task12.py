from time import time
sum = int(input('сумма чисел: '))
prod = int(input('произведение:'))
answer = 'решения нет!'

start = time()
d = sum**2 - 4*prod
if d>=0:
    x1 = (sum + d**0.5)/2
    x2 = (sum - d**0.5)/2
    if x1*x2 == prod:
        answer = f"{x1}, {x2}"

print(answer)
print(time()-start)