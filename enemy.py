import pygame
from ship import Ship

class Enemy(Ship):
    COLOR_MAP = {
        "green": (pygame.image.load("assets/dog.png"), pygame.image.load("assets/pixel_laser_green.png")),
        "red": (pygame.image.load("assets/red_ship.png"), pygame.image.load("assets/pixel_laser_red.png")),
        "blue": (pygame.image.load("assets/bird.png"), pygame.image.load("assets/pixel_laser_blue.png"))
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel
