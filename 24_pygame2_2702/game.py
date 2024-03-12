import random
import sys

import pygame as pg

import game_functions as gf

pg.init()  # это находится наверху и инициализирует библиотеку
# pg.font.init() <- пишется для инициализации работы с текстом при наличии pg.init() не нужна

# ЦВЕТА
WHITE = (255, 255, 255)
RED = (245, 71, 59)
BROWN = (69, 54, 42)

# создаем экран игры
S_WIDTH = 1280
S_HEIGHT = 720
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

# настройки шрифта
f1 = pg.font.Font(None, 36)  # объявление шрифта и его размера
text = f1.render('Hello!', True, (180, 0, 0))

f2 = pg.font.SysFont('comicsans', 24)  # объявление шрифта и его размера
text2 = f2.render("Hi hi!", True, (0, 0, 255))

score_font = pg.font.Font('MadimiOne-Regular.ttf', 28)

FPS = 60
clock = pg.time.Clock()

# игровые переменные (логика)
speed = 2
apple_speed = speed * 5
player_speed = 0
missed_apples = 0
score = 0

# игровые объекты
player = pg.Rect(0, S_HEIGHT - 50, S_WIDTH * 0.12, S_HEIGHT * 0.04)
player.centerx = S_WIDTH // 2  # centerx устанавливает положение ЦЕНТРА объекта по горизонтали
apple = pg.Rect(random.randint(50, S_WIDTH - 50), 40, 40, 40)

# print(pg.font.get_fonts()) <- список установленных шрифтов
pg.display.update()  # если на экране игры нужно что-то показать до начала игры
while True:  # главный цикл игры
    for event in pg.event.get():  # отслеживает события в игре
        if event.type == pg.QUIT:  # если окно игры закрывают крестиком
            sys.exit()  # завершить игру

    clock.tick(FPS)  # сменяет кадры в игре
    screen.fill(WHITE)
    pg.draw.rect(screen, BROWN, player)
    pg.draw.circle(screen, RED, (apple.x, apple.y), 20)

    score_text = score_font.render('Score: ' + str(score), True, (0, 0, 180))
    screen.blit(score_text, (10, 20))
    lives = 3 - missed_apples
    msg = ''
    for i in range(lives):
        msg += ' * '
    missed_text = score_font.render('Lives: ' + msg, True, (0, 0, 180))
    screen.blit(missed_text, (10, 50))


    pg.display.update()  # должен оставаться последним из отображений

    # здесь обрабатываем логику игры
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:  # если в списке нажатых кнопок кнопке K_LEFT соответствует значение True
        player_speed -= speed
    elif keys[pg.K_RIGHT]:
        player_speed += speed
    else:  # когда все кнопки отпущены
        player_speed = 0

    gf.player_motion(player, screen, player_speed)
    apple_catch = gf.non_playable_obj_move(apple, player, screen, apple_speed)

    if apple_catch == 'miss':
        missed_apples += 1
    elif apple_catch == 'catch':
        score += 10

    if missed_apples >= 3:
        sys.exit()
