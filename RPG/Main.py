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
    region_id = 0
    display_size_list = [(800, 600), (1200, 900), (1600, 1200)]
    displayChange = 0
    display_size = display_size_list[0]
    gameDisplay = pygame.display.set_mode(
        (display_size[0], display_size[1]))
    player_pos_x = display_size * (1 / 2)
    player_pos_y = display_size * (1 / 2)
    player_health = 100
    startTime = pygame.time.get_ticks()
    seconds = 0
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
            mode += Menu.draw_menuFrame(gameDisplay)
            pygame.mixer.music.stop()
            gameMusic = True
        elif mode == 1:
            if(gameMusic):
                pygame.mixer.music.play(-1)
                gameMusic = False

            pressedKeys = pygame.key.get_pressed()
            # print([pressedKeys[pygame.K_LEFT], pressedKeys[pygame.K_RIGHT],
            # pressedKeys[pygame.K_DOWN], pressedKeys[pygame.K_UP]])
            x_change = 0
            y_change = 0
            if pressedKeys[pygame.K_LEFT] and player_pos_x > 0:
                x_change = -4
            if pressedKeys[pygame.K_RIGHT] and player_pos_x < src.display["dwidth"] - 50:
                x_change = 4
            if pressedKeys[pygame.K_UP] and player_pos_y > 0:
                y_change = -4
            if pressedKeys[pygame.K_DOWN] and player_pos_y < src.display["dheight"] - 50:
                y_change = 4
            player_pos_x += x_change
            player_pos_y += y_change


            modeChange, id, damage = Game_loop.game_loop(gameEvent,
                                        gameDisplay, player_pos_x, player_pos_y, region_id, player_health, display_size)
            mode += modeChange
            region_id = id
            # if damage > 0:
            #     seconds=(pygame.time.get_ticks()-startTime)/1000
            #     if seconds >= 0.8:
            #         player_health -= damage * 5
            #         startTime = pygame.time.get_ticks()
            seconds = 0





        elif mode == 2:
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
