import pygame
import Game_loop

# Dictionaries
display = {"dwidth": 800, "dheight": 600}
colors = {"red" : (255,0,0), "white": (255,255,255), "black": (0, 0, 0), "green": (44, 255, 20), "grey": (92, 110, 90)}
menu_buttons = [{"content": "Go!", "color": colors["green"]}, {"content": "Settings", "color": colors["grey"]}, {"content": "Quit", "color": colors["red"]}]
# Images
game_menuImg = pygame.image.load('src/game_menuImg.png')
game_menuImg = pygame.transform.scale(game_menuImg, (40, 40))
# Settings
framerate = 60
gameDisplay = pygame.display.set_mode((display["dwidth"], display["dheight"]))
clock = pygame.time.Clock()

# Classes
class HUD():
    def text_objects(text, font):
        textSurface = font.render(text, True, colors["black"])
        return textSurface, textSurface.get_rect()

    def draw_spriteButton(img, x, y, w, h, action1=None, action2=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        draw_sprite(img, x, y, w, h)
        if x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            if action1!=None and action2!=None and click[0] == 1:
                action1()
                action2()
            elif action1!=None and click[0] == 1:
                action1()

    def draw_menuButton(index, action1=None, action2=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        buttonX = display["dwidth"] * (1 / 8)
        buttonY = display["dheight"] * ((index * 2 + 1) / 7)
        buttonW = display["dwidth"] * (6 / 8)
        buttonH = display["dheight"] * (1 / 7)

        pygame.draw.rect(gameDisplay, menu_buttons[index]["color"], (buttonX, buttonY, buttonW, buttonH))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = HUD.text_objects(menu_buttons[index]["content"], smallText)
        textRect.center = ((display["dwidth"] * (1 / 2)), display["dheight"] * ((index * 4 + 3) / 14))
        gameDisplay.blit(textSurf, textRect)
        if buttonX + buttonW > mouse[0] > buttonX and buttonY + buttonH > mouse[1] > buttonY and click[0] == 1:
            if index == 0 and action1!=None:
                action1()
            elif index == 1 and action2!=None:
                action2()
            elif index == 2:
                pygame.quit()
                quit()

# Functions
def draw_sprite(img, x, y, w, h):
    gameDisplay.fill(colors["white"])
    img = pygame.transform.scale(img, (w, h))
    gameDisplay.blit(img, (x, y))


