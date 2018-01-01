import pygame
import random
import time

from pygame.locals import *


# Modyfikatory statyczne

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
yellow = (255,255,0)
white_yellow = 1

display_width = 800
display_height = 600
FPS = 20
block_size = 20
snake_growth = 3
apple_thickness = 20

apple = pygame.image.load_basic('jablko.bmp')
img = pygame.image.load_basic('snakehead3.bmp')
clock = pygame.time.Clock()

pygame.init()
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Kobas Games - Snake')
pygame.mixer.music.load('freefall.mp3')
dzwiek_jablka = pygame.mixer.Sound('apple sound.wav')



pygame.display.update()

def pause():
    pause = True
    #game_display.fill(white)
    message_to_screen('Game Paused', red, -50, 60)
    message_to_screen('Press C to continue or Q to quit.', black, 0, 25)
    pygame.display.update()
    clock.tick(5)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    pause = False


def score_counter(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Score: '+str(score), True, black)
    game_display.blit(text, (0,0))

def snake(block_size, snake_list, snake_head, direction):

    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    elif direction == 'left':
        head = pygame.transform.rotate(img, 90)
    elif direction == 'up':
        head = pygame.transform.rotate(img, 0)
    elif direction == 'down':
        head = pygame.transform.rotate(img, 180)

    game_display.blit(head, (snake_head[0], snake_head[1]))
    for XY in snake_list[:-1]:
        pygame.draw.rect(game_display, green, (XY[0],XY[1], block_size, block_size))



# Centrowanie tekstu

def message_to_screen(msg,color, y_displace = 0, size = 25):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, color)
    rect = screen_text.get_rect()
    rect.center = display_width/2, display_height/2 + y_displace
    game_display.blit(screen_text, rect)


def game_into():
    clock.tick(1)
    game_display.fill((0,128,128))
    intro = True
    atm = time.time()
    pygame.mixer.music.play(-1)
    while intro:
        global white_yellow

        if time.time() - atm >= 0.3:
            white_yellow += 1
            atm = time.time()

        if white_yellow % 2 == 0:
            message_to_screen('Welcome to:', yellow, -150, 100)
            message_to_screen('Kobas Games: Snake!', yellow, -50, 100)

        else:
            message_to_screen('Welcome to:', white, -150, 100)
            message_to_screen('Kobas Games: Snake!', white, -50, 100)

        message_to_screen('Collect as many apples as you can!', white, 20, 30)
        message_to_screen('Press C to play, P to pause or Q to quit', red, 50, 30)
        message_to_screen('Caution: "Kobas Games - Snake" is a licensed Kobas Games Torun product.',
                          black,
                          80,
                          30)
        message_to_screen('Kobas Games Torun is a part of Kobas Games Poland GMBH. ',
                          black,
                          110,
                          30)
        message_to_screen('All rights reserved. ', black, 140, 30)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


def game_loop():

# Modyfikatory dynamiczne
    direction = 'up'
    lead_x_change = 0
    lead_y_change = 0

    lead_x = display_width / 2
    lead_y = display_height / 2
    snake_list = []
    snake_length = 1
    game_over = False
    game_exit = False
    score = 0
    appleX = random.randrange(0, display_width-block_size, block_size)
    appleY = random.randrange(0, display_height-block_size, block_size)
    pygame.mixer.music.stop()
    while not game_exit:
        if game_over == True:
            message_to_screen('Game over!',
                              red, -30,
                              size = 100)
            message_to_screen('Press C to play again or Q to quit',
                              green,
                              20,
                              35)

            pygame.display.update()
        while game_over == True:



            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                game_over = False
            if event.type == pygame.KEYDOWN:
                lead_y_change = 0
                lead_x_change = 0
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    direction = 'right'
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    direction = 'up'
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    direction = 'down'
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x <0 or lead_y >= display_height or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change


#Rysowanie oraz zjadanie jabłka i przyrost snaka

        if lead_x >= appleX and lead_x <= appleX + apple_thickness - block_size and lead_y >= appleY and lead_y <= appleY + apple_thickness - block_size:
            appleX = random.randrange(0, display_width - block_size, block_size)
            appleY = random.randrange(0, display_height - block_size, block_size)
            snake_length += snake_growth
            score += 1
            pygame.mixer.Sound.play(dzwiek_jablka)
        game_display.fill(white)
        game_display.blit(apple, (appleX,appleY))
        score_counter(score)

        #pygame.draw.rect(game_display,red,(appleX,appleY,apple_thickness,apple_thickness))
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        snake(block_size, snake_list, snake_head, direction)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                game_over = True




        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


game_into()
game_loop()