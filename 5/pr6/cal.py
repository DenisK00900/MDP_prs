import pygame
from random import randint
import math

pygame.init()

size_x = 400
size_y = 400

Window = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Круговой график")

FPS = 60

pygame.mouse.set_visible(True)
clock = pygame.time.Clock()

run = True

A = [5, 10, 15, 30, 40]
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]

def draw():
    total = sum(A)
    angles = [(value / total) * 360 for value in A]
    start_angle = 0

    for i in range(len(A)):
        end_angle = start_angle + angles[i]

        for angle in range(int(start_angle), int(end_angle)):
            pygame.draw.line(Window, colors[i], 
                             (200, 200), 
                             (200 + 100 * math.cos(angle * math.pi / 180), 
                              200 + 100 * math.sin(angle * math.pi / 180)), 
                             3)

        effect_color = tuple(int(c * 0.5) for c in colors[i])

        for angle in range(int(start_angle), int(end_angle)):
            if angle > 0 and angle < 180:
                pygame.draw.line(Window, effect_color, 
                                 (200 + 100 * math.cos(angle * math.pi / 180), 
                                  200 + 100 * math.sin(angle * math.pi / 180)), 
                                 (200 + 100 * math.cos(angle * math.pi / 180), 
                                  200 + 100 * math.sin(angle * math.pi / 180) + 20), 
                                 3)

        start_angle = end_angle

def update():
    Window.fill((0, 0, 0))

    draw()
    
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
