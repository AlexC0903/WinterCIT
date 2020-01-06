# Runs First
import pygame

import Source.src as src
import Source.Screen.Menu as Menu
import Source.Screen.Game_loop as Game_loop
import Source.Screen.Settings as Settings
# from Screen import Game_loop
# from Screen import Settings

pygame.init()
pygame.display.set_caption('The Quest for Cheese')


framerate = 120
clock = pygame.time.Clock()


def main():
    is_quit = False
    mode = 0
    gameMusic = True
    display_size_list = [(800, 600), (1200, 900), (1600, 1200)]
    displayChange = 0
    display_size = display_size_list[0]
    gameDisplay = pygame.display.set_mode(
        (display_size[0], display_size[1]))
    pygame.mixer.init()

    mainTheme = "files/music.ogg"  # mp3 is not suitable in pygame
    pygame.mixer.music.load(mainTheme)

    while not is_quit:
        if(displayChange != 0 and mode == 0) :
            display_size = display_size_list[displayChange -1]
            gameDisplay = pygame.display.set_mode(
                (display_size[0], display_size[1]))
            displayChange = 0
        gameEvent = pygame.event.get()
        for event in gameEvent:
            if event.type == pygame.QUIT:
                is_quit = True

        gameDisplay.fill(src.colors["white"])     # background
        if mode == 0:
            pygame.mouse.set_visible(True)
            mode += Menu.draw_menuFrame(gameDisplay)
            pygame.mixer.music.stop()
            gameMusic = True
        elif mode == 1:
            pygame.mouse.set_visible(False)
            if(gameMusic):
                pygame.mixer.music.play(-1)
                gameMusic = False

            modeChange = Game_loop.game_loop(gameEvent,
                                        gameDisplay,  display_size)
            mode += modeChange

        elif mode == 2:
            pygame.mouse.set_visible(True)
            modeChange, dChange = Settings.drawSettings(gameDisplay, gameEvent)
            if (displayChange and dChange) :
                displayChange = dChange
            else :
                displayChange += dChange
            mode += modeChange
        else:
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(framerate)


main()
# Menu.menu()
pygame.quit()
quit()
