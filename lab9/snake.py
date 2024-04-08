import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 10
initial_snake_speed = 15
speed_increment = 2
speed_level_increment = 4

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score, level):
    value = score_font.render("Score: " + str(score) + "  Level: " + str(level), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    level = 1
    score = 0
    snake_speed = initial_snake_speed

    #variables for food generation
    food_types = ['apple', 'banana', 'cherry']  #add more food types as needed
    food_weights = {'apple': 6, 'banana': 3, 'cherry': 1}  #adjust weights as needed
    food_timer = 5000  #time in milliseconds for food to disappear (5 seconds in this case)
    food_timer_start = pygame.time.get_ticks()  #get the current time in milliseconds

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        #generate food randomly based on weights
        if random.randint(1, sum(food_weights.values())) <= food_weights['apple']:
            food_type = 'apple'
        elif random.randint(1, sum(food_weights.values())) <= food_weights['banana']:
            food_type = 'banana'
        else:
            food_type = 'cherry'

        #draw food on screen
        if food_type == 'apple':
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        elif food_type == 'banana':
            pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        elif food_type == 'cherry':
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        #check if food timer has expired
        if pygame.time.get_ticks() - food_timer_start >= food_timer:
            #reset food position
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            #reset food timer
            food_timer_start = pygame.time.get_ticks()

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(score, level)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1

            #check if level should be increased
            if score % speed_level_increment == 0:
                level += 1
                snake_speed += speed_increment

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
