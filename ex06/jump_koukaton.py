import pygame as pg
import time
import math
import sys
from random import randint

screen_x = 1600 #スクリーンの横サイズ
screen_y = 900 #スクリーンの縦サイズ
jumping = False #ジャンプ中かの判定
bg_x = 0 
v = 0 

def main():
    global bg_x, jumping, v
    t_sta = time.time()
    clock = pg.time.Clock()
    #スクリーンの設定
    pg.display.set_caption("避けろ！こうかとん")
    scrn_sfc = pg.display.set_mode((screen_x,screen_y))
    scrn_rct = scrn_sfc.get_rect()

    #背景の設定
    bg_sfc = pg.image.load("fig/pg_bg3.jpg")
    bg_rct = bg_sfc.get_rect()

    #こうかとんの設定
    tori_sfc = pg.image.load("fig/2.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 350,450

    #障害物の設定
    bomb_sfc = pg.image.load("fig/bomb01.png")
    bomb_sfc = pg.transform.rotozoom(bomb_sfc,0,0.18)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.center = 1450,450

    #背景とスクリーン、こうかとん、障害物の描写
    while True:
        key_states = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if key_states[pg.K_ESCAPE]:
                return

        #背景スクロール設定        
        bg_x = (bg_x-2)%1600
        scrn_sfc.blit(bg_sfc,[bg_x-screen_x,0])
        scrn_sfc.blit(bg_sfc,[bg_x,0])
        bg_sfc.blit(bomb_sfc,bomb_rct)

        #ジャンプの設定
        if key_states[pg.K_UP] and jumping == False:
            jumping = True
            v = -5
        if jumping == True:
            v += 0.05
            tori_rct.centery += v
            if tori_rct.centery > 450:
                tori_rct.centery = 450
                jumping = False
                
        #着地が早くなる    
        if key_states[pg.K_DOWN] and jumping == True:
            v += 0.5
        scrn_sfc.blit(tori_sfc,tori_rct)
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()