import pygame
import Source.UI.Text as Text


def draw_Hud(gameDisplay, color, x, y, w, h, score):
    pygame.draw.rect(
        gameDisplay, color, (x, y, w, h))
    Text.draw_text(gameDisplay, "freesansbold.ttf", 20, str(score), x + w/2, y + h/2, (255,255,255))
