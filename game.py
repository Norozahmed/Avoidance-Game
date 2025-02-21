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
NEON_CYAN = (0, 255, 255)  # Player
NEON_GREEN = (0, 255, 0)  # Items
DEEP_PURPLE = (128, 0, 128)  # Enemies
NEON_PINK = (255, 105, 180)  # Outlines
NEON_YELLOW = (255, 255, 0)  # Score text
WHITE = (255, 255, 255)  # Button text
BUTTON_COLOR = (50, 50, 50)  # Dark gray for buttons
HOVER_COLOR = (100, 100, 100)  # Light gray for hover effect

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
    def __init__(self, x, y, size, base_speed):
        self.x = x
        self.y = y
        self.size = size  # Radius for circle
        self.base_speed = base_speed
        self.speed = base_speed
        self.rect = pygame.Rect(self.x - size, self.y - size, size * 2, size * 2)

    def move(self, keys, held_buttons):
        # Keyboard Input
        if keys[pygame.K_LEFT] or held_buttons["left"]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or held_buttons["right"]:
            self.x += self.speed
        if keys[pygame.K_UP] or held_buttons["up"]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or held_buttons["down"]:
            self.y += self.speed

        # Keep player within screen bounds
        self.x = max(self.size, min(self.x, WIDTH - self.size))
        self.y = max(self.size, min(self.y, HEIGHT - self.size))

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

# Button class for on-screen controls
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover = False
        self.pressed = False

    def draw(self, surface):
        # Change color if hovered
        if self.hover or self.pressed:
            pygame.draw.rect(surface, HOVER_COLOR, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        font = pygame.font.SysFont(None, 24)  # Smaller font for smaller buttons
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Game setup
base_speed = 5
player = Player(WIDTH // 2, HEIGHT // 2, 20, base_speed)
items = []
enemies = []
score = 0
font = pygame.font.SysFont(None, 36)
max_items, max_enemies = 3, 5

# Speed multiplier for button presses
speed_multiplier = 2.0  # Adjusted to 2.0 for more noticeable speed boost

# Create buttons for on-screen controls
button_size = 30
buttons = {
    "left": Button(10, HEIGHT - 2 * button_size - 10, button_size, button_size, "<", BUTTON_COLOR),
    "right": Button(60, HEIGHT - 2 * button_size - 10, button_size, button_size, ">", BUTTON_COLOR),
    "up": Button(35, HEIGHT - 3 * button_size - 10, button_size, button_size, "^", BUTTON_COLOR),
    "down": Button(35, HEIGHT - 2 * button_size + 10, button_size, button_size, "v", BUTTON_COLOR),
}

# Keep track of which buttons are currently held down
held_buttons = {"left": False, "right": False, "up": False, "down": False}

# Game loop
running = True
game_over = False
clock = pygame.time.Clock()

def reset_game():
    global player, items, enemies, score, game_over, held_buttons
    player = Player(WIDTH // 2, HEIGHT // 2, 20, base_speed)
    items = []
    enemies = []
    score = 0
    game_over = False
    # Reset held_buttons to stop continuous movement
    held_buttons = {"left": False, "right": False, "up": False, "down": False}
    # Also reset button pressed states visually
    for button in buttons.values():
        button.pressed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            pos = pygame.mouse.get_pos()
            if restart_button.is_clicked(pos):
                reset_game()
            elif quit_button.is_clicked(pos):
                running = False

        # Button press and release events
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            for button_name, button in buttons.items():
                if button.is_clicked(pos):
                    held_buttons[button_name] = True
                    button.pressed = True
                    player.speed = player.base_speed * speed_multiplier

        if event.type == pygame.MOUSEBUTTONUP and not game_over:
            pos = pygame.mouse.get_pos()
            for button_name, button in buttons.items():
                if button.is_clicked(pos):
                    held_buttons[button_name] = False
                    button.pressed = False
                    player.speed = player.base_speed

        # Hover effect for buttons
        if event.type == pygame.MOUSEMOTION and not game_over:
            pos = pygame.mouse.get_pos()
            for button in buttons.values():
                button.hover = button.is_clicked(pos)

    if not game_over:
        # Player movement based on held buttons and keyboard
        keys = pygame.key.get_pressed()
        player.move(keys, held_buttons)

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
                game_over = True

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

        # Draw on-screen buttons
        for button in buttons.values():
            button.draw(screen)

    else:
        # Game over screen
        screen.fill((0, 0, 0))
        game_over_text = font.render(f"Game Over! Score: {score}", True, NEON_YELLOW)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))  # Restart and Quit buttons
        restart_button = Button(WIDTH // 2 - 100, HEIGHT // 2, 100, 50, "Restart", BUTTON_COLOR)
        quit_button = Button(WIDTH // 2 + 10, HEIGHT // 2, 100, 50, "Quit", BUTTON_COLOR)
        restart_button.draw(screen)
        quit_button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
