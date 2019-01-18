#!/usr/bin/env python
# -*- coding=utf-8 -*-

import pygame as pg

pg.init()


black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

text01 = "TicTacToy Game" 


size=[700,500]
screen=pg.display.set_mode(size)
pg.display.set_caption(text01)
done=False
clock=pg.time.Clock()
 
# -------- Основной цикл программы -----------
while done==False:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done=True
    screen.fill(white)

    font = pg.font.SysFont('Calibri', 25, True, False)
    text = font.render("My text", True, black)
    screen.blit(text, [250,250])

    pg.display.flip()
    
    clock.tick(20)