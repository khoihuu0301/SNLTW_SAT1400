import pygame
class Car:
    def __init__(self, color, speed, size, x, y):
        self.color = color
        self.speed = speed
        self.size = size
        self.x = 0
        self.y = 0
    def draw( self, surface):
        pygame.draw.rect(surface, (0, 200, 255), (self.x, self.y, self.size, self.size))
    
    speed = 1 
    x,y =0,0

    def update(self, direction):
        if direction == "xuong":
            self.y += self.speed
        if direction == "len":
            self.y -= self.speed
        if direction == "trai":
            self.x -= self.speed
        if direction == "phai":
            self.x += self.speed
                

        pygame.display.update()


class Car2:
    def __init__(self, surface,color, speed, size, x, y):
        self.color = color
        self.speed = speed
        self.size = size
        self.x = x
        self.y = y
        self.draw(surface)
    def draw( self, surface):
        pygame.draw.circle(surface, (0, 200, 255), (self.x, self.y), radius=self.size)
    
    speed = 1 
    x,y =0,0

    # def move(self, surface, mapping='WASD'):
    #     running = True
    #     if mapping ==  'WASD':
    #         while running:
    #             for event in pygame.event.get():
    #                 if event.type == pygame.QUIT:
    #                     running = False

    #             keys = pygame.key.get_pressed()
    #             if keys[pygame.K_a]:
    #                 self.x -= self.speed
    #             if keys[pygame.K_d]:
    #                 self.x += self.speed
    #             if keys[pygame.K_w]:
    #                 self.y -= self.speed
    #             if keys[pygame.K_s]:
    #                 self.y += self.speed

    #             self.x = max(0, min(500 - 50, self.x))
    #             self.y = max(0, min(500 - 50, self.y))


                # surface.fill((30, 30, 30))
                # self.draw(surface)
                # pygame.display.flip()
                

                # pygame.display.update()


    # def change_color(self, new_color):
    #     self.color = new_color
