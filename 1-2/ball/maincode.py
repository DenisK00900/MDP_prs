import pygame
from random import randint
import math

pygame.init()

size_x = 800
size_y = 800

balls_count = 64
balls_speed = 400

Window = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Арканоид")

FPS = 60

pygame.mouse.set_visible(True)
clock = pygame.time.Clock()

ball = pygame.image.load("icon.png").convert()
ball.set_colorkey((0, 0, 0))

ball2 = pygame.image.load("icon2.png").convert()
ball2.set_colorkey((0, 0, 0))

button = pygame.image.load("start_button_flame12.png").convert()
button.set_colorkey((255, 255, 255))

button_prestsad = False

run = True

class circule_col:
    def __init__(self, ix=0, iy=0, ir=0, isx=0, isy=0):
        self.x = ix
        self.y = iy
        self.r = ir
        self.speed_x = isx
        self.speed_y = isy

    def set(self, ix, iy, ir, isx, isy):
        self.x = ix
        self.y = iy
        self.r = ir
        self.speed_x = isx
        self.speed_y = isy

    def update(self):
        self.x += self.speed_x * (1 / FPS)
        self.y += self.speed_y * (1 / FPS)

        if self.x >= size_x - self.r:
            self.speed_x *= -1
        if self.y >= size_y - self.r:
            self.speed_y *= -1
        if self.x <= self.r:
            self.speed_x *= -1
        if self.y <= self.r:
            self.speed_y *= -1

def check_circule_col(i1, i2):
    dis = math.sqrt((i1.x - i2.x) ** 2 + (i1.y - i2.y) ** 2)
    return dis < (i1.r + i2.r)

def resolve_collision(circle1, circle2):

    dx = circle2.x - circle1.x
    dy = circle2.y - circle1.y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    
    overlap = (circle1.r + circle2.r) - distance
    
    if overlap > 0:
        if distance != 0:
            nx = dx / distance
            ny = dy / distance
            
            circle1.x -= nx * (overlap / 2)
            circle1.y -= ny * (overlap / 2)
            circle2.x += nx * (overlap / 2)
            circle2.y += ny * (overlap / 2)


            v1n = circle1.speed_x * nx + circle1.speed_y * ny
            v2n = circle2.speed_x * nx + circle2.speed_y * ny

            circle1.speed_x -= v1n * nx
            circle1.speed_y -= v1n * ny
            circle2.speed_x -= v2n * nx
            circle2.speed_y -= v2n * ny
            
            circle1.speed_x += v2n * nx
            circle1.speed_y += v2n * ny
            circle2.speed_x += v1n * nx
            circle2.speed_y += v1n * ny
            
mainmas = []

for i in range(balls_count):
    mainmas.append(
        circule_col(
            randint(20, 700),
            randint(20, 700),
            16,
            randint(-balls_speed, balls_speed),
            randint(-balls_speed, balls_speed)
        )
    )

mainmas2 = []

for i in range(balls_count):
    mainmas2.append(
        circule_col(
            randint(20, 700),
            randint(20, 700),
            16,
            randint(-balls_speed, balls_speed),
            randint(-balls_speed, balls_speed)
        )
    )

def update():
    Window.fill((117, 187, 253))

    for i in range(len(mainmas)):
        Window.blit(ball, (mainmas[i].x - 16, mainmas[i].y - 16))

    for i in range(len(mainmas2)):
        Window.blit(ball2, (mainmas2[i].x - 16, mainmas2[i].y - 16))

    if not button_prestsad:
        Window.blit(button, (size_x - 250, size_y - 250))

    pygame.display.flip()

while run:
    clock.tick(FPS)

    x_mouse, y_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            run = False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            if (x_mouse >= size_x - 250 and
                x_mouse <= size_x - 250 + 128 and
                y_mouse >= size_y - 250 and
                y_mouse <= size_y - 250 + 144 and
                not button_prestsad):
                    button_prestsad = True

    if (button_prestsad):
        
        for i in range(len(mainmas)):
            mainmas[i].update()

        for i in range(len(mainmas2)):
            mainmas2[i].update()

        for i in range(len(mainmas)):
            for j in range(i + 1, len(mainmas)):
                if check_circule_col(mainmas[i], mainmas[j]):
                    resolve_collision(mainmas[i], mainmas[j])

        for i in range(len(mainmas2)):
            for j in range(i + 1, len(mainmas2)):
                if check_circule_col(mainmas2[i], mainmas2[j]):
                    resolve_collision(mainmas2[i], mainmas2[j])

    update()

pygame.quit()
