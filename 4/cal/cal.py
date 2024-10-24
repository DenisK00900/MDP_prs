import pygame
from random import randint
import math
import re

pygame.init()

size_x = 512
size_y = 512

balls_count = 64
balls_speed = 400

Window = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Каркулятор")

FPS = 60

pygame.mouse.set_visible(True)
clock = pygame.time.Clock()

base = pygame.image.load("base.png").convert()
base.set_colorkey((0, 0, 0))

memory_add = pygame.image.load("memory_add.png").convert();

curpos_arrow = pygame.image.load("curpos_arrow.png").convert(); curpos_arrow.set_colorkey((255, 0, 0))

num_0 = pygame.image.load("sum1.png").convert(); num_0.set_colorkey((255, 0, 0))
num_1 = pygame.image.load("sum2.png").convert(); num_1.set_colorkey((255, 0, 0))
num_2 = pygame.image.load("sum3.png").convert(); num_2.set_colorkey((255, 0, 0))
num_3 = pygame.image.load("sum4.png").convert(); num_3.set_colorkey((255, 0, 0))
num_4 = pygame.image.load("sum5.png").convert(); num_4.set_colorkey((255, 0, 0))
num_5 = pygame.image.load("sum6.png").convert(); num_5.set_colorkey((255, 0, 0))
num_6 = pygame.image.load("sum7.png").convert(); num_6.set_colorkey((255, 0, 0))
num_7 = pygame.image.load("sum8.png").convert(); num_7.set_colorkey((255, 0, 0))
num_8 = pygame.image.load("sum9.png").convert(); num_8.set_colorkey((255, 0, 0))
num_9 = pygame.image.load("sum10.png").convert(); num_9.set_colorkey((255, 0, 0))

num_plus = pygame.image.load("sum11.png").convert(); num_plus.set_colorkey((255, 0, 0))
num_minus = pygame.image.load("sum12.png").convert(); num_minus.set_colorkey((255, 0, 0))
num_mult = pygame.image.load("sum13.png").convert(); num_mult.set_colorkey((255, 0, 0))
num_div = pygame.image.load("sum14.png").convert(); num_div.set_colorkey((255, 0, 0))

num_scp_open = pygame.image.load("sum15.png").convert(); num_scp_open.set_colorkey((255, 0, 0))
num_scp_close = pygame.image.load("sum16.png").convert(); num_scp_close.set_colorkey((255, 0, 0))
num_power = pygame.image.load("sum17.png").convert(); num_power.set_colorkey((255, 0, 0))

num_dot = pygame.image.load("sum18.png").convert(); num_dot.set_colorkey((255, 0, 0))

num_pi = pygame.image.load("sum19.png").convert(); num_pi.set_colorkey((255, 0, 0))
num_e = pygame.image.load("sum20.png").convert(); num_e.set_colorkey((255, 0, 0))

num_m1 = pygame.image.load("sum21.png").convert(); num_m1.set_colorkey((255, 0, 0))
num_m2 = pygame.image.load("sum22.png").convert(); num_m2.set_colorkey((255, 0, 0))
num_m3 = pygame.image.load("sum23.png").convert(); num_m3.set_colorkey((255, 0, 0))

num_cos = pygame.image.load("sum24.png").convert(); num_cos.set_colorkey((255, 0, 0))
num_sin = pygame.image.load("sum25.png").convert(); num_sin.set_colorkey((255, 0, 0))
num_tan = pygame.image.load("sum26.png").convert(); num_tan.set_colorkey((255, 0, 0))

num_acos = pygame.image.load("sum27.png").convert(); num_acos.set_colorkey((255, 0, 0))
num_asin = pygame.image.load("sum28.png").convert(); num_asin.set_colorkey((255, 0, 0))
num_atan = pygame.image.load("sum29.png").convert(); num_atan.set_colorkey((255, 0, 0))

num_lg = pygame.image.load("sum30.png").convert(); num_lg.set_colorkey((255, 0, 0))
num_ln = pygame.image.load("sum31.png").convert(); num_ln.set_colorkey((255, 0, 0))

current_string = ''
output_string = '';

is_memory_add = False
memory_1 = 0
memory_2 = 0
memory_3 = 0
curpos = 0
timedelta = 0

def swap_colors(surface, rect, color1, color2):
    
    for x in range(rect.x, rect.x + rect.width):
        for y in range(rect.y, rect.y + rect.height):
            current_color = surface.get_at((x, y))
            if current_color == color1:
                surface.set_at((x, y), color2)
            elif current_color == color2:
                surface.set_at((x, y), color1)

def print_string(pos, string):
    current_add = 0
    for s in string:
        if (s == "0"): Window.blit(num_0, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "1"): Window.blit(num_1, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "2"): Window.blit(num_2, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "3"): Window.blit(num_3, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "4"): Window.blit(num_4, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "5"): Window.blit(num_5, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "6"): Window.blit(num_6, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "7"): Window.blit(num_7, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "8"): Window.blit(num_8, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "9"): Window.blit(num_9, (pos[0]+current_add,pos[1])); current_add += 16

        if (s == "+"): Window.blit(num_plus, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "-"): Window.blit(num_minus, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "*"): Window.blit(num_mult, (pos[0]+current_add,pos[1])); current_add += 16
        if (s == "/"): Window.blit(num_div, (pos[0]+current_add,pos[1])); current_add += 16

        if (s == "("): Window.blit(num_scp_open, (pos[0]+current_add,pos[1])); current_add += 10
        if (s == ")"): Window.blit(num_scp_close, (pos[0]+current_add,pos[1])); current_add += 10
        if (s == "^"): Window.blit(num_power, (pos[0]+current_add,pos[1])); current_add += 16

        if (s == "."): Window.blit(num_dot, (pos[0]+current_add,pos[1])); current_add += 6

        if (s == "p"): Window.blit(num_pi, (pos[0]+current_add,pos[1])); current_add += 20
        if (s == "e"): Window.blit(num_e, (pos[0]+current_add,pos[1])); current_add += 18

        if (s == "!"): Window.blit(num_cos, (pos[0]+current_add,pos[1])); current_add += 48
        if (s == "@"): Window.blit(num_sin, (pos[0]+current_add,pos[1])); current_add += 48
        if (s == "#"): Window.blit(num_tan, (pos[0]+current_add,pos[1])); current_add += 48

        if (s == "$"): Window.blit(num_acos, (pos[0]+current_add,pos[1])); current_add += 62
        if (s == "%"): Window.blit(num_asin, (pos[0]+current_add,pos[1])); current_add += 62
        if (s == "?"): Window.blit(num_atan, (pos[0]+current_add,pos[1])); current_add += 62

        if (s == "№"): Window.blit(num_lg, (pos[0]+current_add,pos[1])); current_add += 32
        if (s == "&"): Window.blit(num_ln, (pos[0]+current_add,pos[1])); current_add += 32

        if (s == ","): Window.blit(num_m1, (pos[0]+current_add,pos[1])); current_add += 26
        if (s == "<"): Window.blit(num_m2, (pos[0]+current_add,pos[1])); current_add += 26
        if (s == ">"): Window.blit(num_m3, (pos[0]+current_add,pos[1])); current_add += 26        

def string_len(string):
    current_add = 0
    for s in string:
        if (s == "0"): current_add += 16
        if (s == "1"): current_add += 16
        if (s == "2"): current_add += 16
        if (s == "3"): current_add += 16
        if (s == "4"): current_add += 16
        if (s == "5"): current_add += 16
        if (s == "6"): current_add += 16
        if (s == "7"): current_add += 16
        if (s == "8"): current_add += 16
        if (s == "9"): current_add += 16

        if (s == "+"): current_add += 16
        if (s == "-"): current_add += 16
        if (s == "*"): current_add += 16
        if (s == "/"): current_add += 16

        if (s == "("): current_add += 10
        if (s == ")"): current_add += 10
        if (s == "^"): current_add += 16

        if (s == "."): current_add += 6

        if (s == "p"): current_add += 20
        if (s == "e"): current_add += 18

        if (s == "!"): current_add += 48
        if (s == "@"): current_add += 48
        if (s == "#"): current_add += 48

        if (s == "$"): current_add += 62
        if (s == "%"): current_add += 62
        if (s == "?"): current_add += 62

        if (s == "№"): current_add += 32
        if (s == "&"): current_add += 32

        if (s == ","): current_add += 26
        if (s == "<"): current_add += 26
        if (s == ">"): current_add += 26

    return current_add
        
def update_output_string():
    global output_string
    substr = current_string

    substr = substr.replace("^", "**")
    substr = substr.replace("p", str(math.pi))
    substr = substr.replace("e", str(math.e))

    substr = substr.replace(",", str(memory_1))
    substr = substr.replace("<", str(memory_2))
    substr = substr.replace(">", str(memory_3))

    for trig_func, func in zip(["!", "@", "#", "$", "%", "?"], 
                                ["math.cos", "math.sin", "math.tan", 
                                 "math.acos", "math.asin", "math.atan"]):
        substr = replace_trig_function(substr, trig_func, func)

    substr = replace_log_functions(substr)

    try:
        output_string = str(eval(substr))
    except Exception as e:
        output_string = ""

def replace_trig_function(expr, symbol, func):
    result = ""
    i = 0
    while i < len(expr):
        if expr[i] == symbol:
            j = i + 1

            if j < len(expr) and expr[j] == '(':
                k = j + 1
                stack = 1
                while k < len(expr) and stack > 0:
                    if expr[k] == '(':
                        stack += 1
                    elif expr[k] == ')':
                        stack -= 1
                    k += 1
                
                result += f"{func}(math.radians({expr[j + 1:k - 1]}))"
                i = k
            else:
                while j < len(expr) and (expr[j].isdigit() or expr[j] in ['+', '-', '*', '/']):
                    j += 1
        
                result += f"{func}(math.radians({expr[i + 1:j]}))"
                i = j
        else:
            result += expr[i]
            i += 1
    return result

def replace_log_functions(expr):
    result = ""
    i = 0
    while i < len(expr):
        if expr[i] == "№":
            j = i + 1
            
            if j < len(expr) and expr[j] == '(':
                k = j + 1
                stack = 1
                while k < len(expr) and stack > 0:
                    if expr[k] == '(':
                        stack += 1
                    elif expr[k] == ')':
                        stack -= 1
                    k += 1
                
                result += f"math.log10({expr[j + 1:k - 1]})"
                i = k
            else:
                while j < len(expr) and (expr[j].isdigit() or expr[j] in ['+', '-', '*', '/', '.']):
                    j += 1
                
                if j < len(expr) and expr[j] == '^':
                    result += f"math.log10({expr[i + 1:j]})"
                else:
                    result += f"math.log10({expr[i + 1:j]})"
                i = j
        elif expr[i] == "&":
            j = i + 1
            
            if j < len(expr) and expr[j] == '(':
                k = j + 1
                stack = 1
                while k < len(expr) and stack > 0:
                    if expr[k] == '(':
                        stack += 1
                    elif expr[k] == ')':
                        stack -= 1
                    k += 1
                
                result += f"math.log({expr[j + 1:k - 1]})"
                i = k
            else:
                while j < len(expr) and (expr[j].isdigit() or expr[j] in ['+', '-', '*', '/', '.']):
                    j += 1
                
                if j < len(expr) and expr[j] == '^':
                    result += f"math.log({expr[i + 1:j]})"
                else:
                    result += f"math.log({expr[i + 1:j]})"
                i = j
        else:
            result += expr[i]
            i += 1
    return result




run = True

def update():
    Window.fill((127, 127, 127))

    Window.blit(base, (0,0))

    if (is_memory_add):
        Window.blit(memory_add, (452,144))

    print_string((6,6),current_string)

    print_string((6,6+128),output_string)

    if (timedelta > 30): Window.blit(curpos_arrow, (string_len(current_string[:curpos]),6+26+4))

    pygame.display.flip()

while run:
    clock.tick(FPS)

    timedelta += 1; timedelta = timedelta%60

    x_mouse, y_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            run = False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            if (x_mouse >= 0 and x_mouse <= 64 and y_mouse >= 256 and y_mouse <= 256+64): current_string = current_string[:curpos] + "1" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 64 and x_mouse <= 128 and y_mouse >= 256 and y_mouse <= 256+64): current_string = current_string[:curpos] + "2" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 128 and x_mouse <= 192 and y_mouse >= 256 and y_mouse <= 256+64): current_string = current_string[:curpos] + "3" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 0 and x_mouse <= 64 and y_mouse >= 256+64 and y_mouse <= 256+128): current_string = current_string[:curpos] + "4" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 64 and x_mouse <= 128 and y_mouse >= 256+64 and y_mouse <= 256+128): current_string = current_string[:curpos] + "5" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 128 and x_mouse <= 192 and y_mouse >= 256+64 and y_mouse <= 256+128): current_string = current_string[:curpos] + "6" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 0 and x_mouse <= 64 and y_mouse >= 256+128 and y_mouse <= 256+192): current_string = current_string[:curpos] + "7" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 64 and x_mouse <= 128 and y_mouse >= 256+128 and y_mouse <= 256+192): current_string = current_string[:curpos] + "8" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 128 and x_mouse <= 192 and y_mouse >= 256+128 and y_mouse <= 256+192): current_string = current_string[:curpos] + "9" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 0 and x_mouse <= 64 and y_mouse >= 256+192 and y_mouse <= 256+256): current_string = ""; curpos = 0
            if (x_mouse >= 64 and x_mouse <= 128 and y_mouse >= 256+192 and y_mouse <= 256+256): current_string = current_string[:curpos] + "0" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 128 and x_mouse <= 192 and y_mouse >= 256+192 and y_mouse <= 256+256): current_string = current_string[:curpos - 1] + current_string[curpos:]; curpos -= 1

            if (x_mouse >= 192 and x_mouse <= 256 and y_mouse >= 256 and y_mouse <= 256+64): current_string = current_string[:curpos] + "(" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 256 and x_mouse <= 256+64 and y_mouse >= 256 and y_mouse <= 256+64): current_string = current_string[:curpos] + ")" + current_string[curpos:]; curpos += 1

            if (x_mouse >= 192 and x_mouse <= 256 and y_mouse >= 256+64 and y_mouse <= 256+128): current_string = current_string[:curpos] + "+" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 256 and x_mouse <= 256+64 and y_mouse >= 256+64 and y_mouse <= 256+128): current_string = current_string[:curpos] + "-" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 192 and x_mouse <= 256 and y_mouse >= 256+128 and y_mouse <= 256+192): current_string = current_string[:curpos] + "*" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 256 and x_mouse <= 256+64 and y_mouse >= 256+128 and y_mouse <= 256+192): current_string = current_string[:curpos] + "/" + current_string[curpos:]; curpos += 1
            
            if (x_mouse >= 512-128 and x_mouse <= 512-64 and y_mouse >= 256-64 and y_mouse <= 256): current_string = current_string[:curpos] + "^" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 512-64 and x_mouse <= 512 and y_mouse >= 256-64 and y_mouse <= 256): current_string = current_string[:curpos] + "." + current_string[curpos:]; curpos += 1

            if (x_mouse >= 256+64 and x_mouse <= 256+128 and y_mouse >= 256+128 and y_mouse <= 256+192): is_memory_add = not(is_memory_add)

            if (x_mouse >= 256+128 and x_mouse <= 256+192 and y_mouse >= 256+128 and y_mouse <= 256+192): current_string = current_string[:curpos] + "p" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 256+192 and x_mouse <= 256+256 and y_mouse >= 256+128 and y_mouse <= 256+192): current_string = current_string[:curpos] + "e" + current_string[curpos:]; curpos += 1

            if (x_mouse >= 256+64 and x_mouse <= 256+128 and y_mouse >= 256 and y_mouse <= 256+64): current_string = current_string[:curpos] + "!" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 256+128 and x_mouse <= 256+192 and y_mouse >= 256 and y_mouse <= 256+64): current_string = current_string[:curpos] + "@" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 256+192 and x_mouse <= 256+256 and y_mouse >= 256 and y_mouse <= 256+64): current_string = current_string[:curpos] + "#" + current_string[curpos:]; curpos += 1

            if (x_mouse >= 256+64 and x_mouse <= 256+128 and y_mouse >= 256+64 and y_mouse <= 256+128): current_string = current_string[:curpos] + "$" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 256+128 and x_mouse <= 256+192 and y_mouse >= 256+64 and y_mouse <= 256+128): current_string = current_string[:curpos] + "%" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 256+192 and x_mouse <= 256+256 and y_mouse >= 256+64 and y_mouse <= 256+128): current_string = current_string[:curpos] + "?" + current_string[curpos:]; curpos += 1

            if (x_mouse >= 256-64 and x_mouse <= 256 and y_mouse >= 512-64 and y_mouse <= 512): current_string = current_string[:curpos] + "№" + current_string[curpos:]; curpos += 1
            if (x_mouse >= 256 and x_mouse <= 256+64 and y_mouse >= 512-64 and y_mouse <= 512): current_string = current_string[:curpos] + "&" + current_string[curpos:]; curpos += 1

            if (x_mouse >= 0 and x_mouse <= 64 and y_mouse >= 256-64 and y_mouse <= 256): curpos -= 1
            if (x_mouse >= 64 and x_mouse <= 128 and y_mouse >= 256-64 and y_mouse <= 256): curpos += 1        

            if (x_mouse >= 256+64 and x_mouse <= 256+128 and y_mouse >= 512-64 and y_mouse <= 512):
                if (is_memory_add):
                    is_memory_add = False
                    memory_1 = float(output_string)
                else: current_string += ","
            if (x_mouse >= 256+128 and x_mouse <= 256+192 and y_mouse >= 512-64 and y_mouse <= 512):
                if (is_memory_add):
                    is_memory_add = False
                    memory_2 = float(output_string)
                else: current_string += "<"
            if (x_mouse >= 256+192 and x_mouse <= 256+256 and y_mouse >= 512-64 and y_mouse <= 512):
                if (is_memory_add):
                    is_memory_add = False
                    memory_3 = float(output_string)
                else: current_string += ">"

            update_output_string()
            
    update()

pygame.quit()
