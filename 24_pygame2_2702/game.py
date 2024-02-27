import random
import sys

import pygame as pg

import game_functions as gf

pg.init()  # это находится наверху и инициализирует библиотеку

# ЦВЕТА
WHITE = (255, 255, 255)
RED = (245, 71, 59)
BROWN = (69, 54, 42)

# создаем экран игры
S_WIDTH = 1280
S_HEIGHT = 720
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

FPS = 60
clock = pg.time.Clock()

# игровые переменные (логика)
speed_y = 5

# игровые объекты
player = pg.Rect(0, S_HEIGHT - 50, S_WIDTH * 0.12, S_HEIGHT * 0.04)
player.centerx = S_WIDTH // 2  # centerx устанавливает положение ЦЕНТРА объекта по горизонтали
apple = pg.Rect(random.randint(50, S_WIDTH - 50), 40, 40, 40)

pg.display.update()  # если на экране игры нужно что-то показать до начала игры
while True:  # главный цикл игры
	for event in pg.event.get():  # отслеживает события в игре
		if event.type == pg.QUIT:  # если окно игры закрывают крестиком
			sys.exit()  # завершить игру

	clock.tick(FPS)  # сменяет кадры в игре
	screen.fill(WHITE)
	pg.draw.rect(screen, BROWN, player)
	pg.draw.circle(screen, RED, (apple.x, apple.y), 20)

	pg.display.update()  # должен оставаться последним из отображений

	# здесь обрабатываем логику игры
	gf.non_playable_obj_move(apple, speed_y)
