# -*- coding:utf-8 -*-
import pygame
class Ship_Test():
    def __init__(self,setscreen,screen):
        '''加载图片并获取属性信息'''
        self.screen = screen
        self.image = pygame.image.load('images/test.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #火箭放置屏幕最左边y轴中间
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        #上下方向的移动标志
        self.moving_down = False
        self.moving_up = False

        self.setscreen = setscreen
        self.center = float(self.rect.centery)
    def update(self):
        '''更新上下移动的位置'''
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.setscreen.ship_speed_factor
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.setscreen.ship_speed_factor

        self.rect.centery = self.center

    def blitme(self):
        '''屏幕显示'''
        self.screen.blit(self.image,self.rect)