month = int(input('Введите номер месяца: '))


if month >= 3 and month <= 5:
    print('Spring')
elif month >= 6 and month <= 8:
    print('Summer')
elif month >= 9 and month <= 11:
    print('Autumn')
elif month == 1 or month % 10 == 2:
    print('Winter')
else:
    print('Incorrect')

