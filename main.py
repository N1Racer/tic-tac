from setting import *
from Board import Board
import pygame as pg
board = Board(W, H, 200)

pg.init()
screen = pg.display.set_mode((W, H))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)

    screen.fill('white')
    board.render(screen)
    pg.display.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        pg.quit()
        exit()