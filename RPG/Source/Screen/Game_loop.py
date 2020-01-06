import pygame
import Source.src as src
import Source.Screen.Menu
import Source.UI.Sprite as Sprite
import Source.UI.Button as Button
import Source.Component.Region as Region
import Source.UI.Text as Text
import Source.Component.Hud as Hud

playerImg = pygame.image.load("files/Manny.png")
game_menuImg = pygame.image.load('files/game_menuImg.png')
character_size = (50, 50)

player_info = {"health": 100, "score": 0, "x": 1 / 2,
               "y": 1 / 2, "w": 1 / 16, "h": 1 / 12, "region": 0}
danger_zone = [[0, -20, 800, 20], [0, 600, 800, 20], [-20, 0, 20, 600], [800, 0, 20, 600]]

def player_move(player_info, display_size):
    x = player_info["x"]
    y = player_info["y"]
    w = player_info["w"]
    h = player_info["h"]
    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_LEFT]:
        x -= 1 / 200
    if pressedKeys[pygame.K_RIGHT]:
        x += 1 / 200
    if pressedKeys[pygame.K_UP]:
        y -= 1 / 200
    if pressedKeys[pygame.K_DOWN]:
        y += 1 / 200
    canMove = 1
    for blocks in danger_zone:
        if Sprite.check_collision([x * display_size[0], y * display_size[1], w * display_size[0], h * display_size[1]], [blocks[0], blocks[1], blocks[2], blocks[3]]):
            canMove *= 0
    if canMove:
        if pressedKeys[pygame.K_LEFT]:
            player_info["x"] = x
        if pressedKeys[pygame.K_RIGHT]:
            player_info["x"] = x
        if pressedKeys[pygame.K_UP]:
            player_info["y"] = y
        if pressedKeys[pygame.K_DOWN]:
            player_info["y"] = y


def drawScreen(gameDisplay, player_info, display_size):
    x = player_info["x"] * display_size[0]
    y = player_info["y"] * display_size[1]
    w = player_info["w"] * display_size[0]
    h = player_info["h"] * display_size[1]
    id = Region.create_region(
        gameDisplay, player_info["region"], x, y, player_info)
    # Player
    Sprite.draw_sprite(gameDisplay, playerImg,
                       x, y, int(w), int(h))
    Text.draw_text(gameDisplay, "freesansbold.ttf", 20, str(
        player_info["health"]), x, y, (30, 50, 69))
    Hud.draw_Hud(gameDisplay, (255, 0, 255), 300,
                 300, 60, 60, player_info["score"])
    return id


def game_loop(gameEvent, gameDisplay,  display_size):
    mode = 0
    gameDisplay.fill(src.colors["white"])
    player_move(player_info, display_size)
    player_info["region"] = drawScreen(gameDisplay, player_info, display_size)
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
