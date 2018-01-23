# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import  Sprite

class Bullet2(Sprite):
    '''对飞船发射的子弹管理类'''
    def __init__(self,setscreen,screen,xing):
        '''在飞船的位置上创建一个子弹对象'''
        super().__init__()
        self.screen = screen

        #在（0.0）坐标处创建一个子弹的矩形，之后在调整位置
        self.rect = pygame.Rect(0,0,setscreen.bullet_width,setscreen.bullet_height)   #子弹不是图像，需要使用pygame的rect画一个矩形
        self.rect.centery = xing.rect.centery
        self.rect.right = xing.rect.right

        #存储用小数表示的子弹位置
        self.x = float(self.rect.x)
        self.color = setscreen.bullet_color
        self.speed_factor = setscreen.bullet_speed_factor

    def update(self):
        '''向右移动子弹'''
        #更新表示子弹位置的小数
        self.x += self.speed_factor
        #更新表示子弹rect的位置
        self.rect.x = self.x

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)