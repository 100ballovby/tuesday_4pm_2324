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
paused = False


# игровые объекты
player_img = pg.image.load('bowl.png').convert_alpha()
player_img = pg.transform.scale(player_img, (120, 40))
apple_img = pg.image.load('apple.png').convert_alpha()
bg_image = pg.image.load('bg.jpg').convert()
heart_img = pg.image.load('heart.png').convert_alpha()
heart_img = pg.transform.scale(heart_img, (50, 50))
heart_rect = heart_img.get_rect()

player = player_img.get_rect()
player.centerx = S_WIDTH // 2  # centerx устанавливает положение ЦЕНТРА объекта по горизонтали
player.y = S_HEIGHT - 50
apple = apple_img.get_rect()
apple.x, apple.y = random.randint(50, S_WIDTH - 50), -20

# print(pg.font.get_fonts()) <- список установленных шрифтов
pg.display.update()  # если на экране игры нужно что-то показать до начала игры
while True:  # главный цикл игры
    if missed_apples >= 3:
        paused = True
        score = 0
        missed_apples = 0

    for event in pg.event.get():  # отслеживает события в игре
        if event.type == pg.QUIT:  # если окно игры закрывают крестиком
            sys.exit()  # завершить игру
        elif event.type == pg.MOUSEBUTTONDOWN:
            if paused and 'Start' == gf.draw_button(screen, score_font, S_WIDTH // 2,
                                                    S_HEIGHT // 2, 100, 70, (200, 120, 80)):
                paused = False

    clock.tick(FPS)  # сменяет кадры в игре
    # screen.fill(WHITE)
    screen.blit(bg_image, (0, 0))

    # отображение информации
    if paused:
        # отображать текст о паузе
        text_surface = score_font.render('You lost!', True, (255, 255, 0))
        text_rect = text_surface.get_rect(center=(S_WIDTH // 2, S_HEIGHT // 2 - 50))
        screen.blit(text_surface, text_rect)
        gf.draw_button(screen, score_font, S_WIDTH * 0.456,
                       S_HEIGHT // 2, 100, 70, (200, 120, 80))
        pg.display.update()
    else:
        # pg.draw.rect(screen, BROWN, player)
        # pg.draw.circle(screen, RED, (apple.x, apple.y), 20)
        screen.blit(player_img, player)
        screen.blit(apple_img, apple)

        score_text = score_font.render('Score: ' + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 60))
        lives = 3 - missed_apples
        for i in range(lives):
            heart_rect.x = 10 + (i * heart_rect.width)
            heart_rect.y = 5
            screen.blit(heart_img, heart_rect)
        # missed_text = score_font.render('Lives: ' + msg, True, (0, 0, 180))
        #screen.blit(missed_text, (10, 50))

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
