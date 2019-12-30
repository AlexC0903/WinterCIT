import pygame
import Source.src as src
import Source.Screen.Menu
import Source.UI.Sprite as Sprite
import Source.UI.Button as Button
import Source.Component.Region as Region

playerImg = pygame.image.load("files/Manny.png")
game_menuImg = pygame.image.load('files/game_menuImg.png')
character_size = (50, 50)



def drawScreen(gameDisplay, player_pos_x, player_pos_y):
    Region.create_region(gameDisplay, src.colors["green"])
    # Player
    Sprite.draw_sprite(gameDisplay, playerImg,
                       player_pos_x, player_pos_y, character_size[0], character_size[1])




def game_loop(gameEvent, gameDisplay, player_pos_x, player_pos_y):
    mode = 0
    gameDisplay.fill(src.colors["white"])
    drawScreen(gameDisplay, player_pos_x, player_pos_y)
    for event in gameEvent:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mode -= 1
    return mode

# # game_menuImg = pygame.transform.scale(game_menuImg, (40, 40))
#

# player_pos_x, player_pos_y = check_boundary(player_pos_x, player_pos_y, character_size)
# def check_boundary(player_pos_x, player_pos_y, character_size):
#     # if player_pos_x > src.display["dwidth"] and player_pos_x > -src.display["dwidth"]:
#     #     player_pos_x -= 1
#     # if player_pos_y > src.display["dheight"] and player_pos_y > -src.display["dheight"]:
#     #     player_pos_y -= 1
#     if(player_pos_x > src.display["dwidth"] - character_size[0]):
#         player_pos_x = src.display["dwidth"] - character_size[0]
#     if player_pos_x < 0:
#         player_pos_x = 0
#     if player_pos_y > src.display["dheight"] - character_size[1]:
#         player_pos_y = src.display["dheight"] - character_size[1]
#     if player_pos_y < 0:
#         player_pos_y = 0
#     return player_pos_x, player_pos_y
