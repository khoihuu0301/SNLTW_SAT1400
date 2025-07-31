import pygame

class SecondMenu:
    def __init__(self):
        self.font = pygame.font.SysFont("Times New Roman", 80)
        self.title = self.font.render("This is second", True, (255, 255, 255))
        self.title_position = (10, 10)
        self.main_menu = None  # Sẽ được gán từ ngoài

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.main_menu:
                        return self.main_menu
        return self

    def draw(self, screen):
        screen.blit(self.title, self.title_position)