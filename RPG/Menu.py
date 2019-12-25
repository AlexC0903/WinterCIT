import pygame
import src
import Game_loop

pygame.init()

def menu():
    is_quit = False
    while not is_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_quit = True

        src.gameDisplay.fill(src.colors["white"])     # background
        for i in range(3):
            src.HUD.draw_menuButton(i, Game_loop.game_loop)

        pygame.display.update()
        src.clock.tick(60)
