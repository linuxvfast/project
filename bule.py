# -*- coding:utf-8 -*-
import sys,pygame
from ship2 import Ship2
from pygame.sprite import Group
from setting import Settings
import game_function as gf
def run_blue():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Alien Invasion")
    # ai_settings = Settings()
    ship = Ship2(screen)

    bg_color = (255,255,255)

    bullets = Group()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = True
                elif event.key == pygame.K_UP:
                    ship.moving_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False
                elif event.key == pygame.K_UP:
                    ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    ship.moving_down = False
        screen.fill(bg_color)
        ship.update()
        ship.blitme()  # 绘制飞船
        bullets.update()

        # 让最新绘制的屏幕可见
        pygame.display.flip()




run_blue()
