from  math import sin
import pygame as py

W, H = 1000, 400
WIN = py.display.set_mode((W, H))
angle = 0
FPS = 50
nextposX = 0


while True:
    WIN.fill(py.Color('black'))

    
    py.time.Clock().tick(FPS)
    offset = 0
    for i in range(0, W, 40):
        w = 37
        h = sin(angle + offset) * 200
        if h <= 0:
            h = 0
        py.draw.rect(WIN, (h, h, h) , (i + w * 0.4, H//2 - h/2, w, h))
        offset += 0.1
    angle += 0.05
    py.display.update()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()