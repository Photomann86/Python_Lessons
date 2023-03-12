def print_operation_table(operation, num_rows, num_cols):
    massive = [[operation(i,j) for i in range(1, num_rows+1)] for j in range(1, num_cols+1)] 
    #massive = [[operation(i,j) for i in range(0, num_rows+1)] for j in range(0, num_cols+1)]
    for i in massive:
        print(*[f"{x:3}" for x in i])
rows = int(input('введите количество строк: '))
cols = int(input('введите количество столбцов: '))
print_operation_table(lambda x, y: x*y, rows, cols)
