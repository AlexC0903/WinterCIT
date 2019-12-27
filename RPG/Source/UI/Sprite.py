import pygame


def draw_sprite(gameDisplay, img, x, y, w, h):
    img = pygame.transform.scale(img, (w, h))
    gameDisplay.blit(img, (x, y))
