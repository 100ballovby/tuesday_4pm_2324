import sys

import pygame as pg

pg.init()  # это находится наверху и инициализирует библиотеку

# создаем экран игры
S_WIDTH = 1280
S_HEIGHT = 720
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

FPS = 60
clock = pg.time.Clock()

x = 10

pg.display.update()  # если на экране игры нужно что-то показать до начала игры
while True:  # главный цикл игры
    for event in pg.event.get():  # отслеживает события в игре
        if event.type == pg.QUIT:  # если окно игры закрывают крестиком
            sys.exit()  # завершить игру

    clock.tick(FPS)  # сменяет кадры в игре

    screen.fill((255, 255, 255))  # заливка экрана игры белым цветом

    # нарисуем на экране синий прямоугольник в координатах х:10,у:10, ширина 100, высота 75
    pg.draw.rect(screen, (79, 146, 255), (x, 10, 100, 75))

    pg.display.update()  # должен оставаться последним из отображений

    x += 2  # изменяю переменную x
