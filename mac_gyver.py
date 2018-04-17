#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
Game MacGyver. Help him to get out of the labyrinth
Macgyver must collect randomly scatter objects in order to create a syringe
that will fall asleep the guard.

Script python 3
"""

import pygame

from pygame.locals import *

from classes import *

"""initialize all imported pygame modules"""
pygame.init()


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("MacGyver")
level = Level('level.txt')
level.generate()
level.display(screen)
pygame.display.flip()

GAME_LEVEL = 1

"""main loop"""
while GAME_LEVEL:
    pygame.time.Clock().tick(30)
           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_LEVEL = 0

    screen.fill(pygame.Color('black'))
    level.display(screen)
    pygame.display.flip()
