import pygame
import time
import random
# initialize pygame
pygame.init()

#Screen size
width = 600
height = 400
screen = pygame.display.set_model((width,height))
pygame.display.set_caption("Snake Game")

#colors
white = (255,255,255)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)


# Snake Settings
snake_block = 10
snake_speed = 15
clock = pygame.time.clock()
font_style = pygame.font.SysFont("bahnschrif",25)
score_font = pygame.font.SysFont("comicsansms",35)

def message(msg,color):
    game_over = False
    game_close = False

    # Snake starting position
    x1 = width /2
    y2 = height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0,width - snake_block) /10.0)*10.0
    foody = round(random.randrange(0,height - snake_block) /10.0)*10.0

    while not game_over:

        while game_close:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOM:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   x1_change = -snake_block
                   y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key ==pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen,green,[foodx,foody,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        for block


