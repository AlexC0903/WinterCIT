import pygame
import Source.UI.Sprite as Sprite
import Source.src as src

def create_portal(gameDisplay, x, y, w, h, player_pos_x, player_pos_y):
    Sprite.draw_sprite(gameDisplay, src.game_menuImg, x, y, w, h)
    if x + w > player_pos_x > x and y + h > player_pos_y > y:
        return True
    return False
