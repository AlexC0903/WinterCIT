import pygame
from . import src
import Screen.Game_loop

pygame.init()


def draw_menuButton(index):
    mode = 0
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    buttonX = src.display["dwidth"] * (1 / 8)
    buttonY = src.display["dheight"] * ((index * 2 + 1) / 7)
    buttonW = src.display["dwidth"] * (6 / 8)
    buttonH = src.display["dheight"] * (1 / 7)

    pygame.draw.rect(
        src.gameDisplay, src.menu_buttons[index]["color"], (buttonX, buttonY, buttonW, buttonH))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = src.HUD.text_objects(
        src.menu_buttons[index]["content"], smallText)
    textRect.center = ((src.display["dwidth"] * (1 / 2)),
                       src.display["dheight"] * ((index * 4 + 3) / 14))
    src.gameDisplay.blit(textSurf, textRect)
    if buttonX + buttonW > mouse[0] > buttonX and buttonY + buttonH > mouse[1] > buttonY and click[0] == 1:
        if index == 0:
            mode = 1
        elif index == 1:
            mode = 2
        elif index == 2:
            pygame.quit()
            quit()
    return mode


def resize_screen(w, h):
    src.gameDisplay = pygame.display.set_mode((w, h))


def draw_settings():
    is_quit = False
    while not is_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_quit = True
    src.gameDisplay.fill(src.colors["white"])
    draw_menuButton(1, resize_screen(1280, 1080))
    pygame.display.update()
    src.clock.tick(60)


# def menu():
#     is_quit = False
#     while not is_quit:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 is_quit = True
#
#         src.gameDisplay.fill(src.colors["white"])     # background
#         for i in range(3):
#             draw_menuButton(i, Game_loop.game_loop, draw_settings)
#
#         pygame.display.update()
#         src.clock.tick(src.framerate)
