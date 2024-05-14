import pygame
import os
from run import run
pygame.font.init()

pygame.display.set_caption("jet fighter")
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

#YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
#YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

def main():
    run(BG, WIDTH, HEIGHT, WIN)
main()
