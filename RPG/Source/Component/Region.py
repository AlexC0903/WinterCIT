import pygame
import Source.src as src
import Source.Component.Portal as Portal

def create_region(gameDisplay, color, Portals):
    pygame.draw.rect(
        gameDisplay, color, (0, 0, src.display["dwidth"], src.display["dheight"]))

        # Portals
    for portal_coordinates in Portals:
        Portal.create_portal(gameDisplay, portal_coordinates[0], portal_coordinates[1], 50, 50)
