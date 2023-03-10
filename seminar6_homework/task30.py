print('начальное значение, шаг, количество элементов прогрессии')
start, step, limit = map(int, input().split())
result = list([i for i in range(start, start+step*limit, step)])
print(*result)