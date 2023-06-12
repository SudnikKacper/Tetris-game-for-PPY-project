#   Laura   Trzaska     11C
#   Kacper  Tonderys    11C
#   Kacper  Sudnik      11C




'''
# TODO POPRAWA ROTACJI
# TODO HIGHSCORE
# TODO GUI
# TODO IM DALJE TYM SZYBCIEJ NAPIERDALA
# TODO IM DALEJ TO ZMIENIA TŁO I TEKSTURE BLOCZKÓW
'''



from settings import *
from figura import Figura
import math


class Tetris:
    def __init__(self, app):
        self.speeed = False
        self.app = app
        self.sprites = pg.sprite.Group()
        self.pozycje_figur = self.get_pos_figur()
        self.figura = Figura(self)

    def zapisz_pos_figury(self):
        for blok in self.figura.blocks:
            x, y = int(blok.pos.x), int(blok.pos.y)
            self.pozycje_figur[y][x] = blok

    def sprawdz_rzedy(self):
        rzad = FIELD_H - 1

        for y in range(FIELD_H - 1, -1, -1):
            for x in range(FIELD_W):
                self.pozycje_figur[rzad][x] = self.pozycje_figur[y][x]

                if self.pozycje_figur[y][x]:
                    self.pozycje_figur[rzad][x].pos = vec(x, y)

            if sum(map(bool, self.pozycje_figur[y])) < FIELD_W:
                rzad -= 1
            else:
                for x in range(FIELD_W):
                    self.pozycje_figur[rzad][x].zyje = False
                    self.pozycje_figur[rzad][x] = 0

    def get_pos_figur(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def czy_koniec_spadania(self):
        if self.figura.koniec_ruchu:
            self.speeed = False
            self.zapisz_pos_figury()
            self.figura = Figura(self)

    def kontrola_lewo_prawo(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.figura.move(kierunek='LEWO')
        elif pressed_key == pg.K_RIGHT:
            self.figura.move(kierunek='PRAWO')
        elif pressed_key == pg.K_UP:
            self.figura.rotacja()
        elif pressed_key == pg.K_DOWN:
            self.speeed = True

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black', (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speeed]
        if trigger:
            self.figura.update()
            self.sprawdz_rzedy()
            self.czy_koniec_spadania()
        self.sprites.update()

    def draw(self):
        self.draw_grid()
        self.sprites.draw(self.app.screen)
