#!/usr/bin/env python

"""Proof of concept gfxdraw example"""

import pygame
import pygame.gfxdraw
import math


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

    rock_img = pygame.image.load("The_Rock.png").convert_alpha()
    rock_img = pygame.transform.scale(rock_img, (100, 75))
    boulder_img = pygame.image.load("Boulder.png").convert_alpha()
    boulder_img = pygame.transform.scale(boulder_img, (100, 75))
    player_rect = boulder_img.get_rect(center=(player_x, player_y))

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

            # Redraws the player's image on the screen
            player_rect.center = (player_x, player_y)
            screen.fill((200, 100, 50))
            screen.blit(s, (0, 0))
            distance = math.sqrt((player_x - 100) ** 2 + (player_y - 100) ** 2)

            if distance < 50:
                screen.blit(rock_img, player_rect)
            else:
                screen.blit(boulder_img, player_rect)

            if hidden_circle.colliderect(player_rect):
                hidden_circle = pygame.draw.circle(screen, "blue", (50, 100), 10, 1)
            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
