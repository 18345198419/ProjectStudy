import random


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕背景色表
        color = [(0, 0, 255), (255, 245, 238), (127, 255, 212), (162, 181, 205)]
        num = random.randrange(0, 4, 1)
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = color[num]

        # 飞船的设置
        #  飞船数量
        self.ship_limit = 1

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 子弹数
        self.bullet_allowed = 3

        # 外星人设置
        self.fleet_speed = 10
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 获取初始速度信息
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        # 飞船的移动速度
        self.ship_speed_factor = 5
        # 子弹移动速度
        self.bullet_speed_factor = 3
        # 外星人移动速度
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
