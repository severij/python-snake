import random
import pygame
import pygame.freetype

FPS = 30
BG_COLOR = (0, 0, 0)
FG_COLOR = (255, 255, 255)
SNAKE_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)
snake = [[300, 300], [290, 300], [280, 300]]
apple = [0, 0]
x_dir = 10
y_dir = 0
score = 0

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill(BG_COLOR)
clock = pygame.time.Clock()
borders = pygame.draw.rect(screen, FG_COLOR, (10, 10, 620, 380))
game_area = pygame.Surface((600, 360))
score_area = pygame.Surface((620, 100)) 
font = pygame.freetype.Font("homespun.ttf", 100) 


def create_apple(snake):
    overlap = True
    while overlap:
        apple_x = 10*random.randint(0, 59)
        apple_y = 10*random.randint(0, 35)
        for part in snake:
            if apple_x == part[0] and apple_y == part[1]:
                overlap = True
                break
            else:
                overlap = False
    return [apple_x, apple_y]


def update_snake(snake, move_x, move_y):
    temp = snake[0].copy()
    snake[0][0] += x_dir
    snake[0][1] += y_dir
    for i in range(1, len(snake)):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            quit()
        for i in range(1, len(snake)):
            temp2 = snake[i].copy()
            snake[i] = temp.copy()
            temp = temp2.copy()
        return snake


def draw_snake(surface, snake, color):
    for part in snake:
        pygame.draw.rect(surface, color, (part[0], part[1], 10, 10))

apple = create_apple(snake)
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_dir != 10:
                x_dir = -10
                y_dir = 0
            elif event.key == pygame.K_RIGHT and x_dir != -10:
                x_dir = 10
                y_dir = 0
            elif event.key == pygame.K_UP and y_dir != 10:
                x_dir = 0
                y_dir = -10
            elif event.key == pygame.K_DOWN and y_dir != -10:
                x_dir = 0
                y_dir = 10
    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        snake.append([0, 0])
        apple = create_apple(snake)
        score += 1
        screen.blit(score_area, (20, 400))
    game_area.fill(BG_COLOR)
    pygame.draw.rect(game_area, APPLE_COLOR, (apple[0], apple[1], 10, 10))
    snake = update_snake(snake, x_dir, y_dir)
    if snake[0][0] >= 600 or snake[0][0] < 0 or \
            snake[0][1] >= 360 or snake[0][1] < 0:
                quit()
    draw_snake(game_area, snake, SNAKE_COLOR)
    screen.blit(game_area, (20, 20))
    font.render_to(screen, (10, 400), "Score: " + str(score), FG_COLOR)
    clock.tick(FPS)
    pygame.display.update()
