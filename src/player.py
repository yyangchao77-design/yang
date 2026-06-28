import pygame
import settings

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 28, 48)

        self.vel_x = 0
        self.vel_y = 0

        self.on_ground = False

    def handle_input(self):
        keys = pygame.key.get_pressed()

        self.vel_x = 0

        if keys[pygame.K_a]:
            self.vel_x = -settings.PLAYER_SPEED

        if keys[pygame.K_d]:
            self.vel_x = settings.PLAYER_SPEED

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = settings.JUMP_FORCE
            self.on_ground = False

    def update(self):
        self.handle_input()

        self.vel_y += settings.GRAVITY

        self.rect.x += int(self.vel_x)
        self.rect.y += int(self.vel_y)

        # 临时地面
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.vel_y = 0
            self.on_ground = True

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 200, 120), self.rect)
