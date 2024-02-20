import sys

import pygame as pg

pg.init()  # это находится наверху и инициализирует библиотеку

# создаем экран игры
S_WIDTH = 1280
S_HEIGHT = 720
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

FPS = 60
clock = pg.time.Clock()

player = pg.Rect(0, 0, 100, 100)  # создал объект-игрока в виде квадратной области в 0;0
hor_speed = 5  # горизонтальная скорость объекта
ver_speed = 5  # вертикальная скорость объекта
player_2 = pg.Rect(S_WIDTH // 2, S_HEIGHT // 2, 50, 50)
rad = 25
motion = 'stop'

hit = False  # столкновения по умолчанию нет

pg.display.update()  # если на экране игры нужно что-то показать до начала игры
while True:  # главный цикл игры
    for event in pg.event.get():  # отслеживает события в игре
        if event.type == pg.QUIT:  # если окно игры закрывают крестиком
            sys.exit()  # завершить игру
        elif event.type == pg.KEYDOWN:  # если событие - кнопка клавиатуры нажата
            if event.key == pg.K_LEFT:  # если кнопка - стрелка влево  / pg.K_a (кнопка A)
                motion = 'left'
            elif event.key == pg.K_RIGHT:  # если кнопка - стрелка вправо  / pg.K_d (кнопка D )
                motion = 'right'
            elif event.key == pg.K_UP:
                motion = 'up'
            elif event.key == pg.K_DOWN:
                motion = 'down'
        elif event.type == pg.KEYUP:
            if event.key in [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]:  # если отпущенная кнопка находится в списке
                motion = 'stop'  # запретить двигаться
    clock.tick(FPS)  # сменяет кадры в игре
    screen.fill((63, 63, 63))

    pg.draw.rect(screen, (255, 255, 255), player)
    pg.draw.circle(screen, (0, 255, 0), (player_2.x, player_2.y), rad)

    if hit:
        screen.fill((255, 0, 0))  # экран заливается красным цветом
        player.x, player.y = 0, 0  # перемещаем белый квадрат в левый верхний угол экрана
        player_2.x, player_2.y = S_WIDTH // 2, S_HEIGHT // 2  # перемещаем круг в середину
        hit = False  # выключаем столкновение
    pg.display.update()  # должен оставаться последним из отображений

    player.x += hor_speed
    player.y += ver_speed
    if player.right > S_WIDTH or player.left < 0:  # если правая или левая граница player вышла за пределы ширины экрана
        hor_speed *= -1  # изменить значение скорости
    elif player.bottom > S_HEIGHT or player.top < 0:
        ver_speed *= -1

    if motion == 'left':
        player_2.x -= 7
    elif motion == 'right':
        player_2.x += 7
    elif motion == 'up':
        player_2.y -= 7
    elif motion == 'down':
        player_2.y += 7

    if player.colliderect(player_2):  # если колижн-модели игроков пересекаются между собой
        hit = True  # засчитать им столкновение
