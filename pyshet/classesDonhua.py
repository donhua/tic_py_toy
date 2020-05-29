import sys
import random

import pygame
from pygame.locals import *


class Plitka:
    def __init__(self, windowsSurfase, xpos, ypos, filename="1.png", logic=False):
        self.x = xpos
        self.y = ypos
        self.filename = filename
        self.bitmap = pygame.image.load(self.filename)
        self.rect = self.bitmap.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.windowsSurfase = windowsSurfase
        self.logic = logic

    def relogik(self):
        if self.logic:
            self.logic = True
        else:
            self.logic = False

    def render(self):
        self.windowsSurfase.blit(self.bitmap, [self.x, self.y])


class Zadanie:
    def __init__(self, windowsSurfase, tx="", xpos=0, ypos=0, font=None,
                 fontsize=80, COLORfont=(0, 255, 0), COLORbgr=(255, 255, 255)):
        self.tx = tx
        self.x = xpos
        self.y = ypos
        self.font = font
        self.fontsize = fontsize
        self.COLORfont = COLORfont
        self.COLORbgr = COLORbgr
        self.basicFont = pygame.font.SysFont(self.font, self.fontsize)
        self.text = self.basicFont.render(tx, True, self.COLORfont,
                                          self.COLORbgr)
        self.rect = self.text.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.windowsSurfase = windowsSurfase

    def dataTx(self):
        self.rnddata = random.shuffle(self.data)

    def render(self):
        self.windowsSurfase.blit(self.text, self.rect)


class Plauer:

    def __init__(self, life=3, score=0, name='Вика'):
        self.life = life
        self.score = score
        self.name = name

    def skoreCounter(self):
        self.sсore += 1

    def damag(self):
        self.life -= 1
        if self.life == 0:
            pygame.quit()
            sys.exit()

