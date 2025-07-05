import pygame
import random

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

if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 400, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Player car setup
    car_size = 40
    player = Car(color=(0, 200, 255), speed=5, size=car_size, x=WIDTH//2 - car_size//2, y=HEIGHT - car_size - 10)
    player.x = WIDTH//2 - car_size//2
    player.y = HEIGHT - car_size - 10

    # Car2 setup
    car2_size = 30
    car2_speed = 5
    car2_x = random.randint(0, WIDTH - car2_size)
    car2_y = -car2_size
    car2 = Car2(screen, color=(255, 0, 0), speed=car2_speed, size=car2_size, x=car2_x, y=car2_y)

    running = True
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.update("trai")
        if keys[pygame.K_RIGHT] and player.x < WIDTH - player.size:
            player.update("phai")
        if keys[pygame.K_UP] and player.y > 0:
            player.update("len")
        if keys[pygame.K_DOWN] and player.y < HEIGHT - player.size:
            player.update("xuong")

        # Car2 movement
        car2.y += car2.speed
        if car2.y > HEIGHT:
            car2.x = random.randint(0, WIDTH - car2.size)
            car2.y = -car2.size

        # Draw cars
        player.draw(screen)
        car2.draw(screen)

        # Collision detection (rect-circle)
        player_rect = pygame.Rect(player.x, player.y, player.size, player.size)
        dist_x = abs(car2.x - player_rect.centerx)
        dist_y = abs(car2.y - player_rect.centery)
        if dist_x <= (player.size // 2 + car2.size) and dist_y <= (player.size // 2 + car2.size):
            # Simple collision check
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over!", True, (255, 0, 0))
            screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        pygame.display.update()

    pygame.quit()

