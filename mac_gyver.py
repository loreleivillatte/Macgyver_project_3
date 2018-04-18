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

MAC_GYVER = Player("pictures/mac_down.png", "pictures/mac_left.png",
                   "pictures/mac_right.png", "pictures/mac_up.png", level)
pygame.key.set_repeat(1, 40)

"""display loot"""
TUBE_IMG = pygame.image.load(TUBE_POS).convert_alpha()
NEEDLE_IMG = pygame.image.load(NEEDLE_POS).convert_alpha()
ETHER_IMG = pygame.image.load(ETHER_POS).convert_alpha()

"""position loot in level"""
TUBE_POS = Loot(TUBE_IMG, level)
TUBE_POS.display(TUBE_IMG, screen)
NEEDLE_POS = Loot(NEEDLE_IMG, level)
NEEDLE_POS.display(NEEDLE_IMG, screen)
ETHER_POS = Loot(ETHER_IMG, level)
ETHER_POS.display(ETHER_IMG, screen)

pygame.display.flip()

GAME_LEVEL = 1

TUBE_NOTPICKED = True
ETHER_NOTPICKED = True
NEEDLE_NOTPICKED = True

GAME_WON = False
GAME_LOOSE = False

"""main loop"""
while GAME_LEVEL:
    pygame.time.Clock().tick(30)
           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_LEVEL = 0

        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                MAC_GYVER.update('down')
            elif event.key == K_LEFT:
                MAC_GYVER.update('left')
            elif event.key == K_RIGHT:
                MAC_GYVER.update('right')
            elif event.key == K_UP:
                MAC_GYVER.update('up')

    screen.fill(pygame.Color('black'))
    level.display(screen)
    screen.blit(MAC_GYVER.direction, (MAC_GYVER.x, MAC_GYVER.y))
    pygame.display.flip()

    if TUBE_NOTPICKED:
        screen.blit(TUBE_POS.Loot_Image, (TUBE_POS.x, TUBE_POS.y))
        if (MAC_GYVER.x, MAC_GYVER .y) == (TUBE_POS.x, TUBE_POS.y):
            TUBE_NOTPICKED = False
    if TUBE_NOTPICKED == False:
        screen.blit(TUBE_POS.Loot_Image, (80, 0))
        
    if NEEDLE_NOTPICKED:
        screen.blit(NEEDLE_POS.Loot_Image, (NEEDLE_POS.x, NEEDLE_POS.y))
        if (MAC_GYVER.x, MAC_GYVER .y) == (NEEDLE_POS.x, NEEDLE_POS.y):
            NEEDLE_NOTPICKED = False
    if NEEDLE_NOTPICKED == False:
        screen.blit(NEEDLE_POS.Loot_Image, (120, 0))
        
    if ETHER_NOTPICKED:
        screen.blit(ETHER_POS.Loot_Image, (ETHER_POS.x, ETHER_POS.y))
        if (MAC_GYVER.x, MAC_GYVER .y) == (ETHER_POS.x, ETHER_POS.y):
            ETHER_NOTPICKED = False
    if ETHER_NOTPICKED == False:
        screen.blit(ETHER_POS.Loot_Image, (160, 0))
        
    pygame.display.flip()

    if level.structure[MAC_GYVER.case_y][MAC_GYVER.case_x] == 'e':
        if TUBE_NOTPICKED == False:
            if NEEDLE_NOTPICKED == False:
                if ETHER_NOTPICKED == False:
                    GAME_WON = True
                    GAME_LEVEL = 0
        else:
            GAME_LOOSE = True
            GAME_LEVEL = 0
