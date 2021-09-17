import pygame
import random
import os

pygame.mixer.init()
pygame.mixer.music.load("turn.mp3")
x = pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 250, 0)
black = (0, 0, 0)

# print(x)

gameWindow = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Snake's loop")

bgimg = pygame.image.load("mainbg.jpg")
bgimg = pygame.transform.scale(bgimg, (900, 500)).convert_alpha()
frimg = pygame.image.load("frimg.jpg")
frimg = pygame.transform.scale(frimg, (900, 500)).convert_alpha()
last = pygame.image.load("last.jpg")
last = pygame.transform.scale(last, (310, 480)).convert_alpha()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    game_exit = False
    while not game_exit:
        gameWindow.fill(white)
        gameWindow.blit(frimg, (0, 0))
        text_screen("Welcome To Snake's Loop", white, 190, 150)
        text_screen("Press Space Bar to play", white, 190, 200)
        text_screen("By-Akash Sharma", red, 50, 450)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("bgmusic.mp3")
                    pygame.mixer.music.play(-1)
                    gameloop()
            pygame.display.update()
            clock.tick(30)


def gameloop():
    exit_game = False
    game_over = False

    food_x = random.randint(20, 500 / 2)
    food_y = random.randint(20, 900 / 2)

    score = 0

    velocity_x = 0
    velocity_y = 0

    snake_x = 80
    snake_y = 100

    snake_size = 13
    fps = 15

    snk_list = []
    snk_length = 1

    if (not os.path.exists("hscore.txt")):
        with open("hscore.txt", "w") as f:
            f.write("0")

    with open("hscore.txt", "r") as f:
        hi_score = f.read()

    while not exit_game:

        if game_over == True:
            with open("hscore.txt", "w") as f:
                f.write(str(hi_score))
            gameWindow.fill(white)
            gameWindow.blit(last, (0, 0))
            text_screen("Game over, Press enter to play", red, 160, 180)
            text_screen("HI-Score: " + str(hi_score), red, 330, 250)

            pygame.display.update()
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # pygame.mixer.music.load("turn.mp3")
                        # pygame.mixer.music.play()
                        x = pygame.init()
                        velocity_x = 10
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        # pygame.mixer.music.load("turn.mp3")
                        # pygame.mixer.music.play()
                        velocity_x = - 10
                        velocity_y = 0
                    elif event.key == pygame.K_DOWN:
                        # pygame.mixer.music.load("turn.mp3")
                        # pygame.mixer.music.play()
                        velocity_y = 10
                        velocity_x = 0
                    elif event.key == pygame.K_UP:
                        # pygame.mixer.music.load("turn.mp3")
                        # pygame.mixer.music.play()
                        velocity_y = - 10
                        velocity_x = 0
            snake_y = snake_y + velocity_y
            snake_x = snake_x + velocity_x

            if abs(snake_x - food_x) < 6 and (snake_y - food_y) < 6:
                score += 10
                # print("Score:  ", hi_score)

                food_x = random.randint(20, 500 / 2)
                food_y = random.randint(20, 900 / 2)
                snk_length += 5
                if score > int(hi_score):
                    hi_score = str(score)

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score:  " + str(score) + " Hi-score: " + str(hi_score), red, 4, 4)
            # text_screen("Score:  " + str(score), red, 4, 4)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                x = pygame.init()

            if snake_x < 0 or snake_x > 900 or snake_y < 0 or snake_y > 500:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                x = pygame.init()
                game_over = True

            plot_snake(gameWindow, red, snk_list, snake_size)
            pygame.draw.rect(gameWindow, blue, [food_x, food_y, snake_size, snake_size])
            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()


welcome()
