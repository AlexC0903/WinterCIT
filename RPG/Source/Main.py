# Runs First
import pygame
import Screen.src
import Screen.Menu
import Screen.Game_loop
import Screen.Settings
# from Screen import Game_loop
# from Screen import Settings

pygame.init()
pygame.display.set_caption('The Quest for Cheese')

framerate = 60
gameDisplay = pygame.display.set_mode(
    (src.display["dwidth"], src.display["dheight"]))
clock = pygame.time.Clock()



def main():
    is_quit = False
    mode = 0

    while not is_quit:
        gameEvent = pygame.event.get()
        for event in gameEvent:
            if event.type == pygame.QUIT:
                is_quit = True

        gameDisplay.fill(src.colors["white"])     # background
        if mode==0:
            for i in range(3):
                mode += Menu.draw_menuButton(i)
        elif mode==1:
            mode += Game_loop.game_loop(gameEvent, gameDisplay)
        elif mode==2:
            mode += Settings.drawSettings(gameDisplay)



        print(mode)
        pygame.display.update()
        clock.tick(framerate)


main()
# Menu.menu()
pygame.quit()
quit()
