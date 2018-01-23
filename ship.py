# -*- coding:utf-8 -*-
import pygame
# from setting import Settings
class Ship():
    '''管理飞船的类'''

    def __init__(self,ai_settings,screen):
        #初始化飞船并设置其初始的位置
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取图形的外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将新的飞船放置在屏幕底部的中央
        self.rect.centerx = self.screen_rect.centerx   #元素x轴居中
        self.rect.bottom = self.screen_rect.bottom     #元素与屏幕边缘相邻
        # self.rect.center = self.screen_rect.center
        # self.rect.up = self.screen_rect.up
        # self.rect.down = self.screen_rect.down
        #飞船移动的标志
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False

        #在属性center中存储小数
        self.center = float(self.rect.centerx)

    def update(self):
        '''根据移动标志的状态调整飞船的位置'''
        # if self.moving_right:
        #     self.rect.centerx += 1
        # if self.moving_left:
        #     self.rect.centerx -= 1
        # 更新飞船的center值，不是rect
        # if self.moving_right:
        #     self.center += self.ai_settings.ship_speed_factor
        # if self.moving_left:
        #     self.center -= self.ai_settings.ship_speed_factor
        # speed = initialize_dynamic_settings(self)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            # self.center += self.ai_settings.initialize_dynamic_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # if self.moving_up and self.rect.up < self.screen_rect.up:
        #     self.center += self.ai_settings.ship_speed_factor
        # if self.moving_down and self.rect.down > 0:
        #     self.center -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象的位置
        self.rect.centerx = self.center

    def blitme(self):
        #在指定的位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        '''飞船居中显示'''
        self.center = self.screen_rect.centerx

