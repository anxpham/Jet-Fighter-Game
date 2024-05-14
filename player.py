import pygame
from ship import Ship


class Player(Ship):
# playership
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = pygame.image.load("assets/main_player.png")
        self.laser_img = pygame.image.load("assets/pixel_laser_yellow.png")
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs, HEIGHT):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)