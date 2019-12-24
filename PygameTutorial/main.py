import pygame
import time


display_width = 800
display_height = 600
x =  (display_width * 0.45)
y = (display_height * 0.8)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)
orange_width = 200
orange_height = 150
# x_change = 0
# y_change = 0
framerate = 60
do_once = False

pygame.init()

orangeImg = pygame.image.load('src/OrangeSprite.jpg')
orangeImg = pygame.transform.scale(orangeImg, (orange_width, orange_height))

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

def orange(x, y):
    gameDisplay.blit(orangeImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text, o_x, o_y):
    largeText = pygame.font.Font('freesansbold.ttf',26)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((o_x + 100),(o_y + -20))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def health(health, x, y):
    message_display(str(health), x, y)


def game_loop(x, y):
    x_change = 0
    y_change = 0
    orange_health = 3
    gameExit = False
    do_once = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            else :
                x_change = 0
                y_change = 0
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:

        x += x_change
        y += y_change
        gameDisplay.fill(white)
        if x >= display_width - orange_width or x <= 0:
            orange_health -= 1
            x = display_width * 0.45
            y = display_height * 0.8
        orange(x, y)
        health(orange_health, x, y)








        pygame.display.update()
        clock.tick(framerate)

game_loop(x, y)
pygame.quit()
quit()
