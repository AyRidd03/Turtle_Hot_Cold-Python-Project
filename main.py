#!/usr/bin/env python

"""Proof of concept gfxdraw example"""

import pygame
import pygame.gfxdraw
import menu


def main():
    pygame.init()
    pygame.key.set_repeat(10)  # Lets Keys be held inputs
    screen = pygame.display.set_mode((500, 500))
    screen.fill((255, 0, 0))
    s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    pygame.draw.line(s, (0, 0, 0), (250, 250), (250 + 200, 250))

    width = 1
    for a_radius in range(width):
        radius = 200
        pygame.gfxdraw.aacircle(s, 250, 250, radius - a_radius, (0, 0, 0))

    screen.blit(s, (0, 0))

    pygame.display.flip()
    try:

        while True:
            # menu.set_cursor(s)
            event = pygame.event.wait(1)
            menu.menu_choices(screen, s, event)  # menu before the game starts
            if event.type == pygame.QUIT:
                break

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
