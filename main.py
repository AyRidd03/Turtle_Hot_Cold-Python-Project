#!/usr/bin/env python

"""Proof of concept gfxdraw example"""

import pygame
import pygame.gfxdraw
import player as play
import menu


def main():
    pygame.init()
    pygame.key.set_repeat(10)  # Lets Keys be held inputs
    screen = pygame.display.set_mode((500, 500))
    screen.fill((255, 0, 0))
    s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    pygame.draw.line(s, (0, 0, 0), (250, 250), (250 + 200, 250))

    p = play.player_circle(250, 250)
    width = 1
    for a_radius in range(width):
        radius = 200
        pygame.gfxdraw.aacircle(s, 250, 250, radius - a_radius, (0, 0, 0))

    screen.blit(s, (0, 0))

    # Hidden Circle
    hidden_circle = pygame.draw.circle(screen, "black", (50, 100), 10, 1)

    pygame.display.flip()
    try:

        while True:
            # menu.set_cursor(s)
            # menu.menu_choices(screen, s)
            event = pygame.event.wait(1)
            if event.type == pygame.QUIT:
                break

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    p.set_player_accx(-0.5)
                elif event.key == pygame.K_RIGHT:
                    p.set_player_accx(0.5)
                elif event.key == pygame.K_UP:
                    p.set_player_accy(-0.5)
                elif event.key == pygame.K_DOWN:
                    p.set_player_accy(0.5)
                elif event.key == pygame.K_ESCAPE or event.unicode == "q":
                    break
            p.move_player_circle()

            if hidden_circle.colliderect(p.get_player_circle()):
                hidden_circle = pygame.draw.circle(screen, "blue", (50, 100), 10, 1)
            pygame.display.flip()
            p.draw_player_circle(hidden_circle, screen, s)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
