#-*- coding:utf-8-*-
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    '''管理子弹的类'''
    def __init__(self,ai_settings,screen,ship):
        '''在飞船所在的位置创建子弹'''
        super(Bullet,self).__init__()
        self.screen = screen

        #在(0,0)位置创建表示子弹的矩形，在移动到指定的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #用小数表示子弹的位置
        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        #更新表示子弹位置的小数值
        self.x -= self.speed_factor
        #更新表示子弹的rect位置
        self.rect.x = self.x

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)