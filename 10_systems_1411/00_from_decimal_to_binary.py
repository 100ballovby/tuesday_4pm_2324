n = int(input('Number: '))
binary = ''

while n != 0:
    rem = n % 2
    n //= 2
    binary = str(rem) + binary

print(binary)
