#!/usr/bin/env python

"""Proof of concept gfxdraw example"""

import pygame
import pygame.gfxdraw


def main():
    player_x = 250
    player_y = 250
    player_velx = 0
    player_vely = 0
    player_accx = 0
    player_accy = 0
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

    player_circle = pygame.draw.circle(screen, "green", (player_x, player_y), 10)
    # Hidden Circle
    hidden_circle = pygame.draw.circle(screen, "black", (50, 100), 10, 1)

    pygame.display.flip()
    try:
        while True:
            event = pygame.event.wait(1)
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    player_accx -= 0.5
                elif event.key == pygame.K_RIGHT:
                    player_accx += 0.5
                elif event.key == pygame.K_UP:
                    player_accy -= 0.5
                elif event.key == pygame.K_DOWN:
                    player_accy += 0.5
                elif event.key == pygame.K_ESCAPE or event.unicode == "q":
                    break
            # Below changes and resets values to apply physics

            player_velx += player_accx
            player_vely += player_accy
            player_accx -= (player_accx / 8)
            player_accy -= (player_accy / 8)
            player_x += player_velx
            player_y += player_vely
            player_velx -= player_velx
            player_vely -= player_vely

            # Redraws the circle on the screen
            player_circle.x = player_x
            player_circle.y = player_y
            print(f"X {player_circle.x}")
            print(f"Y {player_circle.y}")
            screen.fill((200, 100, 50))
            screen.blit(s, (0, 0))
            player_circle = pygame.draw.circle(screen, "green", (player_x, player_y), 10)
            if(hidden_circle.colliderect(player_circle)):
                hidden_circle = pygame.draw.circle(screen, "blue", (50, 100), 10, 1)
            player_circle.update(player_circle)

            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
