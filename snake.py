import pygame
import time
import random

pygame.init()

width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block_size = 20

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 50)


def our_snake(snake_list, start_time, apples_eaten):
    elapsed_time = int(time.time() - start_time)
    timer_text = font_style.render("Time: " + str(elapsed_time), True, (255, 255, 255))
    window.blit(timer_text, (10, 10))
    apples_text = font_style.render("Apples: " + str(apples_eaten), True, (255, 255, 255))
    window.blit(apples_text, (width - 120, 10))
    for x in snake_list:
        pygame.draw.rect(window, (0, 0, 0), [x[0], x[1], snake_block_size, snake_block_size])


def message(msg, color, offset=0):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(width / 2, height / 2 + offset))
    window.blit(mesg, text_rect)


def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0

    difficulty = None
    speed_mapping = {
        "Easy": 10,
        "Medium": 25,
        "Hard": 50
    }

    start_time = time.time()
    apples_eaten = 0

    background_image = pygame.image.load("C://Users//User//Downloads//background.jpg")
    background_image = pygame.transform.scale(background_image, (width, height))

    while not game_over:
        while not game_close:
            if difficulty is None:
                window.blit(background_image, (0, 0))
                message("Choose difficulty:", (255, 255, 255), offset=-50)
                message("1 - Easy", (255, 255, 255), offset=0)
                message("2 - Medium", (255, 255, 255), offset=30)
                message("3 - Hard", (255, 255, 255), offset=60)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            difficulty = "Easy"
                        elif event.key == pygame.K_2:
                            difficulty = "Medium"
                        elif event.key == pygame.K_3:
                            difficulty = "Hard"

                clock.tick(5)
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block_size
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block_size
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block_size
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block_size
                            x1_change = 0

                if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                window.blit(background_image, (0, 0))
                pygame.draw.rect(window, (123, 255, 123), [foodx, foody, snake_block_size, snake_block_size])
                snake_head = []
                snake_head.append(x1)
                snake_head.append(y1)
                snake_list.append(snake_head)
                if len(snake_list) > length_of_snake:
                    del snake_list[0]

                for x in snake_list[:-1]:
                    if x == snake_head:
                        game_close = True

                our_snake(snake_list, start_time, apples_eaten)

                pygame.display.update()

                if abs(x1 - foodx) < snake_block_size and abs(y1 - foody) < snake_block_size:
                    foodx = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
                    foody = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0
                    length_of_snake += 1
                    apples_eaten += 1

                clock.tick(speed_mapping[difficulty])

        window.blit(background_image, (0, 0))
        message("Game Over! Press Q-Quit or С-Play Again", (255, 255, 255), offset=-50)
        message("Score: " + str(length_of_snake - 1), (255, 255, 255), offset=50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game_loop()

    pygame.quit()


game_loop()
