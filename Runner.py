import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load assets
CHARACTER_RUN_IMAGE = pygame.image.load("character_run1.png")  # Only one image for running
OBSTACLE_IMAGE = pygame.image.load("obstacle.png")
BACKGROUND_IMAGE = pygame.image.load("background.png")  # Background image

# Scale assets (making them larger)
CHARACTER_RUN_IMAGE = pygame.transform.scale(CHARACTER_RUN_IMAGE, (100, 100))  # Larger character
OBSTACLE_IMAGE = pygame.transform.scale(OBSTACLE_IMAGE, (100, 100))  # Larger obstacle
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Full screen background

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Running Game")
clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT - 150  # Lower the player slightly to fit the new size
        self.width = 100
        self.height = 100
        self.image = CHARACTER_RUN_IMAGE  # Use the single image
        self.jump = False
        self.jump_velocity = 0
        self.speed = 5  # Movement speed for the player

    def update(self):
        # Handle jumping
        if self.jump:
            self.y += self.jump_velocity
            self.jump_velocity += 1
            if self.y >= SCREEN_HEIGHT - 150:  # Check if player hits the ground
                self.y = SCREEN_HEIGHT - 150
                self.jump = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def start_jump(self):
        if not self.jump:
            self.jump = True
            self.jump_velocity = -15

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed

# Obstacle class
class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100

    def update(self):
        self.x -= 2  # Slow obstacle speed

    def draw(self, screen):
        screen.blit(OBSTACLE_IMAGE, (self.x, self.y))

# Button class for on-screen buttons
class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(self.text, True, BLACK)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_pressed(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Game loop variables
player = Player()
obstacles = []
score = 0
running = True

# Create buttons
move_up_button = Button(10, 10, 120, 50, GREEN, "Move Up")
move_down_button = Button(10, 70, 120, 50, RED, "Move Down")
move_left_button = Button(10, 130, 120, 50, BLUE, "Move Left")
move_right_button = Button(10, 190, 120, 50, BLUE, "Move Right")
jump_button = Button(10, 250, 120, 50, GREEN, "Jump")

# Game loop
while running:
    screen.fill(WHITE)
    screen.blit(BACKGROUND_IMAGE, (0, 0))  # Draw background

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Button presses
            if move_up_button.is_pressed(mouse_pos):
                player.move_up()
            if move_down_button.is_pressed(mouse_pos):
                player.move_down()
            if move_left_button.is_pressed(mouse_pos):
                player.move_left()
            if move_right_button.is_pressed(mouse_pos):
                player.move_right()
            if jump_button.is_pressed(mouse_pos):
                player.start_jump()

    # Automatically make the player jump when an obstacle approaches
    if obstacles:
        if obstacles[0].x < SCREEN_WIDTH / 2:  # Trigger jump when obstacle is near
            player.start_jump()

    # Update player
    player.update()

    # Update obstacles
    if random.random() < 0.02:  # Add a new obstacle with a small probability
        x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)  # Obstacles spawn from different positions
        y = random.randint(100, SCREEN_HEIGHT - 150)  # Random Y position
        obstacles.append(Obstacle(x, y))

    for obstacle in obstacles[:]:
        obstacle.update()
        if obstacle.x < -100:  # Remove obstacle when it goes off-screen
            obstacles.remove(obstacle)
            score += 1

    # Check for collisions
    for obstacle in obstacles:
        if (player.x < obstacle.x + obstacle.width and
            player.x + player.width > obstacle.x and
            player.y < obstacle.y + obstacle.height and
            player.y + player.height > obstacle.y):
            running = False  # End game if player collides with obstacle

    # Draw everything
    player.draw(screen)
    for obstacle in obstacles:
        obstacle.draw(screen)

    # Draw buttons
    move_up_button.draw(screen)
    move_down_button.draw(screen)
    move_left_button.draw(screen)
    move_right_button.draw(screen)
    jump_button.draw(screen)

    # Draw score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 310))

    # Refresh display
    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame
pygame.quit()
sys.exit()

