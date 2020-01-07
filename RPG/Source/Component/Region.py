import pygame
import Source.src as src
import Source.Component.Portal as Portal
import Source.UI.Sprite as Sprite
import Source.UI.Text as Text


def static(x, y):
    return x, y


def moveCheese(x, y):
    return x + 1, y + 1


def moveMouse(x, y):
    return x + 1, y + 1


cheese = pygame.image.load("files/cheese.png")
mouse = pygame.image.load("files/mouse.png")
npc = pygame.image.load("files/npc.png")
rsk = pygame.image.load("files/redShovelknight.png")
region = [(src.colors["green"],  [(src.display["dwidth"] - 50, 0, 1), (0, src.display["dheight"] - 50, 2)],
           [
           [cheese, 0, 0, 30, 30, static, 1, None, True, []],
           [cheese, 70, 150, 30, 30, static, 1, None, True, []],
           [cheese, 300, 450, 30, 30, moveCheese, 1, None, True, []],
           [rsk, 500, 500, 50, 60, static, 1, None, False, ["hihihi", " Iwant 3 cheese", " Because I'm hungry"]],
           [npc, 500, 200, 300, 300, static, 1, (0, 100, 60, 70), False, []]
           ]
         ),
          (src.colors["red"], [(src.display["dwidth"] - 50, 100, 0)],
           [[mouse, 300, 300, 60, 60, moveMouse, 1, None, True]]),
          (src.colors["brown"], [(src.display["dwidth"] - 50, 100, 0)], [])]


def create_region(gameDisplay, region_id, player_pos_x, player_pos_y, player_info):
    damage = 0
    pygame.draw.rect(
        gameDisplay, region[region_id][0], (0, 0, src.display["dwidth"], src.display["dheight"]))


    for sprites in region[region_id][2]:
        if sprites[6]:
            Sprite.draw_sprite(
                gameDisplay, sprites[0], sprites[1], sprites[2], sprites[3], sprites[4], sprites[7])
            if Sprite.check_collision([player_pos_x, player_pos_y, 50, 50], [sprites[1], sprites[2], sprites[3], sprites[4]]):
                if sprites[8]:
                    sprites[6] = 0
                    player_info["score"] += 1
                # pressedKeys = pygame.key.get_pressed()
                # if pressedKeys[pygame.K_RETURN]  and sprites[9]:
                #     is_dialogue_finished = False
                #     index = 0
                #     while not is_dialogue_finished:
                #         Text.draw_text(gameDisplay, "freesansbold.ttf", 30, sprites[9][index],
                #                        sprites[1], sprites[2] + 20, src.colors["red"])
                #         pygame.display.update()
                #         if (pygame.key.get_pressed() != pygame.K_SPACE):
                #             continue
                #         index += 1
                #         is_dialogue_finished = True
        sprites[1], sprites[2] = sprites[5](sprites[1], sprites[2])

    # Portals
    for portal_info in region[region_id][1]:
        if Portal.create_portal(gameDisplay, portal_info[0], portal_info[1], 50, 50, player_pos_x, player_pos_y):
            return create_region(gameDisplay, portal_info[2], player_pos_x, player_pos_y, player_info)
    return region_id
