import sys
from random import choice

import pygame as pg


def round_restart(obj, s_width, s_height, font, sc):
	global speed_x, speed_y, ball_moving, score_time
	obj.center = (s_width // 2, s_height // 2)
	speed_x *= choice([-1, 1])
	speed_y *= choice([-1, 1])

	sc.fill((255, 255, 255))
	pg.display.update()
	cur_time = pg.time.get_ticks()  # фиксирую время, когда была вызвана функция
	if cur_time - score_time < 700:  # прошла одна секунда
		num_3 = font.render('3', True, (0, 0, 0))
		sc.blit(num_3, [s_width // 2, s_height // 2])
	elif cur_time - score_time < 1400:  # прошло две секунды
		num_2 = font.render('2', True, (0, 0, 0))
		sc.blit(num_2, [s_width // 2, s_height // 2])
	elif cur_time - score_time < 2100:  # прошло три секунды
		num_1 = font.render('1', True, (0, 0, 0))
		sc.blit(num_1, [s_width // 2, s_height // 2])

	if cur_time - score_time < 2100:
		speed_x, speed_y = 0, 0
	else:
		speed_x = speed * choice([-1, 1])
		speed_y = speed * choice([-1, 1])
		score_time = None


def ball_move(obj, s_width, s_height, play_obj, opp, font, sc):
	global speed_x, speed_y, player_score, opponent_score, score_time  # из функции можно менять значение этих переменных
	obj.x += speed_x
	obj.y += speed_y

	if obj.top <= 0 or obj.bottom >= s_height:
		pong_sound.play()
		speed_y *= -1
	elif obj.left <= 0:
		score_sound.play()
		score_time = pg.time.get_ticks()
		player_score += 1
		round_restart(obj, s_width, s_height, font, sc)
	elif obj.right >= s_width:
		score_sound.play()
		score_time = pg.time.get_ticks()
		opponent_score += 1
		round_restart(obj, s_width, s_height, font, sc)

	if obj.colliderect(play_obj):
		pong_sound.play()
		if abs(obj.right - play_obj.left) < 10:
			speed_x *= -1
		elif abs(obj.bottom - play_obj.top) < 10 or abs(obj.top - play_obj.bottom) < 10:
			speed_x *= -1
	elif obj.colliderect(opp):
		pong_sound.play()
		if abs(obj.left - opp.right) < 10:
			speed_x *= -1
		elif abs(obj.bottom - opp.top) < 10 or abs(obj.top - opp.bottom) < 10:
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
pl_img = pg.image.load('assets/paddle2.png')  # картинка ракетки игрока
opp_img = pg.image.load('assets/paddle1.png')  # картинка ракетки оппонента
b_img = pg.image.load('assets/ball.png')  # картинка мяча

pl_img = pg.transform.scale(pl_img, (45, 150))
opp_img = pg.transform.scale(opp_img, (45, 150))
b_img = pg.transform.scale(b_img, (45, 45))

player = pl_img.get_rect()
player.center = (W - 50, H // 2)
opponent = opp_img.get_rect()
opponent.center = (40, H // 2)
ball = b_img.get_rect()
ball.center = (W // 2, H // 2)

# Sounds
pg.mixer.init()
pong_sound = pg.mixer.Sound('assets/pong.wav')
score_sound = pg.mixer.Sound('assets/fail.wav')
pong_sound.set_volume(0.2)
score_sound.set_volume(0.2)

speed = 7
p_speed = 0
o_speed = speed
ball_moving = False
speed_x = speed_y = speed * choice([-1, 1])
player_score = 0
opponent_score = 0
score_font = pg.font.SysFont('comicsans', 64)
score_time = True

pg.display.update()  # если на экране игры нужно что-то показать до начала игры
while True:  # главный цикл игры
	for event in pg.event.get():  # отслеживает события в игре
		if event.type == pg.QUIT:  # если окно игры закрывают крестиком
			sys.exit()  # завершить игру

	clock.tick(FPS)  # сменяет кадры в игре

	screen.fill(GREEN)
	pg.draw.aaline(screen, WHITE, [W // 2, 0], [W // 2, H])
	screen.blit(pl_img, player)
	screen.blit(opp_img, opponent)
	screen.blit(b_img, ball)

	player_score_text = score_font.render(str(player_score), True, VIOLET)
	opponent_score_text = score_font.render(str(opponent_score), True, VIOLET)

	screen.blit(player_score_text, [W // 2 + 50, H // 2])
	screen.blit(opponent_score_text, [W // 2 - 90, H // 2])

	if score_time:
		round_restart(ball, W, H, score_font, screen)

	pg.display.update()  # должен оставаться последним из отображений

	keys = pg.key.get_pressed()
	if keys[pg.K_UP]:
		p_speed = -speed
	elif keys[pg.K_DOWN]:
		p_speed = speed
	else:
		p_speed = 0

	ball_move(ball, W, H, player, opponent, score_font, screen)
	player_motion(player, p_speed, H)
	opponent_motion(opponent, ball, o_speed, H)
