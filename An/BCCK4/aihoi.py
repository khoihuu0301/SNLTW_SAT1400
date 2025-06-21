import pygame
from car import Car

s = speed

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x = x + s
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x = x - s

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y = y + s
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            y = y - s

