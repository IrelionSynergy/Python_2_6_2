print('Введите натуральное число от 1 до 2е9:')
integer = int(input())

if integer >= 2e9:
    print('Введено неверное число. Введите число от 1 до 2е9')
else:
    count = 0
    for i in range(1, integer + 1):
        if integer % i == 0:
            count += 1
    print('Количество натуральных делителей для числа {d} равно: {c}'.format(d = integer, c = count))