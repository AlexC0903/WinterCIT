import pygame


def draw_sprite(gameDisplay, img, x, y, w, h):
    img = pygame.transform.scale(img, (w, h))
    gameDisplay.blit(img, (x, y))

def check_collision(gameDisplay, sprite1, sprite2):
    x_collide = 0
    y_collide = 0
    if sprite2[0] - sprite1[0] <= sprite1[2] and sprite1[0] < sprite2[0]:
        x_collide = 1
    if sprite2[1] - sprite1[1] <= sprite1[3] and sprite1[1] < sprite2[1]:
        y_collide = 1

    return x_collide * y_collide
