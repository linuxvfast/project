# -*- coding:utf-8 -*-
import pygame
class Ship2():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp') #导入图片
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # self.rect.center = self.screen_rect.center   #固定图片在屏幕的中间
        self.rect.center = self.screen_rect.center
        self.rect.left = self.screen_rect.left

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1

    def blitme(self):
        self.screen.blit(self.image,self.rect) #画图

