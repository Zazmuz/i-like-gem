import pygame as pg
import pygame.gfxdraw
import numpy as np
from random import randint
import time




def draw_circle(surface, x, y, r, color):
    pg.gfxdraw.aacircle(surface, x ,y ,r, color)
    pg.gfxdraw.filled_circle(surface, x ,y ,r, color)

def circle_collision(x1, y1, r1, x2, y2, r2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return dist < (r1 + r2) ** 2



