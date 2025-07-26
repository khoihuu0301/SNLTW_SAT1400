import pygame
import random
import os
import json
from car import Car, Car2

# === SETUP ===
pygame.init()
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("F1 Street Dodger")
clock = pygame.time.Clock()

# === FONT & FILE ===
font = pygame.font.SysFont(None, 36)
HS_FILE = "highscore.json"
highscore = 0
if os.path.exists(HS_FILE):
    with open(HS_FILE, "r") as f:
        try:
            highscore = json.load(f).get("highscore", 0)
        except:
            highscore = 0

# === GAME BIẾN ===
score = 0
game_over = False

line_y = 0
line_speed = 5

PLAYER_IMG = r"C:\Users\Teky Binh Thanh\Desktop\BCCK4\F1.png"
ENEMY_IMG = r"C:\Users\Teky Binh Thanh\Desktop\BCCK4\Car.png"

car_width = 50
car_height = 100
player = Car(color=(0, 200, 255), speed=8, width=car_width, height=car_height, x=WIDTH//2 - car_width//2, y=HEIGHT - car_height - 10,  image_path= PLAYER_IMG)

obs_list = []
obs_timer = 0

# === Functions ===
def draw_track(screen, line_y):
    screen.fill((40, 40, 40))  # mặt đường

    # Vạch chia làn trắng giữa
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH//2 - 5, (i + line_y) % HEIGHT, 10, 30))

    # Lề đường đỏ trắng
    for i in range(0, HEIGHT, 40):
        color = (255, 0, 0) if (i//40) % 2 == 0 else (255, 255, 255)
        pygame.draw.rect(screen, color, (0, i, 10, 20))                 # Lề trái
        pygame.draw.rect(screen, color, (WIDTH - 10, i, 10, 20))        # Lề phải

# === GAME LOOP ===
running = True
while running:
    clock.tick(60)
    screen.fill((30, 30, 30))  # Nền tối như mặt đường

    line_y += line_speed

    draw_track(screen, line_y)

    # === VẼ LINE ĐƯỜNG ĐUA ===
    line_y += line_speed
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH//2 - 5, (i + line_y) % HEIGHT, 10, 20))
    
    car2_width = 50
    car2_height = 100
    car2_speed = 6

    # === SPAWN OBS ===
    obs_timer += 1
    if obs_timer >= 40:
        car2_x = random.randint(0, WIDTH - car2_width)
        car2_y = -car2_height
        obs_timer=0
        obs_list.append(Car2(color=(232, 123, 0), speed=car2_speed, width=car2_width, height=car2_height, x=car2_x, y=car2_y, image_path=ENEMY_IMG))

    # === SỰ KIỆN ===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                # RESET GAME
                score = 0
                game_over = False
                player.x = WIDTH//2 - car_width//2
                player.y = HEIGHT - car_height - 10
                obs_list.clear()

    if not game_over:
        # === ĐIỀU KHIỂN ===
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0:
            player.update("trai")
        if keys[pygame.K_d] and player.x < WIDTH - car_width:
            player.update("phai")
        if keys[pygame.K_w] and player.y > 0:
            player.update("len")
        if keys[pygame.K_s] and player.y < HEIGHT - car_height:
            player.update("xuong")

        # === UPDATE XE ĐỊCH ===
        for car2 in obs_list:
            car2.y += car2.speed
            if car2.y > HEIGHT:
                obs_list.remove(car2)
                score += 1

        # === VA CHẠM ===
        player_rect = pygame.Rect(player.x + player.width // 2, player.y, player.width, player.height - 15)
        for car2 in obs_list:
            obs_rect = pygame.Rect(car2.x + car2.width // 2, car2.y, car2.width, car2.height - 15)
            if player_rect.colliderect(obs_rect):
                if score > highscore:
                    highscore = score
                    with open(HS_FILE, "w") as f:
                        json.dump({"highscore": highscore}, f)
                game_over = True

    # === VẼ XE ===
    player.draw(screen)
    for car2 in obs_list:
        car2.draw(screen)


    # === VẼ SCORE & HIGH SCORE ===
    score_text = font.render(f"Score: {score}", True, (255, 255, 0))
    hs_text = font.render(f"High Score: {highscore}", True, (0, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(hs_text, (10, 40))

    # === GAME OVER MÀN HÌNH ===
    if game_over:
        text = font.render("Game Over!", True, (255, 0, 0))
        restart = font.render("Press R to Restart", True, (255, 255, 255))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2 + 30))

    pygame.display.update()

pygame.quit()
