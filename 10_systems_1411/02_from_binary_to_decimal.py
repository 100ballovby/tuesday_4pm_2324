number = input('Enter binary number: ')
base = 2
res = 0

for i in range(len(number)):
    res = res * base + int(number[i])

print(res)
