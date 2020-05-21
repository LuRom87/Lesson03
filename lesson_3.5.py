def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число или Z чтобы выйти - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'z' or number[el] == 'Z':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма {sum_res}')
    print(f'Окончательная сумма {sum_res}')


my_sum()