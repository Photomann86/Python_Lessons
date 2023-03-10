def s(a,b):
    if b < 0 < a:
        a, b = b, a
    if b == 0:
        return a
    return s(a+1, b-1)

n = int(input('первое слагаемое: '))
m = int(input('второе слагаемое: '))
print('сумма: ', s(n,m))

