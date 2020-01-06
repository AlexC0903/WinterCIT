import pygame


# Dictionaries
display = {"dwidth": 800, "dheight": 600}
colors = {"red" : (255,0,0), "white": (255,255,255), "black": (0, 0, 0), "green": (44, 255, 20), "grey": (92, 110, 90), "brown": (210,180,140)}

# Images
game_menuImg = pygame.image.load('files/game_menuImg.png')
game_menuImg = pygame.transform.scale(game_menuImg, (40, 40))
# Settings
framerate = 120
gameDisplay = pygame.display.set_mode((display["dwidth"], display["dheight"]))
clock = pygame.time.Clock()

# Classes
class HUD():


    def draw_spriteButton(img, x, y, w, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        draw_sprite(img, x, y, w, h)
        if x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            return -1
        return 0
# Functions
def draw_sprite(img, x, y, w, h):
    gameDisplay.fill(colors["white"])
    img = pygame.transform.scale(img, (w, h))
    gameDisplay.blit(img, (x, y))
