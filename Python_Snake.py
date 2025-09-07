import pygame
import random
pygame.init()


# settings
speed = 1                       # movement per frame (must be int >=1)
safe_head_offset = 20/speed*2   # number of the first body parts ignored for self collision detection, should be: 20/speed*2
growth_rate = 3                 # body segments added per food eaten
frame_rate = 120                # FPS - frames per second
window_width = 800
window_height = 600


# setup
clock = pygame.time.Clock()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("SNAKE 😎😎😏")

class Player:
    def __init__(self):
        self.head = pygame.Rect(window_width/2, window_height/2, 20, 20)
        self.head_color = (100, 100, 255)
        self.body = []

snake = Player()
food = pygame.Rect(window_width * 0.8, window_height/2, 10, 10)
food_color = (255, 150, 0)

move_direction = None

def end_screen():
    font = pygame.Font(None, 60)
    text = font.render(f"Snake died :(\n\nFinal length: {len(snake.body)//(20//speed)}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (window_width/2, window_height/2)
    screen.blit(text, text_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snake.body = []
                    snake.head.topleft = (window_width/2, window_height/2)
                    global move_direction
                    move_direction = None
                    return


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if move_direction != "down": move_direction = "up"
            elif event.key == pygame.K_DOWN:
                if move_direction != "up": move_direction = "down"
            elif event.key == pygame.K_LEFT:
                if move_direction != "right": move_direction = "left"
            elif event.key == pygame.K_RIGHT:
                if move_direction != "left": move_direction = "right"
    
    last_pos = snake.head.topleft
    x, y = snake.head.topleft
    if move_direction == "up":
        snake.head.topleft = (x, y - speed)
    elif move_direction == "down":
        snake.head.topleft = (x, y + speed)
    elif move_direction == "left":
        snake.head.topleft = (x - speed, y)
    elif move_direction == "right":
        snake.head.topleft = (x + speed, y)
    
    x, y = snake.head.topleft
    if x < 0 or x > window_width - 20 or y < 0 or y > window_height - 20:
        end_screen()
    for i in range(int(safe_head_offset), len(snake.body)):
        if snake.head.colliderect(snake.body[i]):
            end_screen()
            break
    
    if snake.head.colliderect(food):
        while True:
            random_x = random.randint(0, window_width - 10)
            random_y = random.randint(0, window_height - 10)
            food.topleft = (random_x, random_y)
            if any(food.colliderect(part) for part in snake.body) == False:
                break
        for i in range(int(20/speed * growth_rate)):
            snake.body.append(pygame.Rect(-30, -30, 20, 20))
    
    if snake.body:
        last = snake.body.pop()
        last.topleft = last_pos
        snake.body.insert(0, last)
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, snake.head_color, snake.head)
    pygame.draw.rect(screen, food_color, food)
    for part in snake.body:
        pygame.draw.rect(screen, snake.head_color, part)
    pygame.display.flip()

    clock.tick(frame_rate)