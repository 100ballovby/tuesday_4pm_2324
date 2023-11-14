number = input('Enter binary number: ')
base = int(input('Enter base number: '))
res = 0

for i in range(len(number)):
    res = res * base + int(number[i])

print(res)
