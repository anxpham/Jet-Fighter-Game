import pygame

def redraw_window(WIN, BG, main_font, level, lives, lost, lost_font, WIDTH, enemies, player):
    WIN.blit(BG, (0, 0))
    lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
    level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
    for enemy in enemies:
        enemy.draw(WIN)
    player.draw(WIN)
    if lost:
        lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
        WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
    pygame.display.update()