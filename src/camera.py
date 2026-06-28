class Camera:
    def __init__(self):
        self.x = 0

    def follow(self, player_rect):
        # 让摄像机跟随玩家
        target_x = player_rect.centerx - 640
        self.x += (target_x - self.x) * 0.1
