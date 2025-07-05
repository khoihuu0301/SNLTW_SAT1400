import pygame
import random
pygame.init()
win = pygame.display.set_mode((500, 500))

WIDTH = 500
HEIGHT = 500
SQUARE_SIZE = 50
x = 60
y = 60
color = (0, 128, 255)
done = False
is_red = False
speed = 5
size = 90
clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
# pygame.draw.rect(win , color, pygame.Rect(x, y, 90, 90))
     

class plane:
    def __init__(self, x, y):
        self.speed = speed
        self.size = size
        self.color = (0, 128, 255)
        self.x = 0
        self.y = 0
        
    
    def draw(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, 90, 90))           

    def move(self, surface , mapping = "arrow"):
        running = True
        if mapping == "arrow":
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.x -= self.speed
                if keys[pygame.K_RIGHT]:
                    self.x += self.speed
                if keys[pygame.K_UP]:
                    self.y -= self.speed
                if keys[pygame.K_DOWN]:
                    self.y += self.speed

                self.x = max(0, min(WIDTH - self.size, self.x))
                self.y = max(0, min(HEIGHT - self.size, self.y))
                
                surface.fill((30, 30, 30))
                self.draw()
                pygame.display.flip()
                clock.tick(60)
    def update(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        elif direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed

        # Ensure the car stays within bounds
        self.x = max(0, min(WIDTH - self.size, self.x))
        self.y = max(0, min(HEIGHT - self.size, self.y))
        
car2 = plane(speed, SQUARE_SIZE)
car2.move(win, mapping="arrow")

class meteorite:
    def __init__(self, x, y):
        self.speed = speed
        self.size = size
        self.color = (0, 128, 255)
        self.x = 0
        self.y = 0
    def draw(self):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, 90, 90))   
if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 728, 1024
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    plane_size = 40
    meteoritefly = car2(color = (255, 0, 0), speed = 5, size = plane_size, x=WIDTH//2, y=HEIGHT-100 - plane_size - 10)
    meteoritefly.x = WIDTH // 2 - plane_size // 2
    meteoritefly.y = HEIGHT - 100 - plane_size - 10
    
    car2_size = 40
    car2_speed = 5
    car2_x = random.randint(0, WIDTH - car2_size)
    car2_y = -car2_size
    car2 = meteorite(screen, color=(255, 0, 0), speed=car2_speed, size=car2_size, x=car2_x, y=car2_y)
    
    running = True
    while running:
        clock.tick(60)
        
        screen.fill((0, 0, 0))
        
        # Update and draw the plane
        meteoritefly.update("down")
        meteoritefly.draw()
        
        # Update and draw the car2
        car2.update("down")
        car2.draw()
        
        pygame.display.flip()
        clock.tick(60)
    

pygame.display.update()