alphabet = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}

n = int(input('Enter decimal number: '))
res = ''

while n != 0:
    rem = n % 16
    if rem > 9:
        rem = alphabet[rem]  # достать значение из словаря по ключу
    n //= 16
    res = str(rem) + res

print(res)
