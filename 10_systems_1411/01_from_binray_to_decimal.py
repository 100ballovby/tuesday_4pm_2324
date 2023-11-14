binary = input('Enter binary number: ')

n = 0

for i in range(len(binary)):
    tmp = len(binary) - i - 1
    n += int(binary[i]) * pow(2, tmp)

print(n)
