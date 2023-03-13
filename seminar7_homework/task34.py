#задача 34: "про Винни-пуха и его стишки"
def ritmo(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя': #если во фразе встречаются согласные - то есть слог
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])
print('введите винни-пуховский стих, для разделения фраз используйте пробел: ')
stih = input()
if ritmo(stih):
    print('парам пам-пам')
else:
    print('пам парам')
