import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("ex04/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()