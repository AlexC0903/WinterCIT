import pygame
import Source.UI.Sprite as Sprite
import Source.src as src

def create_portal(gameDisplay, x, y, w, h):
    Sprite.draw_sprite(gameDisplay, src.game_menuImg, x, y, w, h)
