import pygame
import settings
from player import Player
from world import World
from camera import Camera
class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        )

        pygame.display.set_caption("PixelWorld")

        self.clock = pygame.time.Clock()

        self.player = Player()
        self.world = World()
        self.running = True
def run(self):
    while self.running:
        self.clock.tick(settings.FPS)

        self.handle_events()
        self.update()
        self.draw()

    pygame.quit()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill(settings.SKY_COLOR)

        self.player.draw(self.screen)

        pygame.display.flip()
