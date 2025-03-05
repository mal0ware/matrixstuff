import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYBERPUNK_BLUE = (0, 255, 255)
CYBERPUNK_PINK = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Player settings
player_size = (50, 30)
player_color = CYBERPUNK_BLUE
player_speed = 5

# Bullet settings
bullet_color = WHITE
bullet_speed = 7
bullets = []

# Enemy settings
enemy_size = (40, 30)
enemy_color = GREEN
enemy_speed = 2

# Create player
player = pygame.Rect(SCREEN_WIDTH // 2 - player_size[0] // 2, SCREEN_HEIGHT - 60, *player_size)

# Create enemies
def create_enemies(rows, cols):
    enemies = []
    for row in range(rows):
        for col in range(cols):
            enemy_x = col * (enemy_size[0] + 20) + 50
            enemy_y = row * (enemy_size[1] + 20) + 50
            enemies.append(pygame.Rect(enemy_x, enemy_y, *enemy_size))
    return enemies

enemies = create_enemies(5, 8)
enemy_direction = 1

def move_enemies():
    global enemy_direction
    move_down = False
    for enemy in enemies:
        enemy.x += enemy_speed * enemy_direction
        if enemy.right >= SCREEN_WIDTH or enemy.left <= 0:
            move_down = True
    if move_down:
        for enemy in enemies:
            enemy.y += enemy_size[1]
        enemy_direction *= -1

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player.x += player_speed
            elif event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx - 5, player.top, 10, 20))
    
    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)
    
    # Move enemies
    move_enemies()
    
    # Check collisions
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                break
    
    # Draw player
    pygame.draw.rect(screen, player_color, player)
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)
    
    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, enemy_color, enemy)
    
    pygame.display.flip()
    clock.tick(60)

sys.exit()
