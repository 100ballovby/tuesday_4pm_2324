import random


def reset_object_position(obj, screen_rect):
	"""
	Функция, которая сбрасывает позицию не игрового объекта
	:param obj: не игровой объект
	:param screen_rect: область квадрата экрана pygame
	"""
	obj.x = random.randint(50, screen_rect.right - 50)
	obj.y = -20


def check_screen_collision(obj, screen_rect):
	return obj.bottom >= screen_rect.bottom


def check_player_collision(obj, player):
	return obj.colliderect(player)


def non_playable_obj_move(obj, player, screen, speed_y):
	obj.y += speed_y
	screen_rect = screen.get_rect()  # получить "колижн модель" экрана
	if check_screen_collision(obj, screen_rect):
		reset_object_position(obj, screen_rect)
		return 'miss'

	if check_player_collision(obj, player):
		reset_object_position(obj, screen_rect)
		return 'catch'

	return None


def player_motion(obj, screen, speed_x):
	obj.x += speed_x
	screen_rect = screen.get_rect()
	if obj.right >= screen_rect.right:
		obj.right = screen_rect.right  # правая часть игрока фиксируется около правой части экрана
	elif obj.left <= screen_rect.left:
		obj.left = screen_rect.left


def draw_button(screen, text, x, y, w, h, color):
	import pygame as pg
	mouse_pos = pg.mouse.get_pos()  # фиксируем позицию курсора мыши
	click = pg.mouse.get_pressed()  # определяем, нажали ли на кнопку мыши (любую)
	button_rect = pg.Rect(x, y, w, h)
	if button_rect.collidepoint(mouse_pos):  # если курсор мыши находится над кнопкой
		if click[0]:
			return 'Start'
		color = (color[0] - 50, color[1] - 50, color[2] - 50)
	pg.draw.rect(screen, color, button_rect)
	text_surf = text.render('start', True, (0, 0, 0))
	text_rect = text_surf.get_rect(center=button_rect.center)
	screen.blit(text_surf, text_rect)
