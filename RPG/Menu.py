import pygame
import src
import Game_loop

pygame.init()


def text_objects(text, font):
    textSurface = font.render(text, True, src.colors["black"])
    return textSurface, textSurface.get_rect()


def button(index):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    buttonX = src.display["dwidth"] * (1 / 8)
    buttonY = src.display["dheight"] * ((index * 2 + 1) / 7)
    buttonW = src.display["dwidth"] * (6 / 8)
    buttonH = src.display["dheight"] * (1 / 7)

    pygame.draw.rect(src.gameDisplay, src.menu_buttons[index]["color"], (buttonX, buttonY, buttonW, buttonH))
    # Text
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(src.menu_buttons[index]["content"], smallText)
    textRect.center = ((src.display["dwidth"] * (1 / 2)), src.display["dheight"] * ((index * 4 + 3) / 14))
    src.gameDisplay.blit(textSurf, textRect)
    if buttonX + buttonW > mouse[0] > buttonX and buttonY + buttonH > mouse[1] > buttonY and click[0] == 1:
        if index == 0:
            print("before game loop")
            Game_loop.game_loop()
        if index == 2:
            pygame.quit()
            quit()

def menu():
    is_quit = False
    while not is_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_quit = True

        src.gameDisplay.fill(src.colors["white"])     # background
        for i in range(3):
            button(i)

        pygame.display.update()
        src.clock.tick(60)
