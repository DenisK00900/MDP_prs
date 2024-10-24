import pygame
from random import randint
import math

pygame.init()

size_x = 800
size_y = 800

Window = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Спираль Архимеда")

FPS = 60

pygame.mouse.set_visible(True)
clock = pygame.time.Clock()

base = pygame.image.load("base.png").convert()
base.set_colorkey((255, 0, 0))



a = 1.9
b = 0.15

run = True

def draw_spiral(surface, a, b, max_angle):
    center_x = size_x // 2
    center_y = size_y // 2
    prev_x = center_x
    prev_y = center_y

    for angle in range(0, max_angle, 1):
        theta = math.radians(angle)
        r = a + b * angle
        x = center_x + r * math.cos(theta)
        y = center_y + r * math.sin(theta)

        pygame.draw.line(surface, (255, 0, 0), (prev_x, prev_y), (x, y), 2)
        prev_x, prev_y = x, y

def update():
    Window.fill((255, 255, 255))

    Window.blit(base,(0,0))
    
    draw_spiral(Window, a, b, 360 * 20)
    pygame.display.flip()

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            run = False
            
    update()

pygame.quit()
