import pygame
import src
import Menu



def drawScreen():
    # Quit Button
    return src.HUD.draw_spriteButton(src.game_menuImg, src.display["dwidth"] * (59/64), src.display["dheight"] * (1/39), 50, 50)
    # The Menu.menu at the end of the line above is a placeholder


def game_loop(gameEvent,gameDisplay):
    mode = 0
    gameDisplay.fill(src.colors["white"])
    mode += drawScreen()
    return mode
