import sys

import pygame as pg

pg.init()  # это находится наверху и инициализирует библиотеку

# создаем экран игры
W = 1280
H = 720
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Ping Pong game | PyGame')

FPS = 60
clock = pg.time.Clock()

# COLORS
GREEN = (171, 255, 228)
WHITE = (255, 255, 255)
VIOLET = (245, 88, 248)

# Config vars
pad_w = W * 0.02
pad_h = H * 0.2
ball_size = W * 0.04
sc_x = W // 2
sc_y = H // 2

# Game objects
player = pg.Rect(W - 30, sc_y, pad_w, pad_h)
opponent = pg.Rect(10, sc_y, pad_w, pad_h)
ball = pg.Rect(sc_x - ball_size // 2, sc_y - ball_size // 2, ball_size, ball_size)

pg.display.update()  # если на экране игры нужно что-то показать до начала игры
while True:  # главный цикл игры
	for event in pg.event.get():  # отслеживает события в игре
		if event.type == pg.QUIT:  # если окно игры закрывают крестиком
			sys.exit()  # завершить игру

	clock.tick(FPS)  # сменяет кадры в игре

	screen.fill(GREEN)
	pg.draw.rect(screen, VIOLET, player)
	pg.draw.rect(screen, VIOLET, opponent)
	pg.draw.aaline(screen, WHITE, [W // 2, 0], [W // 2, H])
	pg.draw.ellipse(screen, VIOLET, ball)

	pg.display.update()  # должен оставаться последним из отображений
