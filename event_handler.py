import pygame



def handle_events(player, player_vel, laser_vel, WIDTH, HEIGHT, enemies):
    enemy_shoot = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.x - player_vel > 0 - 45:  # Move left
        player.x -= player_vel
    if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH + 45:  # Move right
        player.x += player_vel
    if keys[pygame.K_w] and player.y - player_vel > 0:  # Move up
        player.y -= player_vel
    if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT:  # Move down
        player.y += player_vel
    if keys[pygame.K_SPACE]:
        player.shoot()
    #using the class player's function to set up speed, direction, collision obj, and the HEIGHT for off screen
    player.move_lasers(-laser_vel, enemies, HEIGHT)

    return True