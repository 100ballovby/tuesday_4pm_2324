import random as r
import string as st

length = int(input('Введите длину пароля: '))
alphabet = st.ascii_lowercase  # алфавит пароля

print('Выберите, что добавить в пароль: ')
print('''
1 - большие буквы
2 - числа
3 - знаки препинания
0 - закончить''')
choice = int(input('Ваш выбор: '))
while choice != 0:
    match choice:  # сравниваем значение переменной choice
        case 1:  # случай, когда ввели 1
            alphabet += st.ascii_uppercase
        case 2:
            alphabet += st.digits
        case 3:
            alphabet += st.punctuation
    choice = int(input('Хотите что-то еще добавить? '))

passw_num = int(input('Сколько паролей вам нужно? '))

for passw in range(passw_num):
    password = ''
    for i in range(length):
        password += r.choice(alphabet)

    print(f'Ваш пароль: {password}')
