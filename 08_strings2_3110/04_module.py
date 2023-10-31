import random as r
import string as st

print(st.ascii_lowercase)  # вывести все маленькие буквы
print(st.ascii_uppercase)  # вывести все большие буквы
print(st.digits)  # вывести все цифры
print(st.punctuation)  # вывести все специальные символы

print(r.randint(1, 10))  # выводит случайное число от 1 до 10
print(r.choice(st.ascii_uppercase))  # достает случайный символ из последовательности
