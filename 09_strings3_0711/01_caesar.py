text = input('Сообщение: ')
shift = int(input('Сдвиг шифра: '))
encrypted = ''

for char in text:
    if char.isalpha():
        shift_amount = shift % 26
        if char.islower():
            shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
        else:
            shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        encrypted += shifted_char  # добавляю сдвинутую букву к строке
    else:
        encrypted += char

print(encrypted)
