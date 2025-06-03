import time
import random
import pygame

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake settings
block_size = 20
speed = 50

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color, position):
    text = font.render(msg, True, color)
    window.blit(text, position)

def game_loop():
    game_over = False
    game_close = False

    x, y = width / 2, height / 2
    x_change, y_change = 0, 0

    snake = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10

    while not game_over:
        while game_close:
            window.fill(black)
            message("Game Over! Press C to Play Again or Q to Quit", red, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change * 0.5  # Smooth movement factor
        y += y_change * 0.5
        window.fill(black)

        pygame.draw.circle(window, red, (food_x + 5, food_y + 5), block_size // 2)

        snake.append([x, y])
        if len(snake) > length_of_snake:
            del snake[0]

        for segment in snake[:-1]:
            if segment == [x, y]:
                game_close = True

        for part in snake:
            pygame.draw.circle(window, green, (int(part[0]) + 5, int(part[1]) + 5), block_size // 2)

        pygame.display.update()

        if abs(x - food_x) < block_size and abs(y - food_y) < block_size:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10
            length_of_snake += 1

        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()