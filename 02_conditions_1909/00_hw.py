# task 1 сложить цифры двузначного числа
n = int(input('введите двузначное число: '))

tens = n // 10  # при делении ЛЮБОГО двузначного числа на 10, вы получите разряд десятков
units = n % 10  # при нахождении остатка от деления ЛЮБОГО числа на 10, вы получите разряд единиц

print(f'{tens} + {units} = {tens + units}')

# task 2 сложить цифры трехзначного числа
n1 = int(input('введите трехзначное число: '))
hundreds = n1 // 100
tens = n1 % 100 // 10  # 123 % 10 = 23, 23 // 10 = 2
units = n1 % 10

print(f'{hundreds} + {tens} + {units} = {hundreds + tens + units}')



