import pygame
import random
import time
pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound(r'C:\Users\ASUS\OneDrive\Máy tính\Code\SNLTW_SAT1400\Bao\laser-shot-ingame-230500.mp3')
sound.set_volume(1)

sound_break = pygame.mixer.Sound(r'C:\Users\ASUS\OneDrive\Máy tính\Code\SNLTW_SAT1400\Bao\bomb-333672 (1).mp3')
sound_break.set_volume(10)

WIDTH = 500
HEIGHT = 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Game")

color_meteorite = (0, 128, 255)
color_plane = (0, 0, 128)
speed_plane = 10
speed_meteorite = 5
speed_laser = 20

class Obstacle:
    def __init__(self, x, y, width=50, height=50, color=(255, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed_plane
        self.color = color_meteorite
        self.image = pygame.image.load(r"C:\Users\ASUS\OneDrive\Máy tính\Code\SNLTW_SAT1400\Bao\png-clipart-planet-cartoon-green-moon-blue-teal-thumbnail-removebg-preview.png")  # Đường dẫn tới ảnh meteorite
        self.image = pygame.transform.scale(self.image, (width, height))

    def update(self):
        self.rect.y += self.speed
        
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Laser:
    def __init__(self, x, y, width=5, height=20):
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
        laser_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return laser_rect.colliderect(obstacle.rect)

class plane:
    def __init__(self, size, x=0, y=450):
        self.speed = speed_plane
        self.size = size
        self.color = color_plane
        self.x = x
        self.y = y
        self.lasers = []
        self.image = pygame.image.load(r"C:\Users\ASUS\OneDrive\Máy tính\Code\SNLTW_SAT1400\Bao\images__1_-removebg-preview.png")  # Đường dẫn tới ảnh plane
        self.image = pygame.transform.scale(self.image, (size, size))

    def draw(self, surface=None):
        if surface is None:
            surface = win
        surface.blit(self.image, (self.x, self.y))
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

def show_start_screen():
    font = pygame.font.SysFont('Arial', 40)
    button_font = pygame.font.SysFont('Arial', 30)
    title_text = font.render("PLANE GAME", True, (255, 0, 0))
    button_text = button_font.render("START", True, (0, 0, 0))
    button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2, 150, 50)
    waiting = True
    while waiting:
        win.fill((0, 0, 0))
        win.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 100))
        pygame.draw.rect(win, (255, 0, 0), button_rect)
        win.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                               button_rect.y + (button_rect.height - button_text.get_height()) // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False

def load_high_score(filename="highscore.txt"):
    try:
        with open(filename, "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score, filename="highscore.txt"):
    with open(filename, "w") as f:
        f.write(str(score))


if __name__ == "__main__":
    show_start_screen()  # Hiển thị cửa sổ bắt đầu

    pygame.mixer.music.load(r'C:\Users\ASUS\OneDrive\Máy tính\Code\SNLTW_SAT1400\Bao\background.wav')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)  # Phát nhạc nền lặp lại

    plane_size = 40
    player = plane(size=plane_size, x=WIDTH // 2 - plane_size // 2, y=HEIGHT - plane_size)
    obstacles = []
    obstacle_timer = 0
    obstacle_interval = 60
    lasers = []
    clock = pygame.time.Clock()
    running = True

    score = 0
    high_score = load_high_score()
    font_score = pygame.font.SysFont('Arial', 28)

    meteorite_speed = speed_meteorite  # tốc độ ban đầu
    last_speedup_time = time.time()

    while running:
        clock.tick(60)
        now = time.time()
        # Tăng tốc meteorite mỗi 4 giây
        if now - last_speedup_time >= 4:
            meteorite_speed += 1
            last_speedup_time = now

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
                    sound.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.update("left")
        if keys[pygame.K_RIGHT]:
            player.update("right")

        win.fill((0, 0, 0))

        # Vẽ background trước
       

        obstacle_timer += 1
        if obstacle_timer >= obstacle_interval:
            # Truyền tốc độ meteorite hiện tại vào Obstacle
            obstacles.append(Obstacle(random.randint(0, WIDTH - 50), -50))
            obstacles[-1].speed = meteorite_speed
            obstacle_timer = 0

        for obs in obstacles:
            obs.speed = meteorite_speed  # Đảm bảo tất cả meteorite đều tăng tốc
            obs.update()
        obstacles = [obs for obs in obstacles if obs.rect.y < HEIGHT]

        for laser in lasers:
            laser.update()
        lasers = [l for l in lasers if l.y + l.height > 0]

        for obs in obstacles:
            if obs.rect.y + obs.rect.height >= HEIGHT:
                running = False

        for obs in obstacles:
            if player.collide(obs):
                running = False

        for obs in obstacles[:]:
            for laser in lasers[:]:
                if laser.collide(obs):
                    if obs in obstacles:
                        obstacles.remove(obs)
                    if laser in lasers:
                        lasers.remove(laser)
                    sound_break.play()
                    score += 1  # Tăng điểm khi bắn trúng meteorite
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)
                    break

        for obs in obstacles:
            obs.draw(win)
        for laser in lasers:
            laser.draw(win)

        player.draw(win)

        # Hiển thị điểm và điểm cao nhất
        score_text = font_score.render(f"Score: {score}", True, (255, 255, 0))
        high_score_text = font_score.render(f"High Score: {high_score}", True, (255, 255, 255))
        win.blit(score_text, (10, 10))
        win.blit(high_score_text, (10, 40))

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