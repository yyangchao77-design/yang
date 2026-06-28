import pygame
import settings

class World:
    def __init__(self):
        self.tiles = []

        # 简单地面生成（后面会升级成泰拉瑞亚）
        for x in range(settings.WORLD_WIDTH):
            for y in range(settings.WORLD_HEIGHT):

                if y > 80:
                    tile_type = "dirt"
                elif y == 80:
                    tile_type = "grass"
                else:
                    tile_type = None

                if tile_type:
                    self.tiles.append((x, y, tile_type))

    def draw(self, screen, camera_x=0):
        for x, y, tile in self.tiles:

            px = x * settings.BLOCK_SIZE - camera_x
            py = y * settings.BLOCK_SIZE

            rect = pygame.Rect(px, py, settings.BLOCK_SIZE, settings.BLOCK_SIZE)

            if tile == "grass":
                color = settings.GRASS_COLOR
            elif tile == "dirt":
                color = settings.DIRT_COLOR
            else:
                color = (0, 0, 0)

            pygame.draw.rect(screen, color, rect)
