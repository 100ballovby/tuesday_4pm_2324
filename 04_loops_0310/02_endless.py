import time
"""НИКОГДА НЕ ИСПОЛЬЗУЙТЕ В УСЛОВНЫХ ЦИКЛАХ == и !="""
x = 10
# while x != 0:  <- не использовать, потому что получите бесконечные повторения
while x >= 0:  # пока значение переменной х не стало равным 0
    print(x)
    x -= 4  # так как мы умньшаем значение на 4, х никогда не станет нулем и цикл не закончится
    time.sleep(1)
print('x = ', x)