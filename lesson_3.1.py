
def my_f():
    try:
        arg_1 = float(input("Первое число: "))
        arg_2 = float(input("Второе число: "))
        res = arg_1 / arg_2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return "Делить на ноль НЕЛЬЗЯ!!!!"
    return res
print(my_f())