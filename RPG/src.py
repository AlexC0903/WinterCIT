import pygame

display = {"dwidth": 800, "dheight": 600}
colors = {"red" : (255,0,0), "white": (255,255,255), "black": (0, 0, 0), "green": (44, 255, 20), "grey": (92, 110, 90)}
menu_buttons = [{"content": "Go!", "color": colors["green"]}, {"content": "Settings", "color": colors["grey"]}, {"content": "Quit", "color": colors["red"]}]
quitImg = pygame.image.load('src/x.jpg')
quitImg = pygame.transform.scale(quitImg, (50, 50))
framerate = 60
gameDisplay = pygame.display.set_mode((display["dwidth"], display["dheight"]))
clock = pygame.time.Clock()
