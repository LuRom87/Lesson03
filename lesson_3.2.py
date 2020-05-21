name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

def my_fun(**kwargs):
    return list(kwargs.value())
print(f"Имя - {name}; Фамилия - {surname}; Год рождения - {year}; Город - {city}; email - {email}; телефон - {phone}")
