#   Laura   Trzaska     11C
#   Kacper  Tonderys    11C
#   Kacper  Sudnik      11C

import pygame as pg

vec = pg.math.Vector2

FPS = 60
NORMAL_ANIM_TIME = 350 #to sa ms
FAST_ANIM_TIME = 15 #to sa ms




FIELD_COLOR = (71, 69, 64)

TILE_SIZE = 50
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

INIT_POS_OFFSET = vec(FIELD_W / 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)

PORUSZANIE_FIGUR = {
    'LEWO': vec(-1, 0),
    'DOL': vec(0, 1),
    'PRAWO': vec(1, 0),
}

'''
TEKSTURY
'''



FIGURY = {
    'T': {'points': [(0, 0), (-1, 0), (1, 0), (0, -1)], 'color': pg.transform.scale(pg.image.load('Resources/Klocki/czerwony.png'),(TILE_SIZE, TILE_SIZE))},
    'O': {'points': [(0, 0), (0, -1), (1, 0), (1, -1)], 'color': pg.transform.scale(pg.image.load('Resources/Klocki/green.png'),(TILE_SIZE, TILE_SIZE))},
    'J': {'points': [(0, 0), (-1, 0), (0, -1), (0, -2)], 'color': pg.transform.scale(pg.image.load('Resources/Klocki/magenta.png'),(TILE_SIZE, TILE_SIZE))},
    'L': {'points': [(0, 0), (1, 0), (0, -1), (0, -2)], 'color': pg.transform.scale(pg.image.load('Resources/Klocki/niebieski.png'),(TILE_SIZE, TILE_SIZE))},
    'I': {'points': [(0, 0), (0, 1), (0, -1), (0, -2)], 'color': pg.transform.scale(pg.image.load('Resources/Klocki/orange.png'),(TILE_SIZE, TILE_SIZE))},
    'S': {'points': [(0, 0), (-1, 0), (0, -1), (1, -1)], 'color': pg.transform.scale(pg.image.load('Resources/Klocki/purple.png'),(TILE_SIZE, TILE_SIZE))},
    'Z': {'points': [(0, 0), (1, 0), (0, -1), (-1, -1)], 'color': pg.transform.scale(pg.image.load('Resources/Klocki/turqoise.png'),(TILE_SIZE, TILE_SIZE))}
}

# BACKGROUND = pg.image.load('')
GAME_FIELD = pg.image.load('Resources/Backgrounds/pexels-codioful-(formerly-gradienta)-7135121.jpg')
