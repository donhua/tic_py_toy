#!/usr/bin/env python
# -*- coding=utf-8 -*-

import pygame as pg

import const
pg.init()

screen = pg.display.set_mode([const.win_size["ширина"], const.win_size["высота"])
pg.display.set_caption(const.tx001)
done = False
clock = pg.time.Clock()
 
# -------- Основной цикл программы -----------
while done == False:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.fill(const.color["белый"])

    font = pg.font.SysFont('Calibri', 25, True, False)
    text = font.render("My text", True, const.color["черный"])
    screen.blit(text, [250, 250])

    pg.display.flip()
    
    clock.tick(const.fps)
    