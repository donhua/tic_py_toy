#!/usr/bin/env python
# -*- coding=utf-8 -*-

import pygame as pg
import rundom as rnd

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
    pg.display.flip()
    
    clock.tick(20)