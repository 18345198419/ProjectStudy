

class GameStats():
    """跟踪统计游戏信息"""

    def __init__(self, ai_settings):

        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit