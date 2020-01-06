import pygame
import Source.UI.Text as Text


def draw_Hud(gameDisplay, rectColor, textColor, x, y, w, h, score):
    pygame.draw.rect(
        gameDisplay, rectColor, (x, y, w, h))
    Text.draw_text(gameDisplay, "freesansbold.ttf", 20, str(score), x + w/2, y + h/2, (textColor))
