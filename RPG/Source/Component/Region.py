import pygame
import Source.src as src
import Source.Component.Portal as Portal

region = [(src.colors["green"],  [(src.display["dwidth"] -
                                   50, 0, 1), (0, src.display["dheight"] - 50, 2)]), (src.colors["red"], []), (src.colors["black"], [])]


def create_region(gameDisplay, region_id, player_pos_x, player_pos_y):
    pygame.draw.rect(
        gameDisplay, region[region_id][0], (0, 0, src.display["dwidth"], src.display["dheight"]))

    # Portals
    for portal_info in region[region_id][1]:
        print(portal_info)
        if Portal.create_portal(gameDisplay, portal_info[0], portal_info[1], 50, 50, player_pos_x, player_pos_y):
            return create_region(gameDisplay, portal_info[2], player_pos_x, player_pos_y)
    return region_id
