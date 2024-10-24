import pygame
from random import randint
import math
import os
import random
from collections import deque

pygame.init()

size_x = 840
size_y = 480

Window = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Морской бой")

FPS = 60

pygame.mouse.set_visible(True)
clock = pygame.time.Clock()

base = pygame.image.load("base.png").convert()
#base.set_colorkey((0, 0, 0))

vent = pygame.image.load("vent.png").convert(); vent.set_colorkey((255, 0, 0))
vent_close = pygame.image.load("vent_close.png").convert(); vent_close.set_colorkey((255, 0, 0))

decor_arrow = pygame.image.load("decor_arrow.png").convert(); decor_arrow.set_colorkey((255, 0, 0))

messadge_state = [None]*5
for i in range(5): messadge_state[i] = pygame.image.load("messadge_state_"+str(i+1)+".png").convert()

decor_arrow = pygame.image.load("decor_arrow.png").convert(); decor_arrow.set_colorkey((255, 0, 0))

map_applayer = [None]*3
#map_applayer[0] = pygame.image.load("map_base/ptr1.png").convert();
#map_applayer[1] = pygame.image.load("map_base/ptr2.png").convert();
#map_applayer[2] = pygame.image.load("map_base/ptr3.png").convert();

p4_icon =[None]*2
p4_icon[0] = pygame.image.load("ships/p4/p4_icon_1.png").convert(); p4_icon[0].set_colorkey((255, 0, 0))
p4_icon[1] = pygame.image.load("ships/p4/p4_icon_2.png").convert(); p4_icon[1].set_colorkey((255, 0, 0))

p3_icon =[None]*3
p3_icon[0] = pygame.image.load("ships/p3/p3_icon_1.png").convert(); p3_icon[0].set_colorkey((255, 0, 0))
p3_icon[1] = pygame.image.load("ships/p3/p3_icon_2.png").convert(); p3_icon[1].set_colorkey((255, 0, 0))
p3_icon[2] = pygame.image.load("ships/p3/p3_icon_3.png").convert(); p3_icon[2].set_colorkey((255, 0, 0))

p2_icon =[None]*4
p2_icon[0] = pygame.image.load("ships/p2/p2_icon_1.png").convert(); p2_icon[0].set_colorkey((255, 0, 0))
p2_icon[1] = pygame.image.load("ships/p2/p2_icon_2.png").convert(); p2_icon[1].set_colorkey((255, 0, 0))
p2_icon[2] = pygame.image.load("ships/p2/p2_icon_3.png").convert(); p2_icon[2].set_colorkey((255, 0, 0))
p2_icon[3] = pygame.image.load("ships/p2/p2_icon_4.png").convert(); p2_icon[3].set_colorkey((255, 0, 0))

p1_icon =[None]*5
p1_icon[0] = pygame.image.load("ships/p1/p1_icon_1.png").convert(); p1_icon[0].set_colorkey((255, 0, 0))
p1_icon[1] = pygame.image.load("ships/p1/p1_icon_2.png").convert(); p1_icon[1].set_colorkey((255, 0, 0))
p1_icon[2] = pygame.image.load("ships/p1/p1_icon_3.png").convert(); p1_icon[2].set_colorkey((255, 0, 0))
p1_icon[3] = pygame.image.load("ships/p1/p1_icon_4.png").convert(); p1_icon[3].set_colorkey((255, 0, 0))
p1_icon[4] = pygame.image.load("ships/p1/p1_icon_5.png").convert(); p1_icon[4].set_colorkey((255, 0, 0))

p_show_icon =[None]*4
p_show_icon[0] = pygame.image.load("count_show/p1_icon.png").convert(); p_show_icon[0].set_colorkey((255, 0, 0)); p_show_icon[0].set_alpha(191)
p_show_icon[1] = pygame.image.load("count_show/p2_icon.png").convert(); p_show_icon[1].set_colorkey((255, 0, 0)); p_show_icon[1].set_alpha(191)
p_show_icon[2] = pygame.image.load("count_show/p3_icon.png").convert(); p_show_icon[2].set_colorkey((255, 0, 0)); p_show_icon[2].set_alpha(191)
p_show_icon[3] = pygame.image.load("count_show/p4_icon.png").convert(); p_show_icon[3].set_colorkey((255, 0, 0)); p_show_icon[3].set_alpha(191)

p_show_num =[None]*4
p_show_num[0] = pygame.image.load("count_show/p_num1.png").convert(); p_show_num[0].set_colorkey((255, 0, 0)); p_show_num[0].set_alpha(191)
p_show_num[1] = pygame.image.load("count_show/p_num2.png").convert(); p_show_num[1].set_colorkey((255, 0, 0)); p_show_num[1].set_alpha(191)
p_show_num[2] = pygame.image.load("count_show/p_num3.png").convert(); p_show_num[2].set_colorkey((255, 0, 0)); p_show_num[2].set_alpha(191)
p_show_num[3] = pygame.image.load("count_show/p_num4.png").convert(); p_show_num[3].set_colorkey((255, 0, 0)); p_show_num[3].set_alpha(191)

rot_show = [None]*6
for i in range(6): rot_show[i] = pygame.image.load("rot_show/rot_show"+str(i+1)+".png").convert()

p_x = pygame.image.load("target_button/p_x.png").convert(); p_x.set_colorkey((255, 0, 0))
p_y = pygame.image.load("target_button/p_y.png").convert(); p_y.set_colorkey((255, 0, 0))
p_z = pygame.image.load("target_button/p_z.png").convert(); p_z.set_colorkey((255, 0, 0))

can_place = pygame.image.load("ships/p_can_place.png").convert()
not_place = pygame.image.load("ships/p_not_place.png").convert()
target_point = pygame.image.load("ships/p_target.png").convert(); target_point.set_colorkey((0, 0, 255))
miss = pygame.image.load("ships/p_miss.png").convert(); miss.set_colorkey((0, 0, 255))
hit = pygame.image.load("ships/p_hit.png").convert(); hit.set_colorkey((0, 0, 255))

ship_p4 = [None]*6
ship_p4[0] = pygame.image.load("ships/p4/p4_x_u.png").convert(); ship_p4[0].set_colorkey((255, 0, 0))
ship_p4[1] = pygame.image.load("ships/p4/p4_x_d.png").convert(); ship_p4[1].set_colorkey((255, 0, 0))
ship_p4[2] = pygame.image.load("ships/p4/p4_y_u.png").convert(); ship_p4[2].set_colorkey((255, 0, 0))
ship_p4[3] = pygame.image.load("ships/p4/p4_y_d.png").convert(); ship_p4[3].set_colorkey((255, 0, 0))
ship_p4[4] = [None]*4
for i in range(4):
    ship_p4[4][i] = pygame.image.load("ships/p4/p4_z_u"+str(i+1)+".png").convert(); ship_p4[4][i].set_colorkey((255, 0, 0))
ship_p4[5] = [None]*4
for i in range(4):
    ship_p4[5][i] = pygame.image.load("ships/p4/p4_z_d"+str(i+1)+".png").convert(); ship_p4[5][i].set_colorkey((255, 0, 0))

ship_p4_galf = [None]*6
ship_p4_galf[0] = pygame.image.load("ships/p4/p4_x_u_galf.png").convert(); ship_p4_galf[0].set_colorkey((255, 0, 0))
ship_p4_galf[1] = pygame.image.load("ships/p4/p4_x_d_galf.png").convert(); ship_p4_galf[1].set_colorkey((255, 0, 0))
ship_p4_galf[2] = pygame.image.load("ships/p4/p4_y_u_galf.png").convert(); ship_p4_galf[2].set_colorkey((255, 0, 0))
ship_p4_galf[3] = pygame.image.load("ships/p4/p4_y_d_galf.png").convert(); ship_p4_galf[3].set_colorkey((255, 0, 0))
ship_p4_galf[4] = [None]*4
for i in range(4):
    ship_p4_galf[4][i] = pygame.image.load("ships/p4/p4_z_u_galf"+str(i+1)+".png").convert(); ship_p4_galf[4][i].set_colorkey((255, 0, 0))
ship_p4_galf[5] = [None]*4
for i in range(4):
    ship_p4_galf[5][i] = pygame.image.load("ships/p4/p4_z_d_galf"+str(i+1)+".png").convert(); ship_p4_galf[5][i].set_colorkey((255, 0, 0))

ship_p3 = [None]*6
ship_p3[0] = pygame.image.load("ships/p3/p3_x_u.png").convert(); ship_p3[0].set_colorkey((255, 0, 0))
ship_p3[1] = pygame.image.load("ships/p3/p3_x_d.png").convert(); ship_p3[1].set_colorkey((255, 0, 0))
ship_p3[2] = pygame.image.load("ships/p3/p3_y_u.png").convert(); ship_p3[2].set_colorkey((255, 0, 0))
ship_p3[3] = pygame.image.load("ships/p3/p3_y_d.png").convert(); ship_p3[3].set_colorkey((255, 0, 0))
ship_p3[4] = [None]*3
for i in range(3):
    ship_p3[4][i] = pygame.image.load("ships/p3/p3_z_u"+str(i+1)+".png").convert(); ship_p3[4][i].set_colorkey((255, 0, 0))
ship_p3[5] = [None]*3
for i in range(3):
    ship_p3[5][i] = pygame.image.load("ships/p3/p3_z_d"+str(i+1)+".png").convert(); ship_p3[5][i].set_colorkey((255, 0, 0))

ship_p3_galf = [None]*6
ship_p3_galf[0] = pygame.image.load("ships/p3/p3_x_u_galf.png").convert(); ship_p3_galf[0].set_colorkey((255, 0, 0))
ship_p3_galf[1] = pygame.image.load("ships/p3/p3_x_d_galf.png").convert(); ship_p3_galf[1].set_colorkey((255, 0, 0))
ship_p3_galf[2] = pygame.image.load("ships/p3/p3_y_u_galf.png").convert(); ship_p3_galf[2].set_colorkey((255, 0, 0))
ship_p3_galf[3] = pygame.image.load("ships/p3/p3_y_d_galf.png").convert(); ship_p3_galf[3].set_colorkey((255, 0, 0))
ship_p3_galf[4] = [None]*3
for i in range(3):
    ship_p3_galf[4][i] = pygame.image.load("ships/p3/p3_z_u_galf"+str(i+1)+".png").convert(); ship_p3_galf[4][i].set_colorkey((255, 0, 0))
ship_p3_galf[5] = [None]*3
for i in range(3):
    ship_p3_galf[5][i] = pygame.image.load("ships/p3/p3_z_d_galf"+str(i+1)+".png").convert(); ship_p3_galf[5][i].set_colorkey((255, 0, 0))

ship_p2 = [None]*6
ship_p2[0] = pygame.image.load("ships/p2/p2_x_u.png").convert(); ship_p2[0].set_colorkey((255, 0, 0))
ship_p2[1] = pygame.image.load("ships/p2/p2_x_d.png").convert(); ship_p2[1].set_colorkey((255, 0, 0))
ship_p2[2] = pygame.image.load("ships/p2/p2_y_u.png").convert(); ship_p2[2].set_colorkey((255, 0, 0))
ship_p2[3] = pygame.image.load("ships/p2/p2_y_d.png").convert(); ship_p2[3].set_colorkey((255, 0, 0))
ship_p2[4] = [None]*2
for i in range(2):
    ship_p2[4][i] = pygame.image.load("ships/p2/p2_z_u"+str(i+1)+".png").convert(); ship_p2[4][i].set_colorkey((255, 0, 0))
ship_p2[5] = [None]*2
for i in range(2):
    ship_p2[5][i] = pygame.image.load("ships/p2/p2_z_d"+str(i+1)+".png").convert(); ship_p2[5][i].set_colorkey((255, 0, 0))

ship_p2_galf = [None]*6
ship_p2_galf[0] = pygame.image.load("ships/p2/p2_x_u_galf.png").convert(); ship_p2_galf[0].set_colorkey((255, 0, 0))
ship_p2_galf[1] = pygame.image.load("ships/p2/p2_x_d_galf.png").convert(); ship_p2_galf[1].set_colorkey((255, 0, 0))
ship_p2_galf[2] = pygame.image.load("ships/p2/p2_y_u_galf.png").convert(); ship_p2_galf[2].set_colorkey((255, 0, 0))
ship_p2_galf[3] = pygame.image.load("ships/p2/p2_y_d_galf.png").convert(); ship_p2_galf[3].set_colorkey((255, 0, 0))
ship_p2_galf[4] = [None]*2
for i in range(2):
    ship_p2_galf[4][i] = pygame.image.load("ships/p2/p2_z_u_galf"+str(i+1)+".png").convert(); ship_p2_galf[4][i].set_colorkey((255, 0, 0))
ship_p2_galf[5] = [None]*2
for i in range(2):
    ship_p2_galf[5][i] = pygame.image.load("ships/p2/p2_z_d_galf"+str(i+1)+".png").convert(); ship_p2_galf[5][i].set_colorkey((255, 0, 0))

ship_p1 = [None]*6
ship_p1[0] = pygame.image.load("ships/p1/p1_x_u.png").convert(); ship_p1[0].set_colorkey((255, 0, 0))
ship_p1[1] = pygame.image.load("ships/p1/p1_x_d.png").convert(); ship_p1[1].set_colorkey((255, 0, 0))
ship_p1[2] = pygame.image.load("ships/p1/p1_y_u.png").convert(); ship_p1[2].set_colorkey((255, 0, 0))
ship_p1[3] = pygame.image.load("ships/p1/p1_y_d.png").convert(); ship_p1[3].set_colorkey((255, 0, 0))
ship_p1[4] = [None]*1
for i in range(1):
    ship_p1[4][i] = pygame.image.load("ships/p1/p1_z_u"+str(i+1)+".png").convert(); ship_p1[4][i].set_colorkey((255, 0, 0))
ship_p1[5] = [None]*1
for i in range(1):
    ship_p1[5][i] = pygame.image.load("ships/p1/p1_z_d"+str(i+1)+".png").convert(); ship_p1[5][i].set_colorkey((255, 0, 0))

ship_p1_galf = [None]*6
ship_p1_galf[0] = pygame.image.load("ships/p1/p1_x_u_galf.png").convert(); ship_p1_galf[0].set_colorkey((255, 0, 0))
ship_p1_galf[1] = pygame.image.load("ships/p1/p1_x_d_galf.png").convert(); ship_p1_galf[1].set_colorkey((255, 0, 0))
ship_p1_galf[2] = pygame.image.load("ships/p1/p1_y_u_galf.png").convert(); ship_p1_galf[2].set_colorkey((255, 0, 0))
ship_p1_galf[3] = pygame.image.load("ships/p1/p1_y_d_galf.png").convert(); ship_p1_galf[3].set_colorkey((255, 0, 0))
ship_p1_galf[4] = [None]*1
for i in range(1):
    ship_p1_galf[4][i] = pygame.image.load("ships/p1/p1_z_u_galf"+str(i+1)+".png").convert(); ship_p1_galf[4][i].set_colorkey((255, 0, 0))
ship_p1_galf[5] = [None]*1
for i in range(1):
    ship_p1_galf[5][i] = pygame.image.load("ships/p1/p1_z_d_galf"+str(i+1)+".png").convert(); ship_p1_galf[5][i].set_colorkey((255, 0, 0))
    
def inbox(ix,iy,sx,ex,sy,ey):
    return ix >= sx and ix <= ex and iy >= sy and iy <= ey

def rotate_center(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    return rotated_image

def get_ship_adder(x,y,z,tick):
    all_tick = (x*120+y*240+z*480+tick)%(360*4)
    if (all_tick <= 360): return 4
    if (all_tick <= 720): return 6
    if (all_tick <= 1080): return 4
    if (all_tick <= 1440): return 2

def find_best_guess(bmap):
    map_depth = len(bmap)
    map_height = len(bmap[0]) if map_depth > 0 else 0
    map_width = len(bmap[0][0]) if map_height > 0 else 0

    best_guesses = {}
    total_unknown_cells = 0

    for d in range(map_depth):
        for h in range(map_height):
            for w in range(map_width):
                if bmap[d][h][w] == "empty":
                    total_unknown_cells += 1
                    score = 1

                    for dx in [-1, 1]:
                        if 0 <= w+dx < map_width and bmap[d][h][w+dx] == "hit":
                            score += 999
                    for dy in [-1, 1]:
                        if 0 <= h+dy < map_height and bmap[d][h+dy][w] == "hit":
                            score += 999
                    for dz in [-1, 1]:
                        if 0 <= d+dz < map_depth and bmap[d+dz][h][w] == "hit":
                            score += 999

                    for axis in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
                        count = 0
                        for i in range(1, 3):
                            next_d = d + axis[0]*i
                            next_h = h + axis[1]*i
                            next_w = w + axis[2]*i
                            if 0 <= next_d < map_depth and 0 <= next_h < map_height and 0 <= next_w < map_width and bmap[next_d][next_h][next_w] == "hit":
                                count += 1
                        if count >= 2:
                            score += 999999

                    best_guesses[(d, h, w)] = score

    sorted_guesses = sorted(best_guesses.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for guess, score in sorted_guesses[:(total_unknown_cells)]:
        result.append((guess, score/total_unknown_cells*100))

    return result







def randomly_place_ships(bmap):
    global stora_p1, stora_p2, stora_p3, stora_p4

    stora_p1 = 0
    stora_p2 = 0
    stora_p3 = 0
    stora_p4 = 0
    
    ship_lengths = [4] + [3] * 2 + [2] * 3 + [1] * 4
    directions = [0, 1, 2, 3, 4, 5]

    for length in ship_lengths:
        placed = False
        while not placed:
            ix = random.randint(0, 5)
            iy = random.randint(0, 5)
            iz = random.randint(0, 5)
            ir = random.choice(directions)

            if map_check_can_place_ship(bmap, length, ix, iy, iz, ir):
                place_ship_on_map(bmap, length, ix, iy, iz, ir)
                placed = True
                
def delete_ship_from_map(bmap, pos, stack):
    global stora_p1, stora_p2, stora_p3, stora_p4, ship_addet_stack
    
    count = 0
    for x in range(6):
        for y in range(6):
            for z in range(6):
                if (bmap[x][y][z] != "empty"):
                    if (bmap[x][y][z]["start"] == pos):
                        count += 1
                        bmap[x][y][z] = "empty"

    ship_addet_stack = stack[:-1]

    if (count == 1): stora_p1 += 1
    if (count == 2): stora_p2 += 1
    if (count == 3): stora_p3 += 1
    if (count == 4): stora_p4 += 1

def place_ship_on_map(bmap, length, ix, iy, iz, ir):
    global ship_addet_stack
    
    for i in range(length):
        if ir == 0:
            x, y, z = ix + i, iy, iz
        elif ir == 1:
            x, y, z = ix - i, iy, iz
        elif ir == 2:
            x, y, z = ix, iy + i, iz
        elif ir == 3:
            x, y, z = ix, iy - i, iz
        elif ir == 4:
            x, y, z = ix, iy, iz + i
        elif ir == 5:
            x, y, z = ix, iy, iz - i
        
        bmap[x][y][z] = {
            "start": (ix, iy, iz),
            "direction": ir,
            "length": length,
            "part": i + 1
        }

    ship_addet_stack.append((ix, iy, iz))

def map_check_can_place_ship(bmap, length, ix, iy, iz, ir):
    map_depth = len(bmap)
    map_height = len(bmap[0]) if map_depth > 0 else 0
    map_width = len(bmap[0][0]) if map_height > 0 else 0

    for i in range(length):
        if ir == 0:
            x, y, z = ix + i, iy, iz
        elif ir == 1:
            x, y, z = ix - i, iy, iz
        elif ir == 2:
            x, y, z = ix, iy + i, iz
        elif ir == 3:
            x, y, z = ix, iy - i, iz
        elif ir == 4:
            x, y, z = ix, iy, iz + i
        elif ir == 5:
            x, y, z = ix, iy, iz - i
        else:
            return False

        if (x < 0 or x >= map_width or
            y < 0 or y >= map_height or
            z < 0 or z >= map_depth):
            return False

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if (0 <= x+dx < map_width and
                        0 <= y+dy < map_height and
                        0 <= z+dz < map_depth and
                        bmap[x+dx][y+dy][z+dz] != "empty"):
                        return False

    return True

def update_neighbors_on_destroyed(bmap_upper):
    directions = [
        (dx, dy, dz) 
        for dx in [-1, 0, 1] 
        for dy in [-1, 0, 1] 
        for dz in [-1, 0, 1] 
        if (dx, dy, dz) != (0, 0, 0)
    ]
    
    size = len(bmap_upper)
    
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if bmap_upper[x][y][z] == "destroyed":
                    for dx, dy, dz in directions:
                        nx, ny, nz = x + dx, y + dy, z + dz
                        if 0 <= nx < size and 0 <= ny < size and 0 <= nz < size:
                            if bmap_upper[nx][ny][nz] == "empty":
                                bmap_upper[nx][ny][nz] = "miss"
                                
def map_find_destr(bmap, bmap_upper, tp):
    global p4_save_1, p3_save_1, p2_save_1, p1_save_1, p4_save_2, p3_save_2, p2_save_2, p1_save_2
    
    ships = {}

    for x in range(len(bmap)):
        for y in range(len(bmap[0])):
            for z in range(len(bmap[0][0])):
                cell = bmap[x][y][z]
                if isinstance(cell, dict):
                    ship_id = (cell['start'], cell['length'])
                    if ship_id not in ships:
                        ships[ship_id] = []
                    ships[ship_id].append((x, y, z))

    for ship_id, parts in ships.items():
        all_hit = True
        for (x, y, z) in parts:
            if bmap_upper[x][y][z] != "hit":
                all_hit = False
                break
            
        if all_hit:
            for (x, y, z) in parts:
                bmap_upper[x][y][z] = "destroyed"

            if (tp == 1):
                if ship_id[1] == 4: p4_save_1 -= 1
                if ship_id[1] == 3: p3_save_1 -= 1
                if ship_id[1] == 2: p2_save_1 -= 1
                if ship_id[1] == 1: p1_save_1 -= 1
            if (tp == 2):
                if ship_id[1] == 4: p4_save_2 -= 1
                if ship_id[1] == 3: p3_save_2 -= 1
                if ship_id[1] == 2: p2_save_2 -= 1
                if ship_id[1] == 1: p1_save_2 -= 1

            
def map_get_affected_cells(bmap, length, ix, iy, iz, ir):
    map_depth = len(bmap)
    map_height = len(bmap[0]) if map_depth > 0 else 0
    map_width = len(bmap[0][0]) if map_height > 0 else 0

    affected_cells = []

    for i in range(length):
        if ir == 0:
            x, y, z = ix + i, iy, iz
        elif ir == 1:
            x, y, z = ix - i, iy, iz
        elif ir == 2:
            x, y, z = ix, iy + i, iz
        elif ir == 3:
            x, y, z = ix, iy - i, iz
        elif ir == 4:
            x, y, z = ix, iy, iz + i
        elif ir == 5:
            x, y, z = ix, iy, iz - i
        else:
            return []

        if (x < 0 or x >= map_width or
            y < 0 or y >= map_height or
            z < 0 or z >= map_depth):
                return affected_cells
        

        affected_cells.append((x, y, z))

    return affected_cells

class anim:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.type = "non"
        self.frames = []
        self.framerate = 60

        self.curr_frame = 0
        self.curr_subtime = 0

        self.level = 0
        self.target_level = 0

        self.app_layer = None
        self.app_layer_a = 0

    def __init__(self, ix, iy, itype, path, count, ifr):
        self.x = ix
        self.y = iy
        self.type = itype
        self.load(path,count)
        self.framerate = ifr

        self.curr_frame = 0
        self.curr_subtime = 0

        self.level = 0
        self.target_level = 0

        self.app_layer = None
        self.app_layer_a = 0

    def load(self, path_to_frames, frames_count):
        self.frames = []
        for i in range(1, frames_count + 1):
            frame_filename = f"{path_to_frames}{i}.png"
            try:
                frame = pygame.image.load(frame_filename).convert_alpha()
                self.frames.append(frame)
            except pygame.error as e:
                print(f"Unable to load frame {frame_filename}: {e}")

    def set_alpha(self, alp):
        for i in self.frames:
            i.set_alpha(alp)

    def flip(self):
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.flip(self.frames[i],1,0)
        
    def update(self):

        if (self.type == "cirlur"):
            self.curr_subtime += 1

            if (self.curr_subtime >= self.framerate):
                self.curr_subtime = 0

                curr_frame += 1

                if (curr_frame >= len(frames)):
                    curr_frame = 0

        elif (self.type == "burst"):
            
            if (self.target_level == 1):
                self.level = 0

                self.curr_subtime += 1

                if (self.curr_subtime >= self.framerate):
                    self.curr_subtime = 0

                    if (self.curr_frame < len(self.frames)-1):
                        self.curr_frame += 1

                    else:
                        self.level = 1
                        self.target_level = 0
                        self.curr_frame = 0
            
        elif (self.type == "target"):
            if (self.level != self.target_level):

                if (self.level < self.target_level):
                    self.curr_subtime += 1

                    if (self.curr_subtime >= self.framerate):
                        self.curr_subtime = 0

                        self.curr_frame += 1

                else:
                    self.curr_subtime += 1
                    
                    if (self.curr_subtime >= self.framerate):
                        self.curr_subtime = 0

                        self.curr_frame -= 1

            self.level = self.curr_frame

        elif (self.type == "tumbler"):
            
            if (self.level != self.target_level):

                if (self.level < self.target_level):
                    self.curr_subtime += 1

                    if (self.curr_subtime >= self.framerate):
                        self.curr_subtime = 0

                        self.curr_frame += 1

                        if (self.curr_frame > len(self.frames)-1): self.curr_frame = 0

                        self.level += 1

                else:
                    self.curr_subtime += 1
                    
                    if (self.curr_subtime >= self.framerate):
                        self.curr_subtime = 0

                        self.curr_frame -= 1

                        if (self.curr_frame < 0): self.curr_frame = len(self.frames)-1

                        self.level -= 1

                        

    def blit(self):
        if self.app_layer is not None:
            combined_surface = pygame.Surface((self.frames[self.curr_frame].get_width(), 
                                                self.frames[self.curr_frame].get_height()), 
                                               pygame.SRCALPHA)
            
            current_frame = self.frames[self.curr_frame]
            
            combined_surface.blit(current_frame, (0, 0))

            app_layer_with_alpha = self.app_layer.copy()
            app_layer_with_alpha.set_alpha(self.app_layer_a)

            combined_surface.blit(app_layer_with_alpha, (0, 0))

            Window.blit(combined_surface, (self.x, self.y))
        else:
            Window.blit(self.frames[self.curr_frame], (self.x, self.y))

    def update_and_blit(self):
        self.update()
        self.blit()


vent_curr_angle = [randint(0,359),randint(0,359),randint(0,359),randint(0,359)]
vent_curr_speed = [randint(40,50)/1000.0,randint(20,40)/1000.0,randint(10,30)/1000.0,randint(0,20)/1000.0]

lift_up_button_1 = anim(22,168,"target","lift_up_button\lift_up_button",3,2)
lift_down_button_1 = anim(22,192,"target","lift_down_button\lift_down_button",3,2)
lift_up_button_2 = anim(434,168,"target","lift_up_button\lift_up_button",3,2)
lift_down_button_2 = anim(434,192,"target","lift_down_button\lift_down_button",3,2)

lift_1_val = 0
lift_2_val = 0

lift_show_1 = anim(48,122,"target","lift_card\lift_card",31,3); lift_show_1.curr_frame = 30; lift_show_1.level = 30; lift_show_1.target_level = 30;
lift_show_2 = anim(460,122,"target","lift_card\lift_card",31,3); lift_show_2.curr_frame = 30; lift_show_2.level = 30; lift_show_2.target_level = 30;

map_base_1 = anim(94,92,"tumbler","map_base\map_base",8,4)
map_base_2 = anim(506,92,"tumbler","map_base\map_base",8,4)

map_applayer_timer = 0
map_base_1.app_layer_a = 15
map_base_2.app_layer_a = 15

placer_close = anim(0,0,"target","placer_close\placer_close",24,2)

placer_prv = anim(4,50,"target","placer_button\prv",3,2)
placer_nxt = anim(24,50,"target","placer_button\p_nxt",3,2)
placer_rot = anim(64,50,"target","placer_button\p_rot",3,2)
placer_del = anim(116,50,"target","placer_button\del",3,2)
placer_add = anim(136,50,"target","placer_button\p_add",3,2)

curr_state = 0
curr_state_timer = 180
curr_state_subtimer = 0

curr_ship = 1
stora_p4 = 1
stora_p3 = 2
stora_p2 = 3
stora_p1 = 4

p4_save_1 = 1
p3_save_1 = 2
p2_save_1 = 3
p1_save_1 = 4

p4_save_2 = 1
p3_save_2 = 2
p2_save_2 = 3
p1_save_2 = 4

icon_subtimer = 0

rot_subtimer = 0

p_x_subtimer = 0
p_y_subtimer = 0
p_z_subtimer = 0

place_rot = 0

is_fire = False

c3_subtimer = 0

arrow_current_angle = -135
arrow_current_speed = 0.5
arrow_current_target = -135
arrow_current_timer = 0


target_num_x = anim(182,12,"target","target_pos\p_num",11,1)
target_num_y = anim(228,12,"target","target_pos\p_num",11,1)
target_num_z = anim(274,12,"target","target_pos\p_num",11,1)

target_d_1 = anim(164,52,"target","target_button\p_button_d",3,2)
target_u_1 = anim(184,52,"target","target_button\p_button_u",3,2)

target_d_2 = anim(210,52,"target","target_button\p_button_d",3,2)
target_u_2 = anim(230,52,"target","target_button\p_button_u",3,2)

target_d_3 = anim(256,52,"target","target_button\p_button_d",3,2)
target_u_3 = anim(276,52,"target","target_button\p_button_u",3,2)

start_button = anim(310,18,"target","start_button\start_button",13,5)

random_button = anim(28,306,"target","random_placer\p_random_button",5,2)
random_close = anim(28,306,"target","random_placer\p_random_close",9,2)

placer_screen = anim(14,6,"target","placer_close\placer_screen",20,4)

fire_button_up = anim(310,18,"target","start_button\p_fire_button",13,5)
fire_button_press = anim(310,18,"target","start_button\p_fire_button_press",4,2)

expl = anim(0,0,"burst","explosion\expl",60,1)
bullet = anim(0,0,"burst","bullet\p_bullet",10,2)

expl2 = anim(0,0,"burst","explosion\expl",60,1)
bullet2 = anim(0,0,"burst","bullet\p_bullet",10,2)
bullet2.flip()

decor_lamp_group_1 = [None]*4
for i in range(4): decor_lamp_group_1[i] = anim(0,0,"target","decor_lamp\p_red\decor_lamp",2,1)
decor_lamp_group_1[0].x = 372
decor_lamp_group_1[0].y = 6
decor_lamp_group_1[0].target_level = randint(0,1)
decor_lamp_group_1[1].x = 386
decor_lamp_group_1[1].y = 6
decor_lamp_group_1[1].target_level = randint(0,1)
decor_lamp_group_1[2].x = 372
decor_lamp_group_1[2].y = 20
decor_lamp_group_1[2].target_level = randint(0,1)
decor_lamp_group_1[3].x = 386
decor_lamp_group_1[3].y = 20
decor_lamp_group_1[3].target_level = randint(0,1)

decor_lamp_group_1_timer = [0]*4

decor_lamp_group_2 = [None]*3

decor_lamp_group_2[0] = anim(0,0,"target","decor_lamp\green\decor_lamp",2,1)
decor_lamp_group_2[1] = anim(0,0,"target","decor_lamp\yellow\decor_lamp",2,1)
decor_lamp_group_2[2] = anim(0,0,"target","decor_lamp\p_red\decor_lamp",2,1)

decor_lamp_group_2[0].x = 30
decor_lamp_group_2[0].y = 110
decor_lamp_group_2[0].target_level = randint(0,1)
decor_lamp_group_2[1].x = 30
decor_lamp_group_2[1].y = 126
decor_lamp_group_2[1].target_level = randint(0,1)
decor_lamp_group_2[2].x = 30
decor_lamp_group_2[2].y = 140
decor_lamp_group_2[2].target_level = randint(0,1)

decor_lamp_group_2_timer = [0]*3

decor_lamp_group_3 = [None]*3

decor_lamp_group_3[0] = anim(0,0,"target","decor_lamp\green\decor_lamp",2,1)
decor_lamp_group_3[1] = anim(0,0,"target","decor_lamp\yellow\decor_lamp",2,1)
decor_lamp_group_3[2] = anim(0,0,"target","decor_lamp\p_red\decor_lamp",2,1)

decor_lamp_group_3[0].x = 442
decor_lamp_group_3[0].y = 110
decor_lamp_group_3[0].target_level = randint(0,1)
decor_lamp_group_3[1].x = 442
decor_lamp_group_3[1].y = 126
decor_lamp_group_3[1].target_level = randint(0,1)
decor_lamp_group_3[2].x = 442
decor_lamp_group_3[2].y = 140
decor_lamp_group_3[2].target_level = randint(0,1)

decor_lamp_group_3_timer = [0]*3

decor_lamp_group_4 = [None]*4

decor_lamp_group_4[0] = anim(0,0,"target","decor_lamp\p_blue\decor_lamp",2,1)
decor_lamp_group_4[1] = anim(0,0,"target","decor_lamp\p_blue\decor_lamp",2,1)
decor_lamp_group_4[2] = anim(0,0,"target","decor_lamp\p_blue\decor_lamp",2,1)
decor_lamp_group_4[3] = anim(0,0,"target","decor_lamp\green\decor_lamp",2,1)

decor_lamp_group_4[0].x = 16
decor_lamp_group_4[0].y = 394
decor_lamp_group_4[0].target_level = randint(0,1)
decor_lamp_group_4[1].x = 30
decor_lamp_group_4[1].y = 394
decor_lamp_group_4[1].target_level = randint(0,1)
decor_lamp_group_4[2].x = 44
decor_lamp_group_4[2].y = 394
decor_lamp_group_4[2].target_level = randint(0,1)
decor_lamp_group_4[3].x = 58
decor_lamp_group_4[3].y = 394
decor_lamp_group_4[3].target_level = randint(0,1)

decor_lamp_group_4_timer = [0]*4

decor_lamp_group_5 = [None]*3

decor_lamp_group_5[0] = anim(0,0,"target","decor_lamp\yellow\decor_lamp",2,1)
decor_lamp_group_5[1] = anim(0,0,"target","decor_lamp\yellow\decor_lamp",2,1)
decor_lamp_group_5[2] = anim(0,0,"target","decor_lamp\yellow\decor_lamp",2,1)

decor_lamp_group_5[0].x = 716
decor_lamp_group_5[0].y = 458
decor_lamp_group_5[0].target_level = randint(0,1)
decor_lamp_group_5[1].x = 730
decor_lamp_group_5[1].y = 458
decor_lamp_group_5[1].target_level = randint(0,1)
decor_lamp_group_5[2].x = 744
decor_lamp_group_5[2].y = 458
decor_lamp_group_5[2].target_level = randint(0,1)

decor_lamp_group_5_timer = [0]*3

decor_bar_1 = anim(670,56,"target","decor_bar\p_decor_bar",8,6)
decor_bar_2 = anim(670,70,"target","decor_bar\p_decor_bar",8,6)
decor_bar_3 = anim(670,84,"target","decor_bar\p_decor_bar",8,6)

decor_bar_1.target_level = randint(0,7)
decor_bar_2.target_level = randint(0,7)
decor_bar_3.target_level = randint(0,7)

decor_bar_1_timer = 0
decor_bar_2_timer = 0
decor_bar_3_timer = 0

curr_map_x = 0
curr_map_y = 0
curr_map_z = 0

fire_map_x = 0
fire_map_y = 0
fire_map_z = 0

last_map_1_level = 0
last_map_2_level = 0

adder_values = {
    0: (0, 1.0),
    1: (1, 0.75),
    2: (3, 0.50),
    3: (6, 0.25),
    4: (0, 0.00),
    5: (-6, 0.25),
    6: (-3, 0.50),
    7: (-1, 0.75)
}
have_reached_half_1 = False
last_lift_1 = 0
have_reached_half_2 = False
last_lift_2 = 0

ship_adder_tick = 0

ship_addet_stack = []

hyperjump_addpos = 0

fire_over = False

act = None

count_show_timer = [0]*8
for i in range(8):
    count_show_timer[i] = i*120 + randint(-240,240)

map_1 = [[[0 for _ in range(6)] for _ in range(6)] for _ in range(6)]
map_2 = [[[0 for _ in range(6)] for _ in range(6)] for _ in range(6)]

map_1_upper = [[[0 for _ in range(6)] for _ in range(6)] for _ in range(6)]
map_2_upper = [[[0 for _ in range(6)] for _ in range(6)] for _ in range(6)]

for x in range(6):
    for y in range(6):
        for z in range(6):
            map_1[x][y][z] = "empty"
            map_2[x][y][z] = "empty"
            map_1_upper[x][y][z] = "empty"
            map_2_upper[x][y][z] = "empty"

def update_arrow():
    global arrow_current_target, arrow_current_angle, arrow_current_speed, arrow_current_timer

    arrow_current_target = max(-135, min(135, arrow_current_target))

    angle_difference = (arrow_current_target - arrow_current_angle) % 360

    if angle_difference < 90:
        speed = arrow_current_speed * max((angle_difference / 90.0), 0.005)
    else:
        speed = arrow_current_speed

    if angle_difference > 180:
        angle_difference -= 360

    if abs(angle_difference) < speed:
        arrow_current_angle = arrow_current_target
    else:
        if angle_difference > 0:
            arrow_current_angle += speed
        else:
            arrow_current_angle -= speed

    arrow_current_angle = max(-135, min(135, arrow_current_angle))

    rotated_arrow = pygame.transform.rotate(decor_arrow, -arrow_current_angle)
    arrow_rect = rotated_arrow.get_rect(center=(800.5, 440.5))

    Window.blit(rotated_arrow, arrow_rect.topleft)

    if arrow_current_timer <= 0:
        if randint(0, 31) == 0:
            if randint(0, 3) == 0:

                arrow_current_target = randint(100, 135)
                arrow_current_speed = randint(8, 22) / 10.0
                arrow_current_timer = randint(400, 1200)
            else:
                arrow_current_target = randint(-135, 100)
                arrow_current_speed = randint(2, 12) / 10.0
                arrow_current_timer = randint(400, 1200)
    else:

        if angle_difference < 30:
            arrow_current_timer -= 8
        elif angle_difference < 60:
            arrow_current_timer -= 4
        elif angle_difference < 90:
            arrow_current_timer -= 2
        else:
            arrow_current_timer -= 1
    
def draw_ship_placement(vec, curr_ship, storage, map_1, curr_map_x, curr_map_y, curr_map_z, place_rot, adder_1_alt, adder_1_pos):
    if storage[curr_ship] > 0:
        if map_check_can_place_ship(map_1, curr_ship, curr_map_x, curr_map_y, curr_map_z, place_rot):
            can_place.set_alpha(adder_1_alt * 255)
            Window.blit(can_place, (94 + 40 * vec[0], 104 + 40 * vec[1] - adder_1_pos))
        else:
            not_place.set_alpha(adder_1_alt * 255)
            Window.blit(not_place, (94 + 40 * vec[0], 104 + 40 * vec[1] - adder_1_pos))

def get_adder_pos_count_ships(i):
    if (i < 120): return -2
    if (i < 240): return 0
    if (i < 360): return 2
    if (i < 480): return 0
    return 0
        
def draw_count_ships(start_x, start_y, side):
    global p4_save_1, p3_save_1, p2_save_1, p1_save_1, p4_save_2, p3_save_2, p2_save_2, p1_save_2, count_show_timer

    for i in range(8):
        count_show_timer[i] = (count_show_timer[i] + 0.25)%480

    if side == 1:
        saves = [p4_save_1, p3_save_1, p2_save_1, p1_save_1]
    else:
        saves = [p4_save_2, p3_save_2, p2_save_2, p1_save_2]

    non_zero_indices = [i for i, value in enumerate(saves) if value > 0]
    count = len(non_zero_indices)

    if count == 0:
        return

    total_width = count * p_show_icon[0].get_width() + (count - 1) * 4
    start_draw_x = start_x - total_width // 2

    for i in non_zero_indices:
        Window.blit(p_show_icon[3-i], (start_draw_x + (i * (p_show_icon[i].get_width() + 4)), start_y + get_adder_pos_count_ships(count_show_timer[(side-1)*4+i])))
        if (saves[i]-1 >= 0): Window.blit(p_show_num[saves[i]-1], (start_draw_x + (i * (p_show_icon[i].get_width() + 4)), start_y + 18 + get_adder_pos_count_ships(count_show_timer[(side-1)*4+i])))

run = True

def update():
    global curr_state_timer, curr_state_subtimer, icon_subtimer, rot_subtimer, p_x_subtimer, p_y_subtimer, p_z_subtimer, have_reached_half_1, last_lift_1, have_reached_half_2, last_lift_2, ship_adder, ship_adder_tick
    global curr_state, hyperjump_addpos, is_fire, map_1_upper, map_2_upper, fire_over, act, lift_1_val, lift_2_val, c3_subtimer, last_map_1_level, last_map_2_level, map_applayer_timer
    global p4_save_1, p3_save_1, p2_save_1, p1_save_1, p4_save_2, p3_save_2, p2_save_2, p1_save_2, decor_bar_1_timer, decor_bar_2_timer, decor_bar_3_timer
    
    Window.fill((127, 127, 127))

    Window.blit(base, (0,0))

    for i in range(4):
        vent_curr_angle[i] = (vent_curr_angle[i] + vent_curr_speed[i] * 360) % 360

    for i in range(4):
        rotated_vent = rotate_center(vent, vent_curr_angle[i])
        center_x = 490 + (i * 44)
        center_y = 62
        rect = rotated_vent.get_rect(center=(center_x+16, center_y+16))
        Window.blit(rotated_vent, rect.topleft)

        if (randint(0,9) == 0):
            if (vent_curr_speed[i] <= 0.00):
                vent_curr_speed[i] += randint(1,3)/1000.0
            elif (vent_curr_speed[i] >= 0.10):
                vent_curr_speed[i] -= randint(1,3)/1000.0
            else:
                if (randint(0,1) == 0):
                    vent_curr_speed[i] += randint(1,3)/1000.0
                else:
                    vent_curr_speed[i] -= randint(1,3)/1000.0

    Window.blit(vent_close, (488,60))
    Window.blit(vent_close, (532,60))
    Window.blit(vent_close, (576,60))
    Window.blit(vent_close, (620,60))

    for i in range(4):

        if (decor_lamp_group_1_timer[i] == 0):
            if (randint(0,127) == 0):
                decor_lamp_group_1_timer[i] = randint(20,600)
                if (decor_lamp_group_1[i].target_level == 1): decor_lamp_group_1[i].target_level = 0
                else: decor_lamp_group_1[i].target_level = 1
                
        else: decor_lamp_group_1_timer[i] -= 1

        decor_lamp_group_1[i].update_and_blit()

    for i in range(3):

        if (decor_lamp_group_2_timer[i] == 0):
            if (randint(0,127) == 0):
                decor_lamp_group_2_timer[i] = randint(20,600)
                if (decor_lamp_group_2[i].target_level == 1): decor_lamp_group_2[i].target_level = 0
                else: decor_lamp_group_2[i].target_level = 1
                
        else: decor_lamp_group_2_timer[i] -= 1

        decor_lamp_group_2[i].update_and_blit()

    for i in range(3):

        if (decor_lamp_group_3_timer[i] == 0):
            if (randint(0,127) == 0):
                decor_lamp_group_3_timer[i] = randint(20,600)
                if (decor_lamp_group_3[i].target_level == 1): decor_lamp_group_3[i].target_level = 0
                else: decor_lamp_group_3[i].target_level = 1
                
        else: decor_lamp_group_3_timer[i] -= 1

        decor_lamp_group_3[i].update_and_blit()        

    for i in range(4):

        if (decor_lamp_group_4_timer[i] == 0):
            if (randint(0,127) == 0):
                decor_lamp_group_4_timer[i] = randint(20,600)
                if (decor_lamp_group_4[i].target_level == 1): decor_lamp_group_4[i].target_level = 0
                else: decor_lamp_group_4[i].target_level = 1
                
        else: decor_lamp_group_4_timer[i] -= 1

        decor_lamp_group_4[i].update_and_blit()            

    for i in range(3):

        if (decor_lamp_group_5_timer[i] == 0):
            if (randint(0,127) == 0):
                decor_lamp_group_5_timer[i] = randint(20,600)
                if (decor_lamp_group_5[i].target_level == 1): decor_lamp_group_5[i].target_level = 0
                else: decor_lamp_group_5[i].target_level = 1
                
        else: decor_lamp_group_5_timer[i] -= 1

        decor_lamp_group_5[i].update_and_blit()

    if (decor_bar_1_timer == 0):
        if (randint(0,63) == 0):
            decor_bar_1_timer = randint(120,480)
            decor_bar_1.target_level = randint(0,7)
    else: decor_bar_1_timer -= 1
    if (decor_bar_2_timer == 0):
        if (randint(0,63) == 0):
            decor_bar_2_timer = randint(120,480)
            decor_bar_2.target_level = randint(0,7)
    else: decor_bar_2_timer -= 1
    if (decor_bar_3_timer == 0):
        if (randint(0,63) == 0):
            decor_bar_3_timer = randint(120,480)
            decor_bar_3.target_level = randint(0,7)
    else: decor_bar_3_timer -= 1
            
    decor_bar_1.update_and_blit()
    decor_bar_2.update_and_blit()
    decor_bar_3.update_and_blit()
        
    if (hyperjump_addpos > 0): hyperjump_addpos -= 0.25

    lift_up_button_1.update_and_blit()
    lift_down_button_1.update_and_blit()
    lift_up_button_2.update_and_blit()
    lift_down_button_2.update_and_blit()

    lift_show_1.update_and_blit()
    lift_show_2.update_and_blit()

    map_applayer_timer = (map_applayer_timer+1)%3

    #map_base_1.app_layer =  map_applayer[map_applayer_timer]
    #map_base_2.app_layer =  map_applayer[map_applayer_timer]

    map_base_1.update_and_blit()
    if (curr_state >= 2): map_base_2.update_and_blit()
    
    if (curr_state_timer < 120 and curr_state_timer//30%2 == 0 and curr_state_subtimer%2 == 0):
        if (curr_state == 0): Window.blit(messadge_state[0], (532,6))
        if (curr_state == 2): Window.blit(messadge_state[1], (532,6))
        if (curr_state == 3): Window.blit(messadge_state[2], (532,6))
        if (curr_state == 4): Window.blit(messadge_state[3], (532,6))
        if (curr_state == 5): Window.blit(messadge_state[4], (532,6))
        
    if (curr_state_timer > 0): curr_state_timer -= 1

    if (randint(0,511) == 0): curr_state_subtimer = randint(30,240)
    if (curr_state_subtimer > 0): curr_state_subtimer -= 1

    placer_prv.update_and_blit()
    placer_nxt.update_and_blit()
    placer_rot.update_and_blit()
    placer_del.update_and_blit()
    placer_add.update_and_blit()

    update_arrow()

    if (icon_subtimer%2 == 0):
        if (curr_ship == 4):
            Window.blit(p4_icon[1-stora_p4], (6,6))
        if (curr_ship == 3):
            Window.blit(p3_icon[2-stora_p3], (6,6))
        if (curr_ship == 2):
            Window.blit(p2_icon[3-stora_p2], (6,6))
        if (curr_ship == 1):
            Window.blit(p1_icon[4-stora_p1], (6,6))
            
    if (randint(0,511) == 0): icon_subtimer = randint(30,240)
    if (icon_subtimer > 0): icon_subtimer -= 1

    if (randint(0,511) == 0): rot_subtimer = randint(30,240)
    if (rot_subtimer > 0): rot_subtimer -= 1

    if (randint(0,511) == 0): p_x_subtimer = randint(30,240)
    if (p_x_subtimer > 0): p_x_subtimer -= 1

    if (randint(0,511) == 0): p_y_subtimer = randint(30,240)
    if (p_y_subtimer > 0): p_y_subtimer -= 1

    if (randint(0,511) == 0): p_z_subtimer = randint(30,240)
    if (p_z_subtimer > 0): p_z_subtimer -= 1

    if (rot_subtimer%2 == 0): Window.blit(rot_show[place_rot], (88,50))
    
    placer_close.update_and_blit()

    if (p_x_subtimer%2 == 0):
        Window.blit(p_x, (166,6))
        target_num_x.update_and_blit()

    if (p_y_subtimer%2 == 0):
        Window.blit(p_y, (212,6))
        target_num_y.update_and_blit()  

    if (p_z_subtimer%2 == 0):
        Window.blit(p_z, (258,6))
        target_num_z.update_and_blit()
        
    target_d_1.update_and_blit()
    target_u_1.update_and_blit()
    target_d_2.update_and_blit()
    target_u_2.update_and_blit()
    target_d_3.update_and_blit()
    target_u_3.update_and_blit()

    adder_1_pos = adder_values[map_base_1.curr_frame][0]
    adder_1_alt = adder_values[map_base_1.curr_frame][1]

    adder_2_pos = adder_values[map_base_2.curr_frame][0]
    adder_2_alt = adder_values[map_base_2.curr_frame][1]
    
    if (map_base_1.curr_frame == 4): have_reached_half_1 = True
    if (map_base_2.curr_frame == 4): have_reached_half_2 = True

    if (curr_state >= 2):
        draw_count_ships(217,378,1)
        draw_count_ships(629,378,2)

    def get_map_lift(mp):
        if (-mp.level < 4): return 0
        if (-mp.level >= 4 and -mp.level < 12): return 1
        if (-mp.level >= 12 and -mp.level < 20): return 2
        if (-mp.level >= 20 and -mp.level < 28): return 3
        if (-mp.level >= 28 and -mp.level < 36): return 4
        if (-mp.level >= 36): return 5

    #print(lift_1_val,get_map_lift(map_base_1))

    placing_ship = map_get_affected_cells(map_1,curr_ship,curr_map_x,curr_map_y,curr_map_z,place_rot)
        
    for vec in placing_ship:

                if (vec[2] == get_map_lift(map_base_1)):
                    
                    if (curr_ship == 4 and stora_p4 > 0):
                        if (map_check_can_place_ship(map_1,4,curr_map_x,curr_map_y,curr_map_z,place_rot)):
                            can_place.set_alpha(adder_1_alt*255)
                            Window.blit(can_place, (94+40*vec[0],104+40*vec[1]-adder_1_pos))
                        else:
                            not_place.set_alpha(adder_1_alt*255)
                            Window.blit(not_place, (94+40*vec[0],104+40*vec[1]-adder_1_pos))

                    if (curr_ship == 3 and stora_p3 > 0):
                        if (map_check_can_place_ship(map_1,3,curr_map_x,curr_map_y,curr_map_z,place_rot)):
                            can_place.set_alpha(adder_1_alt*255)
                            Window.blit(can_place, (94+40*vec[0],104+40*vec[1]-adder_1_pos))
                        else:
                            not_place.set_alpha(adder_1_alt*255)
                            Window.blit(not_place, (94+40*vec[0],104+40*vec[1]-adder_1_pos))

                    if (curr_ship == 2 and stora_p2 > 0):
                        if (map_check_can_place_ship(map_1,2,curr_map_x,curr_map_y,curr_map_z,place_rot)):
                            can_place.set_alpha(adder_1_alt*255)
                            Window.blit(can_place, (94+40*vec[0],104+40*vec[1]-adder_1_pos))
                        else:
                            not_place.set_alpha(adder_1_alt*255)
                            Window.blit(not_place, (94+40*vec[0],104+40*vec[1]-adder_1_pos))

                    if (curr_ship == 1 and stora_p1 > 0):
                        if (map_check_can_place_ship(map_1,1,curr_map_x,curr_map_y,curr_map_z,place_rot)):
                            can_place.set_alpha(adder_1_alt*255)
                            Window.blit(can_place, (94+40*vec[0],104+40*vec[1]-adder_1_pos))
                        else:
                            not_place.set_alpha(adder_1_alt*255)
                            Window.blit(not_place, (94+40*vec[0],104+40*vec[1]-adder_1_pos))
                            
                            
    ship_adder_tick = (ship_adder_tick + 1)%1440

    def update_map_hits():

        if (bullet.curr_frame == 9): bullet.update()
        else: bullet.update_and_blit()
        expl.update_and_blit()
                
        for x in range(6):
            for y in range(6):
                current_map = map_2_upper[x][y]
                lift_val = get_map_lift(map_base_2)
                data = current_map[lift_val]

                if (data == "miss"):
                    miss.set_alpha(adder_2_alt * 0.5 * 255)
                    Window.blit(miss, (506 + 40 * x, 104 + 40 * y - adder_2_pos))                
                if (data == "hit" or data == "destroyed"):
                    hit.set_alpha(adder_2_alt * 0.5 * 255)
                    Window.blit(hit, (506 + 40 * x, 104 + 40 * y - adder_2_pos))

                if ((x,y,lift_val) == (curr_map_x,curr_map_y,curr_map_z)):
                    target_point.set_alpha(adder_2_alt * 0.5 * 255)
                    Window.blit(target_point, (506 + 40 * x, 104 + 40 * y - adder_2_pos))
                    
                    bullet.x = 506 + 40 * fire_map_x - 80
                    bullet.y = 104 + 40 * fire_map_y - adder_2_pos  - 80

                    pt = 1
                    if (expl.curr_frame > 50): pt = (expl.curr_frame-50)/10.0
                    expl.set_alpha(adder_2_alt  * 255 * 1-pt)
                    expl.x = 506 + 40 * fire_map_x
                    expl.y = 104 + 40 * fire_map_y - adder_2_pos

        for x in range(6):
            for y in range(6):
                current_map = map_1_upper[x][y]
                lift_val = get_map_lift(map_base_1)
                data = current_map[lift_val]

                if (data != "empty"):
                    if (data == "miss"):
                        miss.set_alpha(adder_1_alt * 0.5 * 255)
                        Window.blit(miss, (94 + 40 * x, 104 + 40 * y - adder_1_pos))                
                    if (data == "hit" or data == "destroyed"):
                        hit.set_alpha(adder_1_alt * 0.5 * 255)
                        Window.blit(hit, (94 + 40 * x, 104 + 40 * y - adder_1_pos))

    def weighted_random_choice(data):
        elements = [item[0] for item in data]
        weights = [item[1] for item in data]

        selected_element = random.choices(elements, weights=weights, k=1)[0]
        return selected_element

    bullet.set_alpha((bullet.curr_frame/len(bullet.frames)) * adder_2_alt  * 255)
    bullet2.set_alpha((bullet2.curr_frame/len(bullet2.frames)) * adder_1_alt  * 255)

    if (expl.target_level == 1): bullet.set_alpha(0)
    if (expl2.target_level == 1): bullet2.set_alpha(0)
    
                                

    def draw_ship(ship_data, alpha, position):
        ship_length = ship_data["length"]
        direction = ship_data["direction"]
        part = ship_data.get("part", 0)

        if (curr_state == 0):
            if (ship_length == 4): ship_galf = ship_p4_galf
            if (ship_length == 3): ship_galf = ship_p3_galf
            if (ship_length == 2): ship_galf = ship_p2_galf
            if (ship_length == 1): ship_galf = ship_p1_galf
        else:
            if (ship_length == 4): ship_galf = ship_p4
            if (ship_length == 3): ship_galf = ship_p3
            if (ship_length == 2): ship_galf = ship_p2
            if (ship_length == 1): ship_galf = ship_p1
            
        if direction < 4:
            sprite_group = ship_galf[direction]
            sprite = sprite_group
            sprite.set_alpha(alpha * (1-hyperjump_addpos/15.0) * 255)
            if direction == 0:
                position = (position[0] - hyperjump_addpos**2, position[1])
            elif direction == 1:
                position = (position[0] + hyperjump_addpos**2 - 120 if ship_length == 4 else position[0] + hyperjump_addpos**2 + 40 - (40 * (ship_length)), position[1])
            elif direction == 2:
                position = (position[0], position[1] + hyperjump_addpos**2)
            elif direction == 3:
                position = (position[0], position[1] - hyperjump_addpos**2 - (120 if ship_length == 4 else (80 if ship_length == 3 else (40 if ship_length == 2 else 0))))
        else:
            sprite_group = ship_galf[4 if direction == 4 else 5]
            sprite = sprite_group[(ship_length-1)-(part-1)] if direction == 4 else sprite_group[(part-1)]
            sprite.set_alpha(alpha * (1-hyperjump_addpos/15.0) * 255)

            if direction == 4:
                position = (position[0], position[1] + hyperjump_addpos**2)
            else:
                position = (position[0], position[1] - hyperjump_addpos**2)

        Window.blit(sprite, (position[0], position[1]))

    if (curr_state != 1):
        for x in range(6):
            for y in range(6):
                current_map = map_1[x][y]
                lift_val = get_map_lift(map_base_1)
                ship_data = current_map[lift_val]

                if ship_data != "empty":
                    if ship_data["start"] == (x, y, lift_val):
                        position = (94 + 40 * x, 104 + 40 * y - get_ship_adder(x, y, lift_val, ship_adder_tick) - adder_1_pos)
                        draw_ship(ship_data, adder_1_alt, position)
                    else:
                        if (ship_data["direction"] >= 4):
                            position = (94 + 40 * x, 104 + 40 * y - get_ship_adder(x, y, lift_val, ship_adder_tick) - adder_1_pos)
                            draw_ship(ship_data, adder_1_alt, position)

        if (stora_p4 == 0 and stora_p3 == 0  and stora_p2 == 0  and stora_p1 == 0 and curr_state == 0): start_button.target_level = 12
        else: start_button.target_level = 0;

    if (curr_state >= 4):

        for x in range(6):
            for y in range(6):
                current_map = map_2[x][y]
                lift_val = get_map_lift(map_base_2)
                ship_data = current_map[lift_val]

                if ship_data != "empty":
                    if ship_data["start"] == (x, y, lift_val):
                        position = (506 + 40 * x, 104 + 40 * y - get_ship_adder(x, y, lift_val, ship_adder_tick) - adder_2_pos)
                        draw_ship(ship_data, adder_2_alt, position)
                    else:
                        if (ship_data["direction"] >= 4):
                            position = (506 + 40 * x, 104 + 40 * y - get_ship_adder(x, y, lift_val, ship_adder_tick) - adder_2_pos)
                            draw_ship(ship_data, adder_2_alt, position)
        
        update_map_hits()


    if (curr_state == 3):
        
        if (act == None):
            act = (weighted_random_choice(find_best_guess(map_1_upper)))
            lift_1_val = act[2]
            lift_show_1.target_level = 30-lift_1_val*6;
            map_base_1.target_level = lift_1_val*-8
            bullet2.target_level = 1
            c3_subtimer = randint(60,90)

        if (lift_show_1.level == 30-lift_1_val*6):

            if (c3_subtimer > 0): c3_subtimer -= 1
            else:
                
                bullet2.x = 94 + 40 * act[0]
                bullet2.y = 104 + 40 * act[1] - adder_1_pos  - 80

                pt = 1
                if (expl2.curr_frame > 50): pt = (expl2.curr_frame-50)/10.0
                expl2.set_alpha(adder_1_alt  * 255 * 1-pt)
                expl2.x = 94 + 40 * act[0]
                expl2.y = 104 + 40 * act[1] - adder_1_pos
                            
                if (bullet2.curr_frame == 9): bullet2.update()
                else: bullet2.update_and_blit()
                expl2.update_and_blit()

                if (bullet2.level == 1):

                    expl2.target_level = 1

                    bullet2.target_level = 0
            
                    if (expl2.level == 1):

                        expl2.target_level = 0
                        expl2.level = 0
                        bullet2.level = 0

                        if (map_1[act[0]][act[1]][act[2]] == "empty"):
                                map_1_upper[act[0]][act[1]][act[2]] = "miss"
                                curr_state = 2
                                is_fire = False
                                bullet.target_level = 0
                                expl.target_level = 0
                                act = None
                        else:
                                map_1_upper[act[0]][act[1]][act[2]] = "hit"
                                act = None
                                map_find_destr(map_1,map_1_upper,1)
                                update_neighbors_on_destroyed(map_1_upper)
                                
                                if (p4_save_1 == 0 and p3_save_1 == 0 and p2_save_1 == 0 and p1_save_1 == 0):
                                    curr_state = 5

        update_map_hits()

                        
    if (curr_state == 2):

        if (bullet.level):
            expl.target_level = 1
            bullet.target_level = 0
            bullet.level = 0
                        
        if (expl.level):

            expl.target_level = 0
            expl.level = 0
            
            if (map_2[fire_map_x][fire_map_y][fire_map_z] == "empty"):
                map_2_upper[fire_map_x][fire_map_y][fire_map_z] = "miss"
                curr_state = 3
            else:
                map_2_upper[fire_map_x][fire_map_y][fire_map_z] = "hit"
                is_fire = False
                map_find_destr(map_2,map_2_upper,2)
                update_neighbors_on_destroyed(map_2_upper)

                if (p4_save_2 == 0 and p3_save_2 == 0 and p2_save_2 == 0 and p1_save_2 == 0):
                    curr_state = 4
            
        
        update_map_hits()
                        
    start_button.update_and_blit()

    if (curr_state == 0):
        random_button.update_and_blit()
    else:
        random_close.update_and_blit()

    if (placer_close.level == 23):
        placer_screen.target_level = 19
        placer_screen.update_and_blit()
        if (placer_screen.level == 19 and curr_state == 1):
            curr_state_timer = 180
            curr_state = randint(2,3)
            hyperjump_addpos = 15
    else:
        placer_screen.update()

    if (fire_button_up.target_level != 12 and hyperjump_addpos == 0 and curr_state == 2):
        fire_button_up.target_level = 12

    if (fire_button_up.level != 12 and fire_button_up.target_level == 12):
        fire_button_up.update_and_blit()
    elif (fire_button_up.target_level == 12):
        fire_button_press.update_and_blit()
        
        
    pygame.display.flip()



while run:
    clock.tick(FPS)

    x_mouse, y_mouse = pygame.mouse.get_pos()

    #print(bullet.curr_frame,bullet2.curr_frame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            run = False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            
            if   (inbox(x_mouse,y_mouse,22,39,168,185) and curr_state != 3):
                lift_up_button_1.target_level = 1

                last_lift_1 = lift_1_val
                
                lift_1_val += 1
                if (lift_1_val > 5): lift_1_val = 5

                lift_show_1.target_level = 30-lift_1_val*6;

                map_base_1.target_level = lift_1_val*-8


            elif (inbox(x_mouse,y_mouse,22,39,192,209) and curr_state != 3):
                lift_down_button_1.target_level = 1

                last_lift_1 = lift_1_val
                
                lift_1_val -= 1

                if (lift_1_val < 0): lift_1_val = 0

                lift_show_1.target_level = 30-lift_1_val*6;

                map_base_1.target_level = lift_1_val*-8


            elif (inbox(x_mouse,y_mouse,434,451,168,185)):
                lift_up_button_2.target_level = 1

                last_lift_2 = lift_2_val
                
                lift_2_val += 1

                if (lift_2_val > 5): lift_2_val = 5

                lift_show_2.target_level = 30-lift_2_val*6;

                map_base_2.target_level = lift_2_val*-8

            elif (inbox(x_mouse,y_mouse,434,451,192,209)):
                lift_down_button_2.target_level = 1

                last_lift_2 = lift_2_val
                
                lift_2_val -= 1

                if (lift_2_val < 0): lift_2_val = 0

                lift_show_2.target_level = 30-lift_2_val*6;

                map_base_2.target_level = lift_2_val*-8


            elif (curr_state == 0 and inbox(x_mouse,y_mouse,4,21,50,71)):
                placer_prv.target_level = 1

                curr_ship -= 1
                if (curr_ship < 1): curr_ship = 4

            elif (curr_state == 0 and inbox(x_mouse,y_mouse,24,41,50,71)):
                placer_nxt.target_level = 1

                curr_ship += 1
                if (curr_ship > 4): curr_ship = 1

            elif (curr_state == 0 and inbox(x_mouse,y_mouse,64,81,50,71)):
                placer_rot.target_level = 1
                place_rot += 1
                if (place_rot > 5): place_rot = 0

            elif (curr_state == 0 and inbox(x_mouse,y_mouse,116,133,50,71)):
                placer_del.target_level = 1

                if (ship_addet_stack != []):
                    delete_ship_from_map(map_1,ship_addet_stack[len(ship_addet_stack)-1],ship_addet_stack)

            elif (curr_state == 0 and inbox(x_mouse,y_mouse,136,153,50,71)):
                placer_add.target_level = 1

                if (curr_ship == 4 and stora_p4 > 0):
                    if (map_check_can_place_ship(map_1,4,curr_map_x,curr_map_y,curr_map_z,place_rot)):
                        stora_p4 -= 1
                        place_ship_on_map(map_1,4,curr_map_x,curr_map_y,curr_map_z,place_rot)


                if (curr_ship == 3 and stora_p3 > 0):
                    if (map_check_can_place_ship(map_1,3,curr_map_x,curr_map_y,curr_map_z,place_rot)):
                        stora_p3 -= 1
                        place_ship_on_map(map_1,3,curr_map_x,curr_map_y,curr_map_z,place_rot)


                if (curr_ship == 2 and stora_p2 > 0):
                    if (map_check_can_place_ship(map_1,2,curr_map_x,curr_map_y,curr_map_z,place_rot)):
                        stora_p2 -= 1
                        place_ship_on_map(map_1,2,curr_map_x,curr_map_y,curr_map_z,place_rot)


                if (curr_ship == 1 and stora_p1 > 0):
                    if (map_check_can_place_ship(map_1,1,curr_map_x,curr_map_y,curr_map_z,place_rot)):
                        stora_p1 -= 1
                        place_ship_on_map(map_1,1,curr_map_x,curr_map_y,curr_map_z,place_rot)
                        

            elif (inbox(x_mouse,y_mouse,164,181,52,73)):
                target_d_1.target_level = 1

                curr_map_x -= 1
                if (curr_map_x < 0): curr_map_x = 0

                target_num_x.target_level = curr_map_x*2

            elif (inbox(x_mouse,y_mouse,184,201,52,73)):
                target_u_1.target_level = 1

                curr_map_x += 1
                if (curr_map_x > 5): curr_map_x = 5

                target_num_x.target_level = curr_map_x*2

            elif (inbox(x_mouse,y_mouse,210,227,52,73)):
                target_d_2.target_level = 1

                curr_map_y -= 1
                if (curr_map_y < 0): curr_map_y = 0

                target_num_y.target_level = curr_map_y*2

            elif (inbox(x_mouse,y_mouse,230,247,52,73)):
                target_u_2.target_level = 1

                curr_map_y += 1
                if (curr_map_y > 5): curr_map_y = 5

                target_num_y.target_level = curr_map_y*2

            elif (inbox(x_mouse,y_mouse,256,273,52,73)):
                target_d_3.target_level = 1

                curr_map_z -= 1
                if (curr_map_z < 0): curr_map_z = 0

                target_num_z.target_level = curr_map_z*2

            elif (inbox(x_mouse,y_mouse,276,293,52,73)):
                target_u_3.target_level = 1

                curr_map_z += 1
                if (curr_map_z > 5): curr_map_z = 5

                target_num_z.target_level = curr_map_z*2

            elif (stora_p4 == 0 and stora_p3 == 0  and stora_p2 == 0  and stora_p1 == 0 and curr_state == 0 and inbox(x_mouse,y_mouse,316,350,18,52)):
                curr_state = 1
                placer_close.target_level = 23
                random_close.target_level = 8

                randomly_place_ships(map_2)

                curr_map_x = 0
                curr_map_y = 0
                curr_map_z = 0

                target_num_x.target_level = curr_map_x*2
                target_num_y.target_level = curr_map_y*2
                target_num_z.target_level = curr_map_z*2

            elif (curr_state == 2 and not(is_fire) and inbox(x_mouse,y_mouse,316,350,18,52)):
                fire_button_press.target_level = 3;

                bullet.target_level = 1

                is_fire = True

                fire_map_x = curr_map_x
                fire_map_y = curr_map_y
                fire_map_z = curr_map_z

            elif (inbox(x_mouse,y_mouse,28,69,306,357)):
                random_button.target_level = 3

                while (ship_addet_stack != []):
                    delete_ship_from_map(map_1,ship_addet_stack[len(ship_addet_stack)-1],ship_addet_stack)

                randomly_place_ships(map_1)
                

        if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
            
            lift_up_button_1.target_level = 0
            lift_down_button_1.target_level = 0
            lift_up_button_2.target_level = 0
            lift_down_button_2.target_level = 0

            placer_prv.target_level = 0
            placer_nxt.target_level = 0
            placer_rot.target_level = 0
            placer_del.target_level = 0
            placer_add.target_level = 0

            target_d_1.target_level = 0
            target_u_1.target_level = 0
            target_d_2.target_level = 0
            target_u_2.target_level = 0
            target_d_3.target_level = 0
            target_u_3.target_level = 0

            random_button.target_level = 0
            fire_button_press.target_level = 0;
            
    update()

pygame.quit()
