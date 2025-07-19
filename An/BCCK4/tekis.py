import pygame
import random
class figure:
    x = 0
    y = 0
    figures = [
        [[1,5,9,13], [4, 5, 6, 7]],
        [[1,2,5,9], [0, 4, 5, 6], [1, 5, 6, 10]],
        [[1, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 6], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, 7)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]
    
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])

class tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height =20
    width = 10
    zoom = 30
    x = 100
    y = 60
    figures = None

    def __init__(self):
        self.field = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.new_figure()

    def new_figure(self):
        self.figure = figure(3, 0)

    def intersects(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    y = i + self.figure.y
                    x = j + self.figure.x
                    if y >= self.height or x >= self.width or x < 0 or self.field[y][x]:
                        return True
        return False
    
    def freeze(self):
        for i in range(4):
            for j in range (4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines(self)
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            if 0 not in self.field[i]:
                del self.field[i]
                self.field.insert(0, [0 for _ in range(self.width)])
                lines += 1
        self.score == lines **2

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation


color = [
    (0, 0, 0),
    (255, 0, 0),
    (0,155,0),
    (0,0,255),
    (255, 120,0),
    (255,255,0),
    (180,0,255),
    (0,220,220)
]

pygame.init()
size = (400,600)
screen = pygame. display.set_mode(size)
pygame.display.set_caption("tetris")
done =False
clock = pygame.time.Clock()
fps = 30
game = tetris()
counter = 0

while not done:
    if game.state == "start":
        counter+=1
        if counter >1000:
            counter = 0 
        if counter % (fps // game.level // 2) == 0:
            game.go_down()
        else:
            game.just_spawned = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            elif event.key == pygame.K_DOWN:
                game.go_down()
            elif event.key == pygame.K_LEFT:
                game.go_side(-1)
            elif event.key == pygame.K_RIGHT:
                game.go_side(1)

    screen.fill((0,0,0))

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, (128, 128, 128),
                            [game.x + game.zoom * j + 1, game.y +game.zoom * i, game.zoom, game.zoom])
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, color[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y +game.zoom * i + 1, game.zoom - 2, game.zoom - 2])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                if i * 4 + j in game.figure.image():
                    if i * 4 + j in game.figure.image():
                        pygame.draw.rect(screen, color[game.figure.color],
                                        [game.x + game.zoom * (j + game.figure.x) + 1,
                                        game.y + game.zoom * (i + game.figure.y) + 1,
                                        game.zoom - 2, game.zoom - 2])
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Diem: "+ str(game.score), True, (255, 255, 255))
    screen.blit(text, [0, 0])

    if game.state == "gameover":
        font = pygame.font.SysFont('calibri', 65, True, False)
        text_game_over = font.render("Game Over", True, (255,125,0))
        screen.blit(text_game_over, [40, 250])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()