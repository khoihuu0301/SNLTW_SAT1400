import pygame
import random
pygame.init()
win = pygame.display.set_mode((500, 500))

WIDTH = 500
HEIGHT = 500
SQUARE_SIZE = 50
x = 60
y = 60
color_meteorite= (0, 128, 255)
color_plane = (0,0,128)
done = False
is_red = False
speed_plane = 10
speed_meteorite = 3
speed_laser = 20
size = 5
clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
# pygame.draw.rect(win , color, pygame.Rect(x, y, 90, 90))

meteorite1 = []

class Obstacle:
    def __init__(self, x, y, width=50, height=50, color=(255, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed_plane
        self.color = color_meteorite

    def update(self):
        self.rect.y += self.speed
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def random_obstacle(screen_width, screen_height, width=50, height=50):
        x = random.randint(0, screen_width - width)
        y = 0
       
    
        

class Laser:
    def __init__(self, x, y,  width=5, height=20):
        self.x = x
        self.y = y
        self.speed = speed_laser
        self.color = color_meteorite
        self.width = width
        self.height = height

    def update(self):
        self.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def collide(self, obstacle):
        # Tạo rect cho laser để kiểm tra va chạm
        laser_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return laser_rect.colliderect(obstacle.rect)

class plane:
    def __init__(self, size,  x=0, y=450):
        self.speed = speed_plane
        self.size = size
        self.color = color_plane
        self.x = x
        self.y = y
        self.lasers = []

    def draw(self, surface=None):
        if surface is None:
            surface = win
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        for laser in self.lasers:
            laser.draw(surface)

    def update(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        self.x = max(0, min(WIDTH - self.size, self.x))
        self.y = max(0, min(HEIGHT - self.size, self.y))

    def shoot(self):
        laser_x = self.x + self.size // 2 - 2
        laser_y = self.y
        self.lasers.append(Laser(laser_x, laser_y))

    

    def collide(self, obstacle):
        plane_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        return plane_rect.colliderect(obstacle.rect)

if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    plane_size = 40
    player = plane(size=plane_size,x=WIDTH//2 - plane_size//2, y=HEIGHT-100 - plane_size - 10)
    
    obstacles = []
    obstacle_timer = 0
    obstacle_interval = 60  # số frame giữa các lần sinh chướng ngại vật mới
    
    lasers = []
    

   
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.update("left")
                elif event.key == pygame.K_RIGHT:
                    player.update("right")
                elif event.key == pygame.K_SPACE:
                    lasers.append(Laser(player.x + player.size // 2 - 2, player.y))
        # Di chuyển plane bằng phím giữ
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.update("left")
        if keys[pygame.K_RIGHT]:
            player.update("right")

        screen.fill((0, 0, 0))

        # Sinh chướng ngại vật mới
        obstacle_timer += 1
        if obstacle_timer >= obstacle_interval:
            obstacles.append(Obstacle(random.randint(0, WIDTH - 50), -50))
            obstacle_timer = 0

        # Cập nhật và vẽ laser
        for laser in lasers:
            laser.update()
        lasers = [l for l in lasers if l.y + l.height > 0]
        # Cập nhật và vẽ chướng ngại vật
        for obs in obstacles:
            obs.update()
        obstacles = [obs for obs in obstacles if obs.rect.y < HEIGHT]

        # Kiểm tra va chạm giữa plane và chướng ngại vật
        for obs in obstacles:
            if player.collide(obs):
                running = False

        # Kiểm tra va chạm giữa laser và chướng ngại vật
        for obs in obstacles[:]:
            for laser in lasers[:]:
                if laser.collide(obs):
                    if obs in obstacles:
                        obstacles.remove(obs)
                    if laser in  lasers:
                        lasers.remove(laser)
                    break

        # Vẽ chướng ngại vật
        for obs in obstacles:
            obs.draw(screen)
        for laser in lasers:
            laser .draw(screen)

        # Vẽ plane và laser
        player.draw(screen)

        # Thoát nếu plane chạm biên màn hình
        if (
            player.x < 0 or
            player.x + player.size > WIDTH or
            player.y < 0 or
            player.y + player.size > HEIGHT
        ):
            running = False

        pygame.display.flip()
        clock.tick(60)

pygame.display.update()