import time

import pygame

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

display_surface = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN,
)
pygame.display.set_caption("강원고등학교")

font = pygame.font.Font("ChosunCentennial_ttf.ttf", 400)
clock = pygame.time.Clock()
loop = True

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


def text_obj(text: str, x: int = SCREEN_WIDTH // 2, y: int = SCREEN_HEIGHT // 2, color: tuple = white):
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=(x, y))

    return text, text_rect


def passed():
    display_surface.fill(green)
    display_surface.blit(*text_obj("통과"))

    pygame.display.update()

    time.sleep(1.25)


def banned():
    display_surface.fill(red)
    display_surface.blit(*text_obj("발열"))

    pygame.display.update()

    time.sleep(1.25)


def wait():
    display_surface.blit(*text_obj("대기"))


while loop:
    display_surface.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False

            elif event.key == pygame.K_SPACE:
                passed()

            elif event.key == pygame.K_1:
                banned()

        else:
            wait()

        pygame.display.update()
        clock.tick(60)

pygame.quit()
