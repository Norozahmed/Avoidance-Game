import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoidance Game")

# Colors (RGB) - Adjusted for contrast with the background
NEON_CYAN = (0, 255, 255)    # Player
NEON_GREEN = (0, 255, 0)     # Items
DEEP_PURPLE = (128, 0, 128)  # Enemies
NEON_PINK = (255, 105, 180)  # Outlines
NEON_YELLOW = (255, 255, 0)  # Score text

# Load and darken background image (ensure it's saved as "bg.jpg" in the same folder)
try:
    background = pygame.image.load("bg.jpg").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Scale to fit window

    # Darken the background with a semi-transparent black overlay
    darken_overlay = pygame.Surface((WIDTH, HEIGHT))
    darken_overlay.fill((0, 0, 0))  # Black
    darken_overlay.set_alpha(100)  # Increased alpha for darker effect (adjust 0-255)
    background.blit(darken_overlay, (0, 0))
except FileNotFoundError:
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((0, 0, 0))  # Fallback to black if image not found

# Player class (Neon Cyan Circle)
class Player:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size  # Radius for circle
        self.speed = speed
        self.rect = pygame.Rect(self.x - size, self.y - size, size * 2, size * 2)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > self.size:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > self.size:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.size:
            self.y += self.speed
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        pygame.draw.circle(surface, NEON_CYAN, (int(self.x), int(self.y)), self.size)  # Circle for player
        pygame.draw.circle(surface, NEON_PINK, (int(self.x), int(self.y)), self.size, 2)  # Neon pink outline

# Item class (Neon Green Circle, matching player's style)
class Item:
    def __init__(self):
        self.size = 15  # Radius for circle (same as before)
        self.x = random.randint(self.size, WIDTH - self.size)
        self.y = random.randint(self.size, HEIGHT - self.size)
        self.rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)

    def draw(self, surface):
        # Simple circle with outline, matching player's style
        pygame.draw.circle(surface, NEON_GREEN, (int(self.x), int(self.y)), self.size)  # Main circle
        pygame.draw.circle(surface, NEON_PINK, (int(self.x), int(self.y)), self.size, 2)  # Neon pink outline

# Enemy class (Deep Purple Star-like Shape)
class Enemy:
    def __init__(self):
        self.size = 20  # Radius for circle
        self.x = WIDTH
        self.y = random.randint(self.size, HEIGHT - self.size)
        self.speed = random.randint(2, 5)
        self.rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)

    def move(self):
        self.x -= self.speed
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        # Star-like effect: Draw a circle with points
        pygame.draw.circle(surface, DEEP_PURPLE, (int(self.x), int(self.y)), self.size)  # Main circle
        for angle in range(0, 360, 72):  # 5 points (like a star)
            rad = angle * math.pi / 180
            px = self.x + (self.size + 5) * math.cos(rad)
            py = self.y + (self.size + 5) * math.sin(rad)
            pygame.draw.circle(surface, DEEP_PURPLE, (int(px), int(py)), 3)  # Small points
        pygame.draw.circle(surface, NEON_PINK, (int(self.x), int(self.y)), self.size, 2)  # Neon pink outline

# Game setup
player = Player(WIDTH // 2, HEIGHT // 2, 25, 5)  # Adjusted size for circle radius
items = []
enemies = []
score = 0
font = pygame.font.SysFont(None, 36)
max_items, max_enemies = 3, 5

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Spawn items and enemies
    if random.random() < 0.02 and len(items) < max_items:
        items.append(Item())
    if random.random() < 0.03 and len(enemies) < max_enemies:
        enemies.append(Enemy())

    # Update enemies
    for enemy in enemies[:]:
        enemy.move()
        if enemy.x < -enemy.size:
            enemies.remove(enemy)

    # Collision checks
    for item in items[:]:
        if player.rect.colliderect(item.rect):
            score += 1
            items.remove(item)
    for enemy in enemies[:]:
        if player.rect.colliderect(enemy.rect):
            running = False  # Game over

    # Draw everything
    screen.blit(background, (0, 0))  # Draw darkened background image
    player.draw(screen)
    for item in items:
        item.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    # Draw score
    score_text = font.render(f"Score: {score}", True, NEON_YELLOW)  # Neon yellow for contrast
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()