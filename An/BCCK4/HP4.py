import pygame
import random
from car import Car, Car2
from car import Car2, Car

if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 400,600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock =pygame.time.Clock()

    car_size = 40
    player = Car(color=(0, 200, 255), speed = 5, size = car_size, x=WIDTH//2 - car_size//2, y = HEIGHT - car_size - 10 )
    player.x = WIDTH//2 - car_size//2
    player.y = HEIGHT - car_size - 10

    car2_size = 40 
    car2_speed = 5
    car2_x = random.randint(0, WIDTH - car2_size)
    car2_y = -car2_size
    car2 = Car2(screen, color=(255,0,0), speed=car2_speed, size=car2_size, x=car2_x, y=car2_y)

    running = True
    while running:
        clock.tick(60)
        screen.fill((0,0,0))    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.update("trai")
        if keys[pygame.K_RIGHT] and player.x < WIDTH - car_size:
            player.update("phai")
        if keys[pygame.K_UP] and player.y > 0:
            player.update("len")
        if keys[pygame.K_DOWN] and player.x < HEIGHT - car_size:
            player.update("xuong")

        car2.y += car2.speed
        if car2.y > HEIGHT:
            car2.x = random.randint(0, WIDTH - car2_size)
            car2.y = -car2.size

        player.draw(screen)
        car2.draw(screen)

        player_rect = pygame.Rect(player.x, player.y, player.size, player.size)
        dist_x = abs(car2.x + car2_size // 2 - player_rect.centerx)
        dist_y = abs(car2.y + car2_size // 2 - player_rect.centery)
        if dist_x <= (player.size // 2 + car2.size) and dist_y <= (player.size // 2 + car2.size):
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over!", True, (255, 0, 0))
            screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False
    
        pygame.display.update()
# i = 0

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#         if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
#             i = i + 1
#             if i >= len(color_list):
#                 i = 0  # Reset i về 0 nếu vượt quá số màu trong color_list
#             Porsche.change_color(color_list[i])  # Thay đổi màu của Porsche
            
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
#             i = i - 1
#             if i < 0:  # Nếu i nhỏ hơn 0, reset lại về chỉ số cuối của color_list
#                 i = len(color_list) - 1
#             Porsche.change_color(color_list[i])  # Thay đổi màu của Porsche


    # # Vẽ lại màn hình và Porsche với màu mới
    # win.fill((255, 255, 255))  # Xóa màn hình (màu nền trắng)
    # pygame.draw.rect(win, Porsche.color, pygame.Rect(x, y, 90, 90))  # Vẽ Porsche với màu mới


# BMW = Car2(surface=win, color=G, speed=1, size = 50, x= 30, y= 50)
# Porsche = Car(color=R, speed=1, size = 50, x= 0, y= 0)
# Porsche.move(win, mapping='arrow')



pygame.quit()
