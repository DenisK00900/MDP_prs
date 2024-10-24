import pygame
import sys
import time
import statistics

# Настройки
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
FONT_SIZE = 24
FPS = 60

# Символы для шифрования
RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "  # 33 буквы + пробел
ENGLISH_ALPHABET = "abcdefghijklmnopqrstuvwxyz"  # 26 букв
DIGITS = "0123456789"  # 10 цифр
PUNCTUATION = ".,!? "  # Знаки

# Объединенный набор символов
ALPHABET = RUSSIAN_ALPHABET + ENGLISH_ALPHABET + DIGITS + PUNCTUATION

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char in ALPHABET:
            index = ALPHABET.index(char)
            shifted_index = (index + shift) % len(ALPHABET)
            result.append(ALPHABET[shifted_index])
        else:
            result.append(char)  # Если символ не в алфавите, оставляем его без изменений
    return ''.join(result)

# Инициализация Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Шифр Цезаря")
font = pygame.font.Font(None, FONT_SIZE)
clock = pygame.time.Clock()

# Переменные
input_text = ""
shift = 0

A =[]

while True:
    
    for event in pygame.event.get():

        start_time = time.perf_counter_ns()

        match event.type:
        
            case pygame.QUIT: #Нажатие крестика в правом верхнем углу

                    print(statistics.mean(A))
                    
                    pygame.quit()
                    sys.exit()

            case pygame.KEYDOWN: #Нажатие клавиши
                    if event.key == pygame.K_BACKSPACE: #Если клавиша - Backspace
                        input_text = input_text[:-1]
                    else:                               #Если нет
                        input_text += event.unicode

            case pygame.MOUSEBUTTONDOWN: #Нажатие кнопки мыши
                    if event.button == 1:               #Нажатие ЛКМ
                        mouse_x, mouse_y = event.pos
                        if 50 <= mouse_y <= 150:
                            input_text = ""

            case pygame.KEYUP: #Отпустить клавишу
                    if event.key == pygame.K_UP: #Если клавища - стрелка вверх
                        shift += 1
                    elif event.key == pygame.K_DOWN: #Если клавища - стрелка вниз
                        shift -= 1

        A.append(time.perf_counter_ns()-start_time)

    # Шифрование текста
    encrypted_text = caesar_cipher(input_text, shift)

    # Отрисовка
    window.fill((255, 255, 255))
    
    input_surface = font.render(f"Ввод: {input_text}", True, (0, 0, 0))
    shift_surface = font.render(f"Сдвиг: {shift}", True, (0, 0, 0))
    output_surface = font.render(f"Зашифрованное: {encrypted_text}", True, (0, 0, 0))

    window.blit(input_surface, (50, 50))
    window.blit(shift_surface, (50, 100))
    window.blit(output_surface, (50, 150))

    pygame.display.flip()
    #clock.tick(FPS)
    #print()

