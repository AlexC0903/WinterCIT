import pygame
import Source.src as src
import Source.Screen.Menu
import Source.UI.Sprite as Sprite
import Source.UI.Button as Button

playerImg = pygame.image.load("files/Manny.png")
game_menuImg = pygame.image.load('files/game_menuImg.png')
# game_menuImg = pygame.transform.scale(game_menuImg, (40, 40))


def drawScreen(gameDisplay, player_pos_x, player_pos_y):
    # Player
    Sprite.draw_sprite(gameDisplay, playerImg,
                       player_pos_x, player_pos_y, 50, 50)
    # Quit Button
    return Button.draw_spriteButton(gameDisplay, game_menuImg, src.display["dwidth"] * (59 / 64),
                                    src.display["dheight"] * (1 / 39), 50, 50)
    # The Menu.menu at the end of the line above is a placeholder


def game_loop(gameEvent, gameDisplay, player_pos_x, player_pos_y):


    mode = 0
    gameDisplay.fill(src.colors["white"])
    if drawScreen(gameDisplay, player_pos_x, player_pos_y):
        mode -= 1
    return mode
