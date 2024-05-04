import sys

import pygame as pg

W = 1280
H = 720

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((W, H))  # создаем экран игры разрешением 1280х720px

pg.mixer.music.load('Luck.wav')  # загружаем фоновую музыку в игру
pg.mixer.music.set_volume(0.01)  # ставим громкость 1%
pg.mixer.music.play()  # play() можно передать -1 для бесконечного проигрывания музыки

sound1 = pg.mixer.Sound('fast.wav')
sound2 = pg.mixer.Sound('Keyboard.wav')

while True:  # цикл игры
	for event in pg.event.get():  # обработчик событий pygame
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
		elif event.type == pg.KEYUP:
			if event.key == pg.K_1:
				pg.mixer.music.pause()  # поставить фоновую музыку на паузу
				# pg.mixer.music.stop()  # полностью остановить
			elif event.key == pg.K_2:
				pg.mixer.music.unpause()  # продолжить с места остановки
				# pg.mixer.music.play()  # начать проигрывание сначала
				pg.mixer.music.set_volume(0.15)
			elif event.key == pg.K_3:
				pg.mixer.music.unpause()
				pg.mixer.music.set_volume(0.5)
		elif event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:  # нажали на левую кнопку мыши
				sound1.play()
			elif event.button == 3:  # нажали на правую кнопку мыши
				sound2.play()
