import pygame
import Source.src as src
import Source.Screen.Game_loop

def drawScreen():
    return src.HUD.draw_spriteButton(src.game_menuImg, src.display["dwidth"] * (59/64), src.display["dheight"] * (1/39), 70, 20)

def draw_settingFrame(gameDisplay, mode):
    print("")



def drawSettings(gameDisplay):
    mode = 0
    gameDisplay.fill(src.colors["white"])
    src.HUD.draw_menuButton()
    mode += drawScreen()
    return mode
