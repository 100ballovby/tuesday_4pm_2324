import random
import sys

import pygame
import pygame as pg

pg.init()  # это находится наверху и инициализирует библиотеку

# создаем экран игры
S_WIDTH = 800
S_HEIGHT = 600
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
pg.display.set_caption('Змейка')

FPS = 60
clock = pg.time.Clock()

font_style = pg.font.SysFont(None, 35)
snake_block = 10
snake_speed = 15


def message(msg, color):
	mesg = font_style.render(msg, True, color)
	screen.blit(mesg, [50, S_HEIGHT // 2])


def our_snake(snake_block, snake_list):
	for x in snake_list:
		pg.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])


# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (235, 73, 78)
BLUE = (113, 159, 235)


def game_loop():
	game_over = False
	game_close = False
	x1 = S_WIDTH // 2
	y1 = S_HEIGHT // 2
	x1_change = 0
	y1_change = 0
	snake_list = []  # создаем пустой список, в котором будем хранить элементы змеи
	snake_length = 1  # изначальная длина змеи
	food_x = round(random.randrange(0, S_WIDTH - snake_block) / 10) * 10
	food_y = round(random.randrange(0, S_HEIGHT - snake_block) / 10) * 10
	while not game_over:  # главный цикл игры
		while game_close:
			screen.fill(WHITE)
			message("You lost. Q - quit, C - replay", RED)
			pygame.display.update()
			for event in pg.event.get():
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_q:
						game_over = True
						game_close = False
					elif event.key == pg.K_c:
						game_loop()

		for event in pg.event.get():  # отслеживает события в игре
			if event.type == pg.QUIT:  # если окно игры закрывают крестиком
				game_over = True
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT:
					x1_change = -snake_block
					y1_change = 0
				elif event.key == pg.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
				elif event.key == pg.K_UP:
					x1_change = 0
					y1_change = -snake_block
				elif event.key == pg.K_DOWN:
					x1_change = 0
					y1_change = snake_block

		clock.tick(snake_speed)  # сменяет кадры в игре

		screen.fill(WHITE)
		pg.draw.rect(screen, BLACK, [x1, y1, snake_block, snake_block])
		pg.draw.rect(screen, BLUE, [food_x, food_y, snake_block, snake_block])

		pg.display.update()  # должен оставаться последним из отображений

		if x1 >= S_WIDTH or x1 < 0 or y1 >= S_HEIGHT or y1 < 0:
			game_close = True  # явно указываем, что игра заканчивается, когда выходим за пределы экрана

		x1 += x1_change
		y1 += y1_change

	pygame.display.update()
	pygame.quit()
	sys.exit()


game_loop()
