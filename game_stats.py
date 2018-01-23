# -*- coding:utf-8 -*-
class GameStats():
    '''跟踪统计信息'''
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        #游戏刚启动时处于活动状态,判断游戏是否继续
        self.game_active = False

    def reset_stats(self):
        # 初始化飞船的统计信息
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
