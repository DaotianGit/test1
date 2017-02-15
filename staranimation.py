import pygame,sys
from pygame.locals import *

pygame.init()

FPS=20
fpsClock=pygame.time.Clock()

DISPLAYSURF=pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Animation')

WHITE=(255,255,255)
starImg=pygame.image.load('star1.png')
starx=10
stary=10
direction='right'

while True:
    DISPLAYSURF.fill(WHITE)

    if direction=='right':
        starx+=5
        if starx==280:
            direction='down'
    elif direction=='down':
        stary+=5
        if stary==220:
            direction='left'
    elif direction=='left':
        starx-=5
        if starx==10:
            direction='up'
    elif direction=='up':
        stary-=5
        if stary==10:
            direction='right'

    DISPLAYSURF.blit(starImg,(starx,stary))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
