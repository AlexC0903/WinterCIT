import pygame
import src
import Menu

pygame.init()

def draw_sprite(img, x, y, w, h):
    src.gameDisplay.fill(src.colors["white"])
    img = pygame.transform.scale(img, (w, h))
    src.gameDisplay.blit(img, (x, y))
    
def draw_button(img, x, y, w, h, action1=None, action2=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    draw_sprite(img, x, y, w, h)
    if x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
        if action1!=None and action2!=None and click[0] == 1:
            action1()
            action2()
        elif action1!=None and click[0] == 1:
            action1()
        
        

def draw_screen():
    # Quit Button
    draw_button(src.quitImg, src.display["dwidth"] * (59/64), src.display["dheight"] * (1/39), 50, 50, pygame.quit, quit)


def game_loop():
    pygame.display.set_caption('The Quest for Cheese')

    dead = False
    while not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
        draw_screen()
        pygame.display.update()
        src.clock.tick(src.framerate)

    game_loop()
    pygame.quit()
    quit()