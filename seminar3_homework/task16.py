from random import choices
numb = int(input('введите количество элементов: '))
list_nums = choices(range(numb*2), k = numb)
print(list_nums)
result = list_nums.count(int(input('повторяющийся элемент:')))
print(f"->", result)
