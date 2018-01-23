# -*- coding:utf-8 -*-
class Settings_test():

    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (220, 220, 220)
        self.bg_color_white = (255, 255, 255)
        self.ship_speed_factor = 1.5

        # 子弹设置【单位是像素】
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10
