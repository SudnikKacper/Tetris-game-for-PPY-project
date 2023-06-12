#   Laura   Trzaska     11C
#   Kacper  Tonderys    11C
#   Kacper  Sudnik      11C
from settings import *
from blok import Blok
import random


class Figura:
    def __init__(self, tetris, obecny=True):
        self.tetris = tetris
        self.shape = random.choice(list(FIGURY.keys()))
        self.kolor = FIGURY[self.shape]['color']
        self.blocks = [Blok(self, pos) for pos in FIGURY[self.shape]['points']]
        self.koniec_ruchu = False
        self.obecny = obecny

    def move(self, kierunek):
        kierunek_ruchu = PORUSZANIE_FIGUR[kierunek]
        nowa_pos = [blok.pos + kierunek_ruchu for blok in self.blocks]
        dotyka = self.czy_dotyka(nowa_pos)

        if not dotyka:
            for block in self.blocks:
                block.pos += kierunek_ruchu

        elif kierunek == 'DOL':
            self.koniec_ruchu = True

    def rotacja(self):
        if not self.shape == 'O':

            pos_pivot = self.blocks[0].pos
            nowa_pozycja = [blok.rotacja(pos_pivot) for blok in self.blocks]

            if not self.czy_dotyka(nowa_pozycja):
                for i, block in enumerate(self.blocks):
                    block.pos = nowa_pozycja[i]

    def czy_dotyka(self, block_pos):
        return any(map(Blok.czy_dotyka, self.blocks, block_pos))

    def update(self):
        self.move(kierunek='DOL')
