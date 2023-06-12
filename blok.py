#   Laura   Trzaska     11C
#   Kacper  Tonderys    11C
#   Kacper  Sudnik      11C

from settings import *


class Blok(pg.sprite.Sprite):
    def __init__(self, figura, pos):
        self.figura = figura
        self.pos = vec(pos) + INIT_POS_OFFSET
        self.next_pos = vec(pos) + NEXT_POS_OFFSET
        self.zyje = True

        super().__init__(figura.tetris.sprites)

        self.image = figura.kolor
        self.rect = self.image.get_rect()


    def set_pos(self):
        pos = [self.next_pos, self.pos][True]
        self.rect.topleft = pos * TILE_SIZE

    def update(self):
        self.czy_zyje()
        self.set_pos()

    def czy_zyje(self):
        if not self.zyje:
            self.kill()

    # TODO ZJEBANA ROTACJA DO POPRAWY
    def rotacja(self, pos_pivot):
        temp = self.pos - pos_pivot
        obrocony = temp.rotate(90)
        return obrocony + pos_pivot

    def czy_dotyka(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (y < 0 or not self.figura.tetris.pozycje_figur[y][x]):
            return False
        return True
