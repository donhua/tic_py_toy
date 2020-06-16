import random

import pgztun

gamers = int(input("Количество игроков (не более 30): "))

def gamedollars():
    a = []
    for i in range(15):
        a.append(i)
        a.append(i)
    b = random.shuffle(a)
    return b

def stages(gamedollar, gamers: int):
    if gamers > 30:
        return
    b = []
    while len(gamedollar) >= gamers:
        c = []
        for i in range(gamers):
            c.append(gamedollar.pop())
        b.append(c)
    return b

def dollarin(a):
    screen.draw.text(str(a), (50, 30), color="orange")

WIDTH = 400
HEIGHT = 708

gamedollars()

def draw():
    screen.fill((128, 0, 0))
    dollarin(a)

def on_mouse_down():
    clock.schedule(dollarin, 1.0)

pgzrun.go()