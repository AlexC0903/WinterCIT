import pygame


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()



def draw_text(gameDisplay, font, size, content, ref_width, ref_height, ratio, color):
    textStyle = pygame.font.Font(font, size)
    textSurf, textRect = text_objects(content, textStyle, color)
    textRect.center = ((ref_width * ratio["x_ratio"]),
                   ref_height * ratio["y_ratio"])
    gameDisplay.blit(textSurf, textRect)
