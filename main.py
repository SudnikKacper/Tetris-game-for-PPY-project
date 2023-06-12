#   Laura   Trzaska     11C
#   Kacper  Tonderys    11C
#   Kacper  Sudnik      11C

from settings import *
from tetris import Tetris

import sys


class App:
    def __init__(self):
        self.score = 0
        pg.init()
        self.button1_rect = pg.Rect(680, 10, 100, 50)
        self.button2_rect = pg.Rect(560, 10, 100, 50)
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(RES)
        self.game_surface = pg.Surface(FIELD_RES)
        self.button1_surface = pg.Surface(vec(100, 50))
        self.button1_text = pg.font.SysFont(None, 24).render("KONIEC", True, (155,164,181))
        self.button2_surface = pg.Surface(vec(100, 50))
        self.button2_text = pg.font.SysFont(None, 24).render("OD NOWA", True, (155,164,181))
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)
        self.game_paused = False
        self.game_running = True



    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        self.fast_a_f_boi = NORMAL_ANIM_TIME
        pg.time.set_timer(self.user_event, self.fast_a_f_boi)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.blit(MAIN_BACKGROUND, (0,0))
        self.screen.blit(GAME_BACKGROUND, (400, 0))
        self.tetris.draw()
        self.button1_surface.blit(self.button1_text, (20, 20))
        self.screen.blit(self.button1_surface,  (self.button1_rect.x, self.button1_rect.y))
        self.button2_surface.blit(self.button2_text, (12, 20))
        self.screen.blit(self.button2_surface, (self.button2_rect.x, self.button2_rect.y))

        pg.display.flip()

    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):

                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                self.tetris.kontrola_lewo_prawo(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Sprawdzenie, czy lewy przycisk myszy został naciśnięty
                    if self.button1_rect.collidepoint(event.pos):  # Sprawdzenie, czy kursor myszy jest nad przyciskiem
                        pg.quit()
                    if self.button2_rect.collidepoint(event.pos):  # Sprawdzenie, czy kursor myszy jest nad przyciskiem
                        self.__init__()
            elif event.type == CUSTOM_EVENT:
                self.fast_anim_trigger = False
                self.anim_trigger = False

    def run(self):
        while True:
            self.score += 1
            self.check_events()
            self.update()
            self.draw()
            if self.score%1000 == 0:
                self.fast_a_f_boi = self.fast_a_f_boi - 50


if __name__ == '__main__':
    app = App()
    app.run()
