from random import randint
import pygame as pg
import sys

def check_bound(obj_rct,scrn_rct):
    """
    obj_rct：こうかとんrct,または,爆弾rct
    src_rct：スクリーンrct
    領域内：+1/領域外：-1
    """
    yoko, tate = 1, 1
    if obj_rct.left < scrn_rct.left or scrn_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scrn_rct.top or scrn_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    #背景
    bg_sfc = pg.image.load("ex04/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    #こうかとん
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900,400
    #爆弾
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0)) #四隅の黒い部部を透過させる
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0,scrn_rct.width)
    bomb_rct.centery = randint(0,scrn_rct.height)

    vx, vy = 1, 1 #bombの移動速度
  

    clock = pg.time.Clock()
    
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_states = pg.key.get_pressed()
        #こうかとん
        if key_states[pg.K_w]: tori_rct.centery -= 1
        if key_states[pg.K_s]: tori_rct.centery += 1
        if key_states[pg.K_a]: tori_rct.centerx -= 1
        if key_states[pg.K_d]: tori_rct.centerx += 1
        yoko,tate = check_bound(tori_rct,scrn_rct)
        if yoko == -1:
            if key_states[pg.K_a]:
                tori_rct.centerx += 1
            if key_states[pg.K_d]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_w]:
                tori_rct.centery += 1
            if key_states[pg.K_s]:
                tori_rct.centery -= 1
        scrn_sfc.blit(tori_sfc,tori_rct)
        #爆弾
        yoko,tate = check_bound(bomb_rct,scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)

        if tori_rct.colliderect(bomb_rct):
            return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()