import pygame
import Source.src as src
import Source.Screen.Menu
import Source.UI.Sprite as Sprite
import Source.UI.Button as Button
import Source.Component.Region as Region
import Source.UI.Text as Text

playerImg = pygame.image.load("files/Manny.png")
game_menuImg = pygame.image.load('files/game_menuImg.png')
character_size = (50, 50)

player_info = {"health" : 100, "x" : 0, "w" : 50, "h": 50}




def drawScreen(gameDisplay, player_pos_x, player_pos_y, player_health, region_id):
    id, damage = Region.create_region(gameDisplay, region_id, player_pos_x, player_pos_y)
    if(damage) :
        player_health["health"] -= 5
    # Player
    Sprite.draw_sprite(gameDisplay, playerImg,
                       player_pos_x, player_pos_y, character_size[0], character_size[1])
    Text.draw_text(gameDisplay, "freesansbold.ttf", 20, str(player_health["health"]), player_pos_x, player_pos_y, {"x_ratio" : 1, "y_ratio": 1}, (30,50,69))

    return id, damage

def game_loop(gameEvent, gameDisplay, player_pos_x, player_pos_y, region_id, player_health, display_size):
    mode = 0
    gameDisplay.fill(src.colors["white"])
    id, damage = drawScreen(gameDisplay, player_pos_x, player_pos_y, player_info, region_id)
    for event in gameEvent:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mode -= 1
    return mode, id, damage

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
