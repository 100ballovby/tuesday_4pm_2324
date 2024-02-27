import random


def non_playable_obj_move(obj, player, screen, speed_y):
	obj.y += speed_y
	screen_rect = screen.get_rect()  # получить "колижн модель" экрана
	if obj.bottom >= screen_rect.bottom:
		obj.x = random.randint(50, screen_rect.right - 50)
		obj.y = -20
		return 'miss'
	elif obj.colliderect(player):
		obj.x = random.randint(50, screen_rect.right - 50)
		obj.y = -20
		return 'catch'


def player_motion(obj, screen, speed_x):
	obj.x += speed_x
	screen_rect = screen.get_rect()
	if obj.right >= screen_rect.right:
		obj.right = screen_rect.right  # правая часть игрока фиксируется около правой части экрана
	elif obj.left <= screen_rect.left:
		obj.left = screen_rect.left
