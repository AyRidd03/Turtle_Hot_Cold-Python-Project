import pygame
import pygame.gfxdraw
import math


class PlayerCircle:
    def __init__(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
        self.player_velx = 0
        self.player_vely = 0
        self.player_accx = 0
        self.player_accy = 0
        self.player_width = 200
        self.player_height = 175
        self.rock_img = pygame.image.load("The_Rock.png").convert_alpha()
        self.rock_img = pygame.transform.scale(self.rock_img, (self.player_width, self.player_height))
        self.boulder_img = pygame.image.load("Boulder.png").convert_alpha()
        self.boulder_img = pygame.transform.scale(self.boulder_img, (self.player_width, self.player_height))
        self.player_rect = self.boulder_img.get_rect(center=(self.player_x, self.player_y))
        self.old_distance = 0
        self.travel_distance = 0

    def move_player_circle(self, screen):
        old_position = (self.player_x, self.player_y)
        self.player_velx += self.player_accx
        self.player_vely += self.player_accy
        if int(self.player_x) in range(0, screen.get_width()) and int(self.player_y) in range(0, screen.get_height()):
            self.player_x += self.player_velx
            self.player_y += self.player_vely
        else:
            self.player_x -= self.player_velx * 2
            self.player_y -= self.player_vely * 2
            self.player_velx = 0
            self.player_vely = 0
            self.player_accx = 0
            self.player_accy = 0
        self.player_accx -= (self.player_accx / 8)
        self.player_accy -= (self.player_accy / 8)
        self.player_velx -= self.player_velx
        self.player_vely -= self.player_vely
        new_position = (self.player_x, self.player_y)
        self.add_travel(new_position, old_position)

    def draw_player_circle(self, h_circle, screen, s):
        # Redraws the player's image on the screen
        screen.blit(s, (0, 0))
        self.player_rect.center = (self.player_x, self.player_y)
        distance = math.sqrt((self.player_x - h_circle.x) ** 2 + (self.player_y - h_circle.y) ** 2)
        if distance < self.old_distance:
            screen.blit(self.rock_img, self.player_rect)
        else:
            screen.blit(self.boulder_img, self.player_rect)
        self.old_distance = distance

    def set_player_accx(self, player_accx):
        self.player_accx += player_accx

    def set_player_accy(self, player_accy):
        self.player_accy += player_accy

    def set_player_width(self, player_width):
        self.player_width = player_width
        self.rock_img = pygame.image.load("The_Rock.png").convert_alpha()
        self.rock_img = pygame.transform.scale(self.rock_img, (self.player_width, self.player_height))
        self.boulder_img = pygame.image.load("Boulder.png").convert_alpha()
        self.boulder_img = pygame.transform.scale(self.boulder_img, (self.player_width, self.player_height))
        self.player_rect = self.boulder_img.get_rect(center=(self.player_x, self.player_y))

    def set_player_height(self, player_height):
        self.player_height = player_height
        self.rock_img = pygame.image.load("The_Rock.png").convert_alpha()
        self.rock_img = pygame.transform.scale(self.rock_img, (self.player_width, self.player_height))
        self.boulder_img = pygame.image.load("Boulder.png").convert_alpha()
        self.boulder_img = pygame.transform.scale(self.boulder_img, (self.player_width, self.player_height))
        self.player_rect = self.boulder_img.get_rect(center=(self.player_x, self.player_y))

    def get_player_circle(self):
        return self.player_rect

    def get_player_distance(self, h_circle):
        distance = math.sqrt((self.player_x - h_circle.x) ** 2 + (self.player_y - h_circle.y) ** 2)
        return distance

    def get_old_distance(self):
        return self.old_distance

    def add_travel(self, new, old):
        old_x, old_y = old
        new_x, new_y = new
        self.travel_distance += math.sqrt((old_x - new_x) ** 2 + (old_y - new_y) ** 2)

    def get_travel_distance(self):
        return self.travel_distance
