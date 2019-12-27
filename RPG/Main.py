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

framerate = 60
gameDisplay = pygame.display.set_mode(
    (src.display["dwidth"], src.display["dheight"]))
clock = pygame.time.Clock()



def main():
    is_quit = False
    mode = 0
    gameMusic = True
    player_pos_x=src.display["dwidth"] * (1 / 2)
    player_pos_y=src.display["dheight"] * (1 / 2)

    pygame.mixer.init()

    mainTheme = "files/music.ogg" # mp3 is not suitable in pygame
    pygame.mixer.music.load(mainTheme)


    while not is_quit:
        gameEvent = pygame.event.get()
        for event in gameEvent:
            if event.type == pygame.QUIT:
                is_quit = True

        gameDisplay.fill(src.colors["white"])     # background
        if mode==0:
            mode += Menu.draw_menuFrame(gameDisplay)
            pygame.mixer.music.stop()
            gameMusic = True
        elif mode==1:
            if(gameMusic):
                pygame.mixer.music.play(-1)
                gameMusic = False
            for event in gameEvent:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_pos_x += -5
                    elif event.key == pygame.K_RIGHT:
                        player_pos_x += +5
                    elif event.key == pygame.K_UP:
                        player_pos_y += -5
                    elif event.key == pygame.K_DOWN:
                        player_pos_y += +5

            mode += Game_loop.game_loop(gameEvent, gameDisplay, player_pos_x, player_pos_y)
        elif mode==2:
            mode += Settings.drawSettings(gameDisplay)



        pygame.display.update()
        clock.tick(framerate)


main()
# Menu.menu()
pygame.quit()
quit()