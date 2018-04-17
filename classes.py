"""classes level"""

import pygame

from pygame.locals import *

from constants import *


class Level:
    """create labyrinth"""
    def __init__(self, file):
        """use file .txt"""
        self.file = "level.txt"
        self.frame = 0

    def generate(self):
        """generate level of labyrinth,
        create a general list, containing a list per line to display"""
        with open(self.file) as file:
            frame_level = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                frame_level.append(line_level)
            self.frame = frame_level

    def display(self, screen):
        """display level depends on structure of list returned by generate"""
        wall = pygame.image.load("pictures/wall.png").convert()
        end = pygame.image.load("pictures/guard.png").convert_alpha()
        num_line = 0
        for line in self.frame:
            num_case = 0
            for sprite in line:
                sprite_x = num_case * sprite_size
                sprite_y = num_line * sprite_size
                if sprite == 'w':
                    screen.blit(wall, (sprite_x, sprite_y))
                elif sprite == "e":
                    screen.blit(end, (sprite_x, sprite_y))
                num_case += 1
            num_line += 1
