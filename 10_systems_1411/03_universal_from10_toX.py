n = int(input('Enter decimal number: '))
base = int(input('Enter base: '))
res = ''

while n != 0:
    rem = n % base
    n //= base
    res = str(rem) + res

print(res)
