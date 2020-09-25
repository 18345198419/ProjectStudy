
import random

class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕背景色表
        color = [(0, 0, 255), (255, 245, 238), (127, 255, 212), (162, 181, 205)]
        num= random.randint()
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)
        # 飞船的设置
        # 飞船的移动速度
        self.ship_speed_factor = 5

