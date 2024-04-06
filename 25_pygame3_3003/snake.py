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


def get_high_score():
	file = open('high_score.txt', 'r')  # открываем файл в режиме чтения
	h_s = file.read()  # читаем и сохраняем содержимое файла в переменной
	file.close()  # закрываем файл
	return int(h_s)  # превращаем рекорд в число и возвращаем


def write_high_score(high_score):
	file = open('high_score.txt', 'w')  # открываем файл
	file.write(str(high_score))  # записываем в него рекорд
	file.close()  # закрыть возможность работать с файлом


def score(score, text, x, y):
	value = font_style.render(text + str(score), True, BLACK)
	screen.blit(value, (x, y))


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
GREEN = (85, 255, 0)



def game_loop():
	p_score = 0  # очки
	high_score = get_high_score()  # получаю рекорд из файла
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
			score(p_score, 'Очки: ', 0, 0)
			score(high_score, 'Рекорд: ', 0, 30)
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
				if p_score > high_score:
					write_high_score(score)
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

		screen.fill(BLUE)
		pg.draw.rect(screen, BLACK, [x1, y1, snake_block, snake_block])
		pg.draw.rect(screen, GREEN, [food_x, food_y, snake_block, snake_block])
		snake_head = []  # создаем список, в котором будет храниться показатель длины змейки при передвижении
		snake_head.append(x1)  # добавляю значение в список при изменении положения змеи по иксу
		snake_head.append(y1)  # добавляю значение в список при изменении положения змеи по игреку

		snake_list.append(snake_head)  # добавляю в список элемент змеи
		if len(snake_list) > snake_length:  # если список с сегментами стал длиннее допустимой длины змеи
			del snake_list[0]  # удаляем первый элемент из списка, чтобы змея не росла сама по себе
		for x in snake_list[:-1]:  # прохожусь по каждому сегменту змеи, кроме первого
			if x == snake_head:  # если координаты какого-то из сегментов совпадают с координатами головы
				write_high_score(p_score)
				game_close = True  # остановить игру
		our_snake(snake_block, snake_list)  # включаем механизм роста змеи

		score(p_score, 'Очки: ', 0, 0)
		score(high_score, 'Рекорд: ', 0, 30)
		pg.display.update()  # должен оставаться последним из отображений

		if x1 == food_x and y1 == food_y:  # если координаты головы змейки совпадают с координатами еды
			food_x = round(random.randrange(0, S_WIDTH - snake_block) / 10) * 10
			food_y = round(random.randrange(0, S_HEIGHT - snake_block) / 10) * 10
			snake_length += 1
			p_score += 1

		if x1 >= S_WIDTH or x1 < 0 or y1 >= S_HEIGHT or y1 < 0:
			if p_score > high_score:  # если количество очков больше, чем рекорд в игре
				write_high_score(p_score)
			game_close = True  # явно указываем, что игра заканчивается, когда выходим за пределы экрана
		x1 += x1_change
		y1 += y1_change

	pygame.display.update()
	pygame.quit()
	sys.exit()


game_loop()
