#-*- coding:utf-8-*-
class Settings():
    '''存储游戏(外星人入侵)的所有设置类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 500
        self.screen_height = 600
        self.bg_color = (255,255,255)

        #调整飞船的速度
        self.ship_speed_factor = 1.5

        #子弹设置(像素)
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60,60,60
        self.bullet_allowed = 5