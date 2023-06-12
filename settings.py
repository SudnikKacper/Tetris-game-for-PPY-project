#   Laura   Trzaska     11C
#   Kacper  Tonderys    11C
#   Kacper  Sudnik      11C

import pygame as pg

'''
ZMIENNE DO OKNA
'''

FPS = 60

vec = pg.math.Vector2

TILE_SIZE = 40
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
RES_W = FIELD_W * TILE_SIZE * 2
RES_H = FIELD_H * TILE_SIZE
RES = RES_W, RES_H
FIELD_COLOR = (44, 62, 80)


INIT_POS_OFFSET = vec(FIELD_W / 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.5, FIELD_H * 0.45)
CUSTOM_EVENT = pg.USEREVENT + 1

'''
CZASY ANIMACJI
'''
NORMAL_ANIM_TIME = 350 #to sa ms
FAST_ANIM_TIME = NORMAL_ANIM_TIME // 10




FIELD_COLOR = pg.image.load('Resources/Backgrounds/pexels-codioful-(formerly-gradienta)-7135121.jpg')



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

GAME_BACKGROUND = pg.image.load('Resources/Backgrounds/pexels-codioful-(formerly-gradienta)-7135121.jpg')
GAME_BACKGROUND = pg.transform.scale(GAME_BACKGROUND, RES)
MAIN_BACKGROUND = pg.image.load('Resources/Backgrounds/bckgrnd.jpg')
MAIN_BACKGROUND = pg.transform.scale(MAIN_BACKGROUND, FIELD_RES)
BCG_COLOR = (44, 62, 80)

