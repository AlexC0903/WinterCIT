import pygame
import src
import Menu

pygame.init()

def drawScreen():
    # Quit Button
    src.HUD.draw_spriteButton(src.game_menuImg, src.display["dwidth"] * (59/64), src.display["dheight"] * (1/39), 50, 50, Menu.menu)
    # The Menu.menu at the end of the line above is a placeholder


def game_loop():
    pygame.display.set_caption('The Quest for Cheese')

    dead = False
    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
        src.gameDisplay.fill(src.colors["white"])
        drawScreen()
        pygame.display.update()
        src.clock.tick(src.framerate)

    pygame.quit()
    quit()