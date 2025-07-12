import pygame
class Car:
    def __init__(self, color, speed, size, x, y):
        self.color = color
        self.speed = speed
        self.size = size
        self.x = x
        self.y = y
    def draw( self, surface):
        pygame.draw.rect(surface, (0, 200, 255), (self.x, self.y, self.size, self.size))
    
    speed = 1 


    def update(self, direction):
        if direction == "xuong":
            self.y += self.speed
        if direction == "len":
            self.y -= self.speed
        if direction == "trai":
            self.x -= self.speed
        if direction == "phai":
            self.x += self.speed
                



class Car2:
    def __init__(self, surface,color, speed, size, x, y):
        self.color = color
        self.speed = speed
        self.size = size
        self.x = x
        self.y = y
        self.draw(surface)
    def draw( self, surface):
        pygame.draw.rect(surface, (232, 123, 0), (self.x, self.y, self.size, self.size))
    
    speed = 1 
    x,y =0,0