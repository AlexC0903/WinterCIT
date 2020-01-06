import pygame


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()



def draw_text(gameDisplay, font, size, content, x, y, color):
    textStyle = pygame.font.Font(font, size)
    textSurf, textRect = text_objects(content, textStyle, color)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)
