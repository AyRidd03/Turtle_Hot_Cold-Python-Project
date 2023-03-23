#!/usr/bin/env python

"""Proof of concept gfxdraw example"""

import pygame
import pygame.gfxdraw
import menu


def main():
    pygame.init()
    pygame.key.set_repeat(10)  # Lets Keys be held inputs
    screen = pygame.display.set_mode((1900, 1000))
    screen.fill((255, 0, 0))
    s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    pygame.display.flip()
    try:
        easy_record = menu.Record()
        med_record = menu.Record()
        hard_record = menu.Record()
        while True:
            # menu.set_cursor(s)
            event = pygame.event.wait(1)
            menu.menu_choices(screen, s, event, easy_record, med_record, hard_record)  # menu before the game starts
            if event.type == pygame.QUIT:
                break

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
