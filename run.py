import pygame
import random

from event_handler import handle_events
from player import Player
from enemy import Enemy
from draw import redraw_window
pygame.font.init()

# Main function and game loop
def run(BG, WIDTH, HEIGHT, WIN):
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 35)
    result_font = pygame.font.SysFont("comicsans", 45)

    enemies = []
    wave_length = 0
    enemies_vel = 1

    player = Player(300, 650)
    player_vel = 5
    laser_vel = 8

    clock = pygame.time.Clock()

    lost = False
    win = False
    pause_count = 0
    win_count = 0

    # Main game loop
    while run:
        clock.tick(FPS)
        redraw_window(WIN, BG, main_font, level, lives, lost, win, result_font, WIDTH, enemies, player)

        if lives <= 0 or player.health <= 0:
            lost = True
            pause_count += 1

        if lost:
            if pause_count > FPS * 3:
                run = False
            else:
                continue

        if level == 10:
            win = True
            win_count += 1
            if win_count > FPS * 3:
                run = False
            else:
                continue

        # Spawning enemies
        if len(enemies) == 0:
            level += 1
            wave_length += 3
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-800, -20), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)


        for enemy in enemies[:]:
            enemy.move(enemies_vel)
            enemy.move_lasers(laser_vel, player, HEIGHT)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        if not handle_events(player, player_vel, laser_vel, WIDTH, HEIGHT, enemies):
            run = False

        player.move_lasers(-laser_vel, enemies, HEIGHT)
