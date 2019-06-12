import pygame
import random
import os

pygame.mixer.init()

#initialisation
pygame.init()



# Colors
white=(255,255,255)
red = (255,0, 0)
blue = (30, 136, 229)
magenta = (136,24,91)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
#background Image 
bg=pygame.image.load('assets/images/Background.png')
bgimg=pygame.transform.scale(bg,(screen_width,screen_height)).convert_alpha()

#Welcome Image
bg1=pygame.image.load('assets/images/welcome.png')
bgimg1=pygame.transform.scale(bg1,(screen_width,screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snakes")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game=False
    pygame.mixer.music.load('assets/sounds/back.mp3')
    pygame.mixer.music.play()
    while not exit_game:
        gameWindow.fill((233,220,229))
        gameWindow.blit(bgimg1,(0,0))
        #text_screen("Welcome to Snakes Game",black,230,230)
        #text_screen("Press Space To play",black,260,270)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
                
        pygame.display.update()
        clock.tick(60)
         

    # Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt","w") as f:
            f.write("0")
    with open("high_score.txt", "r") as f:
        high_score = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
            gameWindow.fill(white)
            text_screen("Your Snake is dead...Noob!!!", red, 150, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                pygame.mixer.music.load('assets/sounds/point.wav')
                pygame.mixer.music.play()
                
                if score>int(high_score):
                    high_score = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score: " + str(score) + "  High score: "+str(high_score), blue, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            #if the snake eats himself
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('assets/sounds/die.wav')
                #pygame.mixer.music.play()
                pygame.mixer.music.load('assets/sounds/hit.wav')
                pygame.mixer.music.play()
                

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('assets/sounds/die.wav')
                #pygame.mixer.music.play()
                pygame.mixer.music.load('assets/sounds/hit.wav')
                pygame.mixer.music.play()
                
            plot_snake(gameWindow, magenta, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
#gameloop()

