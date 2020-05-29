
import sys
import random

import pygame
from pygame.locals import *

import classesDonhua


def title_win(level: int = 0):
    """Возвращает сообщение о текущем уровне игрока"""
    return "Текущий ровень: " + str(level)


def random_int(x: list):
    """Возвращает два целых числа для задания с суммой до x: int"""
    assert len(x) == 2, "Недопустимое количество аргументов для интервала значений"
    assert x[1]-x[0] >= 0, "Недопустимый интервал начений"
    a = random.randint(x[0], x[1])
    b = random.randint(x[0], x[1]-a)
    ints = [a, b]
    #assert x[0] <= sum(ints) >= x[1]
    return ints


def finish_value(ints):
    """Принимает список с целыми числами, возвращает сумму"""
    return sum(ints)


def num_sum(ints):
    """Принимает список с двумя целыми числами и преобразует в текст примера"""
    return str(ints[0])+"+"+str(ints[1])+"="


def level_dif(mylevel):
    """Реализует возможный интервал ответов"""
    if mylevel == 0:
        return [0, 4]
    if mylevel == 1:
        return [2, 6]
    if mylevel == 2:
        return [3, 8]
    if mylevel == 3:
        return [4, 10]
    return [0, 10]


def live_delete(live):
    """Удаляет 1 жизнь"""
    live = live.replace("*", "", 1)
    if len(live) == 0:
        pygame.quit()
        sys.exit()
    return live


def timing():
    """Реализация таймера"""
    start_ticks = pygame.time.get_ticks()  # starter tick
    while True:  # mainloop
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
        if seconds > 10:  # if more than 10 seconds close the game
            return

#набор цветовой палитры
color = {"BLACK": (0, 0, 0),
         "WHITE": (255, 255, 255),
         "RED": (255, 0, 0),
         "GREEN": (0, 255, 0),
         "BLUE": (0, 0, 255),}
win_WIDTH = 254
win_HEIGT = 150
button_size = 40
button_in_win = 6
speed_game = 3000
level = 4
score1 = 0
fps = 40
fontsize = 60
fontsize_lafe = 20
b = "Hi"
live = "*****"
frame_count = 0
frame_rate = 60
start_time = 90

interval = level_dif(level)
rndint = random_int(interval)


pygame.init()
mainClock = pygame.time.Clock()
winSurf = pygame.display.set_mode((win_WIDTH, win_HEIGT), 0, 32)
pygame.display.set_caption(title_win())

font = pygame.font.Font(None, fontsize)
font_lafe = pygame.font.Font(None, fontsize)

# различные размеры шрифта
headfont = pygame.font.Font(FONT, 80)
largefont = pygame.font.Font(FONT, 50)
mediumfont = pygame.font.Font(FONT, 38)
smallfont = pygame.font.Font(FONT, 28)
vsmallfont = pygame.font.Font(FONT, 17)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                a = random_int(interval)
                score1 += 1
                b = num_sum(a)
                pygame.display.set_caption("Очки:"+str(score1))
                live = live_delete(live)


    # белый фон
    winSurf.fill(color["WHITE"])

    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = frame_count // frame_rate

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = font.render(output_string, True, color["BLACK"])
    winSurf.blit(text, [250, 250])

    # --- Timer going down ---
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = font.render(output_string, True, color["BLACK"])

    winSurf.blit(text, [250, 280])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1

    text = font.render(b, True, color["BLACK"])
    text_lafe = font.render(live, True, color["RED"])
    koord_text = font.size(b)
    winSurf.blit(text, [(win_WIDTH-koord_text[0])//2, 10])
    winSurf.blit(text_lafe, [10, 10])
    pygame.display.flip()
    pygame.display.update()
    mainClock.tick(fps)
