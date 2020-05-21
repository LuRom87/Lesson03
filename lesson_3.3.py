def my_func():
    arg_1 = int(input("Первое число: "))
    arg_2 = int(input("Второе число: "))
    arg_3 = int(input("Третье число: "))
    if arg_1 > arg_3 and arg_2 > arg_3:
        return arg_1 + arg_2
    elif arg_2 > arg_1 and arg_3 > arg_1:
        return  arg_2 + arg_3
    elif arg_3 > arg_2 and arg_1 > arg_2:
        return arg_3 + arg_1

print(my_func())


"""
def my_func():
    arg_1 = int(input("Первое число: "))
    arg_2 = int(input("Второе число: "))
    arg_3 = int(input("Третье число: "))

    z = [arg_1, arg_2, arg_3]
    z.remove(min(arg_1, arg_2, arg_3))
    return sum(z)
print(my_func())
"""