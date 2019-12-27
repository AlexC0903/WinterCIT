import pygame
import Source.UI.Button as Button
import Source.UI.Text as Text
# import sys
# print(sys.path)
# sys.path.insert(0, sys.path[0].split("\Screen")[0])
# print(sys.path)

import Source.src as src
import Source.Screen.Game_loop

menu_buttons = [{"content": "Go!", "color": src.colors["green"]}, {
    "content": "Settings", "color": src.colors["grey"]}, {"content": "Quit", "color": src.colors["red"]}]


def make_buttonRatio(index):
    ratio = {"x_ratio": 1 / 8,
             "y_ratio": (index * 2 + 1) / 7, "w_ratio": 6 / 8, "h_ratio": 1 / 7}
    return ratio


def make_textRatio(index):
    ratio = {"x_ratio": 1 / 2,
             "y_ratio": (index * 4 + 3) / 14}
    return ratio


def draw_menuFrame(gameDisplay):
    mode = 0
    for i in range(3):
        if (Button.draw_button(
                gameDisplay, src.display["dwidth"], src.display["dheight"], make_buttonRatio(i), menu_buttons[i]["color"])):
            mode = i + 1
        Text.draw_text(gameDisplay, "freesansbold.ttf", 20,
                       menu_buttons[i]["content"], src.display["dwidth"], src.display["dheight"], make_textRatio(i),  src.colors["black"])
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

# def draw_menuButton(index):
#     mode = 0
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     buttonX = src.display["dwidth"] * (1 / 8)
#     buttonY = src.display["dheight"] * ((index * 2 + 1) / 7)
#     buttonW = src.display["dwidth"] * (6 / 8)
#     buttonH = src.display["dheight"] * (1 / 7)
#
#     pygame.draw.rect(
#         src.gameDisplay, src.menu_buttons[index]["color"], (buttonX, buttonY, buttonW, buttonH))
#
#     smallText = pygame.font.Font("freesansbold.ttf", 20)
#     textSurf, textRect = src.HUD.text_objects(
#         src.menu_buttons[index]["content"], smallText)
#     textRect.center = ((src.display["dwidth"] * (1 / 2)),
#                        src.display["dheight"] * ((index * 4 + 3) / 14))
#     src.gameDisplay.blit(textSurf, textRect)
#     if buttonX + buttonW > mouse[0] > buttonX and buttonY + buttonH > mouse[1] > buttonY and click[0] == 1:
#         if index == 0:
#             mode = 1
#         elif index == 1:
#             mode = 2
#         elif index == 2:
#             pygame.quit()
#             quit()
#     return mode

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
