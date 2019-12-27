import pygame
import Source.UI.Sprite as Sprite


def draw_button(gameDisplay, ref_width, ref_height, ratio, color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    buttonX = ref_width * ratio["x_ratio"]
    buttonY = ref_height * ratio["y_ratio"]
    buttonW = ref_width * ratio["w_ratio"]
    buttonH = ref_height * ratio["h_ratio"]
    pygame.draw.rect(
        gameDisplay, color, (buttonX, buttonY, buttonW, buttonH))

    if buttonX + buttonW > mouse[0] > buttonX and buttonY + buttonH > mouse[1] > buttonY and click[0] == 1:
        return True
    return False

def draw_spriteButton(gameDisplay, img, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    Sprite.draw_sprite(gameDisplay, img, x, y, w, h)
    if x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
        return True
    return False
    # smallText = pygame.font.Font("freesansbold.ttf", 20)
    # textSurf, textRect = src.HUD.text_objects(
    #     src.menu_buttons[index]["content"], smallText)
    # textRect.center = ((ref_width * ratio["txt_x_ratio"],
    #                    ref_height * ratio["txt_y_ratio"])
    # src.gameDisplay.blit(textSurf, textRect)
