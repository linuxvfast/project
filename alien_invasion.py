# -*- coding:utf-8 -*-
import pygame
from setting import Settings
from ship import Ship
# from alien import Alien
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    #初始化游戏并创建一个屏幕
    pygame.init()
    # screen = pygame.display.set_mode((1200,800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置屏幕背景色
    # bg_color = (230,230,230)

    #绘制飞船
    ship = Ship(ai_settings,screen)

    #存储子弹的编组
    bullets = Group()

    #创建外星人
    # alien =Alien(ai_settings,screen)
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #存储统计信息
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #创建按钮
    play_button = Button(ai_settings,screen,"start")

    #开始游戏主循环
    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_alien(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
