import pygame
 import src
import Game_loop

def drawScreen():
    return src.HUD.draw_spriteButton(src.game_menuImg, src.display["dwidth"] * (59/64), src.display["dheight"] * (1/39), 70, 20)


def drawSettings(gameDisplay):
    mode = 0
    gameDisplay.fill(src.colors["white"])
    src.HUD.draw_menuButton()
    mode += drawScreen()
    return mode
