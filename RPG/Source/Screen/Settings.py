import pygame
import Source.src as src
import Source.Screen.Game_loop
import Source.UI.Button as Button
applyButtonRatio = {"x_ratio": 0,
                    "y_ratio": 6 / 7, "w_ratio": 1 / 8, "h_ratio": 1 / 7}


def make_buttonRatio(index):
    ratio = {"x_ratio": 1 / 8,
             "y_ratio": (index * 2 + 1) / 7, "w_ratio": 6 / 8, "h_ratio": 1 / 7}
    return ratio


def make_textRatio(index):
    ratio = {"x_ratio": 1 / 2,
             "y_ratio": (index * 4 + 3) / 14}
    return ratio


def drawScreen(gameDisplay):
    modeChange = 0
    displayChange = 0
    for i in range(3):
        Button.draw_button(gameDisplay, src.display["dwidth"], src.display["dheight"], make_buttonRatio(
            i), src.colors["red"])
        displayChange = i
    if Button.draw_button(gameDisplay, src.display["dwidth"], src.display["dheight"], applyButtonRatio, src.colors["green"]):
        modeChange = -2
    return modeChange, displayChange


def draw_settingFrame(gameDisplay, mode):
    print("")


def drawSettings(gameDisplay):
    gameDisplay.fill(src.colors["white"])
    return drawScreen(gameDisplay)
