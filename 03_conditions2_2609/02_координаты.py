coord_x = int(input('Введите число: '))
coord_y = int(input('Введите число: '))


if coord_x > 0 and coord_y > 0:
    print(1)
elif coord_x < 0 and coord_y > 0:
    print(2)
elif coord_x < 0 and coord_y < 0:
    print(3)
elif coord_x > 0 and coord_y < 0:
    print(4)
else:
    print('0 is on axis')

