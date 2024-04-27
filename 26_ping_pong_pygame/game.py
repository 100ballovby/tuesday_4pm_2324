import sys
from random import choice

import pygame as pg


def round_restart(obj, s_width, s_height):
	global speed_x, speed_y
	obj.x = s_width // 2
	obj.y = s_height // 2
	speed_x *= choice([-1, 1])
	speed_y *= choice([-1, 1])


def ball_move(obj, s_width, s_height, play_obj, opp):
	global speed_x, speed_y, player_score, opponent_score  # из функции можно менять значение этих переменных
	obj.x += speed_x
	obj.y += speed_y

	if obj.top <= 0 or obj.bottom >= s_height:
		speed_y *= -1
	elif obj.left <= 0:
		player_score += 1
		round_restart(obj, s_width, s_height)
	elif obj.right >= s_width:
		opponent_score += 1
		round_restart(obj, s_width, s_height)
	elif obj.colliderect(play_obj) or obj.colliderect(opp):
		speed_x *= -1


def player_motion(obj, s, win_h):
	obj.y += s
	if obj.top <= 0:  # если ракетка упирается в верхнюю границу экрана
		obj.top = 0  # она останавливается на этом месте
	elif obj.bottom >= win_h:
		obj.bottom = win_h


def opponent_motion(obj, p_obj, s, win_h):
	if obj.top < p_obj.y:
		obj.y += s
	elif obj.bottom > p_obj.y:
		obj.y -= s

	if obj.top <= 0:
		obj.top = 0
	elif obj.bottom >= win_h:
		obj.bottom = win_h


pg.init()  # это находится наверху и инициализирует библиотеку
pg.font.init()

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

speed = 7
p_speed = 0
o_speed = speed
ball_moving = False
speed_x = speed_y = speed * choice([-1, 1])
player_score = 0
opponent_score = 0
score_font = pg.font.SysFont('comicsans', 64)

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

	player_score_text = score_font.render(str(player_score), True, VIOLET)
	opponent_score_text = score_font.render(str(opponent_score), True, VIOLET)

	screen.blit(player_score_text, [W // 2 + 50, H // 2])
	screen.blit(opponent_score_text, [W // 2 - 90, H // 2])

	pg.display.update()  # должен оставаться последним из отображений

	keys = pg.key.get_pressed()
	if keys[pg.K_UP]:
		p_speed = -speed
	elif keys[pg.K_DOWN]:
		p_speed = speed
	else:
		p_speed = 0

	ball_move(ball, W, H, player, opponent)
	player_motion(player, p_speed, H)
	opponent_motion(opponent, ball, o_speed, H)
