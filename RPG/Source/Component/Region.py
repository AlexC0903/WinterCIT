import pygame
import Source.src as src

def create_region(gameDisplay, color):
    pygame.draw.rect(
        gameDisplay, color, (0, 0, src.display["dwidth"], src.display["dheight"]))
