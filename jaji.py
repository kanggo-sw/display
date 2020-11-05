import pygame

import time

pygame.init()


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

display_surface = pygame.display.set_mode(
    (800, 600),
)
pygame.display.set_caption("Show Text")

font = pygame.font.Font("ChosunCentennial_ttf.ttf", 356)
clock = pygame.time.Clock()


def gogo():
    wait_for = 1000
    sexit = False

    while not sexit:
        display_surface.fill((0,0,0))
        text = font.render("통과", True, (255, 255, 0))
        textRect = text.get_rect()
        textRect.center = (400, 250)
        display_surface.blit(text, textRect)

        pygame.display.update()

        passed_time = clock.tick(60)
        wait_for -= passed_time
        if wait_for <= 0:
            sexit = True

    time.sleep(1)


while True:
    display_surface.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gogo()


                

        else:
            text = font.render("대기", True, (0, 0, 255))
            textRect = text.get_rect()
            textRect.center = (400, 250)
            display_surface.blit(text, textRect)

        pygame.display.update()
        clock.tick(60)
        
