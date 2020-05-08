import pygame
import random
import os

pygame.mixer.init()
pygame.init()
game_over = False

# COLORS
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue_grey = (204, 229, 255)
width = 900
height = 500
# SCREEN LOOK
window_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game By Akshay")
pygame.display.update()
font1 = pygame.font.SysFont("tlwgtypo", 20)
font2 = pygame.font.SysFont("tlwgtypo", 30)
window_screen.fill(blue_grey)
pygame.display.update()
clock = pygame.time.Clock()

def textscreen(text, color, x, y):
    screen_text = font2.render(text, True, color)
    window_screen.blit(screen_text, [x, y])


def gameover(text, color, x, y):
    screen_text = font1.render(text, True, color)
    window_screen.blit(screen_text, [x, y])


def snake_plot(window_screen, color, snake_list, snake_length):
    for x, y in snake_list:
        pygame.draw.rect(window_screen, color, [x, y, snake_length, snake_length])
 #BACKGROUND IMAGES
bcimg=pygame.image.load("/home/akshay/Downloads/PYTHON/images/snake_bac.jpg")
bcimg=pygame.transform.scale(bcimg,(width,height)).convert_alpha()

bcicon=pygame.image.load("/home/akshay/Downloads/PYTHON/images/snakelogo1.png")
bcicon=pygame.transform.scale(bcicon,(150,160)).convert_alpha()

def menu():
    game_close = False
    while not game_close:
        window_screen.fill(white)
        window_screen.blit(bcimg,(0,0))
        textscreen("Welcome to Snake Game", red, 230, 220)
        textscreen("Press Space To Play the Game", red, 140, 250)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_close=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('/home/akshay/Downloads/PYTHON/audios/button_press.mp3')
                    pygame.mixer.music.play()
                    looping()
        clock.tick(60)


def looping():
    # VARIBLES

    game_over = False
    exit_game = False
    fps = 30
    snake_x = 50
    snake_y = 60
    velocity_x = 0
    velocity_y = 0
    score = 0
    snake_size = 15
    snake_length=1
    snake_list = []
    food_pos_x = random.randint(20, width / 2)
    food_pos_y = random.randint(30, height / 2)
    if(not os.path.exists("highest.txt")):
        with open("highest.txt","w") as f:
            f.write("0")
    with open("highest.txt", "r") as f:
        high = f.read()
    while not exit_game:
        if game_over==True:

            with open("highest.txt", "w") as f:
                f.write(str(score))
            window_screen.fill(white)
            gameover("GAME OVER !! Press Enter To Start New Game",red,200, 200)
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 exit_game = True
              if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_RETURN:
                      pygame.mixer.music.load('/home/akshay/Downloads/PYTHON/audios/button_press.mp3')
                      pygame.mixer.music.play()
                      menu()
        else:
            for event in pygame.event.get():
               if event.type==pygame.QUIT:
                 exit_game=True
                 menu()
               if event.type==pygame.KEYDOWN:
                   if event.key==pygame.K_RIGHT:
                       velocity_x=10
                       velocity_y=0
                   if event.key==pygame.K_LEFT:
                       velocity_x=-10
                       velocity_y=0
                   if event.key == pygame.K_UP:
                       velocity_x = 0
                       velocity_y = -10
                   if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = 10
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            window_screen.fill(blue_grey)
            window_screen.blit(bcicon, (width,height))
            pygame.draw.rect(window_screen, black, [snake_x, snake_y, 10, 10])

            if abs(snake_x-food_pos_x)<=15 and abs(snake_y-food_pos_y)<=15:
                food_pos_x = random.randint(20, width -50)
                food_pos_y = random.randint(30, height -70)
                snake_length+=5
                score=score+10
                pygame.mixer.music.load('/home/akshay/Downloads/PYTHON/audios/apple_eating.mp3')
                pygame.mixer.music.play()
                if score>int(high):
                    high=score
            window_screen.fill(blue_grey)
            window_screen.blit(bcicon, (700, 320))
            pygame.draw.circle(window_screen, red, (food_pos_x, food_pos_y), 10)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            textscreen("Score: "+str(score),red,5,5)
            textscreen("Highest Score: "+str(high),red,550,5)




            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer_music.load("/home/akshay/Downloads/PYTHON/audios/gameover.mp3")
                pygame.mixer_music.play()
            if snake_x<0 or snake_x>width or snake_y<0 or snake_y>height:
                game_over=True
                pygame.mixer.music.load('/home/akshay/Downloads/PYTHON/audios/gameover.mp3')
                pygame.mixer.music.play()

            snake_plot(window_screen,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
menu()