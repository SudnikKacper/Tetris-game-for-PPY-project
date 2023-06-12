#   Laura   Trzaska     11C
#   Kacper  Tonderys    11C
#   Kacper  Sudnik      11C

from settings import *
from tetris import Tetris
import sys

class App:
    def __init__(self):
        pg.init()
        self.button1_rect = pg.Rect(630, 10, 100, 50)
        self.button2_rect = pg.Rect(460, 10, 100, 50)
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(RES)
        self.game_surface = pg.Surface(FIELD_RES)
        self.button1_surface = pg.Surface(vec(110, 50))
        self.button1_text = pg.font.SysFont(None, 24).render("KONIEC", True, (155,164,181))
        self.button2_surface = pg.Surface(vec(110, 50))
        self.button2_text = pg.font.SysFont(None, 24).render("OD NOWA", True, (155,164,181))
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)
        self.game_paused = False
        self.game_running = True
        self.s_surface = pg.Surface(vec(300,100))
        self.s_text = pg.font.SysFont(None, 24).render("SCORE", True, (155,164,181))
        self.s_score = pg.font.SysFont(None, 24).render(str(self.tetris.score), True, (155,164,181))
        self.hs_text = pg.font.SysFont(None, 24).render("HIGHSCORE", True, (155,164,181))
        self.hs_score = pg.font.SysFont(None, 24).render(str(self.tetris.hscore), True, (155,164,181))





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
        self.s_surface.blit(self.s_text, (20, 20))
        self.s_surface.blit(self.s_score, (250, 20))
        self.s_surface.blit(self.hs_text, (20, 60))
        self.s_surface.blit(self.hs_score, (250, 60))
        self.screen.blit(self.s_surface, (450, 650))

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
                if event.button == 1:
                    if self.button1_rect.collidepoint(event.pos):
                        pg.quit()
                        sys.exit()
                    if self.button2_rect.collidepoint(event.pos):
                        self.__init__()
            elif event.type == CUSTOM_EVENT:
                self.fast_anim_trigger = False
                self.anim_trigger = False

    def run(self):
        while True:
            if self.tetris.hscore < self.tetris.score:
                self.tetris.hscore = self.tetris.score

            if self.tetris.update_score:
                self.s_score = pg.font.SysFont(None, 25).render(str(self.tetris.score), True, (155, 164, 181))
                self.hs_score = pg.font.SysFont(None, 25).render(str(self.tetris.hscore), True, (155, 164, 181))
                self.s_surface.fill('black')
                self.s_surface.blit(self.s_text, (20, 20))
                self.s_surface.blit(self.s_score, (250, 20))
                self.s_surface.blit(self.hs_text, (20, 60))
                self.s_surface.blit(self.hs_score, (250, 60))
                self.screen.blit(self.s_surface, (450, 650))

            self.check_events()
            self.update()
            self.draw()
            if self.tetris.score%1000 == 0:
                self.fast_a_f_boi = self.fast_a_f_boi - 50


if __name__ == '__main__':
    app = App()
    app.run()
