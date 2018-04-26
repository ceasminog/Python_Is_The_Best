# Импортируем библиотеку pygame
import pygame
from pygame import *
from pygame.locals import *
import time
import gameFunc

field = []
all_alive = [[], []]
type_of_input=''
print("Do you want to read from file(F) or console(C)")
type_of_input = input()
gameFunc.add_to_field(all_alive, type_of_input)

WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (690, 700)
BACKGROUND_COLOR = "#b2ff59"

pygame.init()
pygame.font.init()

def PrintF(field, generation):
    font = pygame.font.SysFont("comicsansms", 50)
    graphic_field = gameFunc.get_field(field)
    for i in range(len(field)):
        text = font.render(graphic_field[i], True, (255, 193, 7))
        screen.blit(text, [20, 20 + 40 * i])
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("Number of generation: " + str(generation), True, (255, 193, 7))
    screen.blit(text, [20, 50 + 40 * len(field)])


screen = pygame.display.set_mode(DISPLAY) # Создаем окно
pygame.display.set_caption("Game of Life") # Пишем в шапку
bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание фона
bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом
font = pygame.font.SysFont("comicsansms", 50)


mainLoop = True
o = 0
clock = pygame.time.Clock()
PrintF(field, 0)
while mainLoop:
    clock.tick(1)
    o += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
    screen.blit(bg, (0, 0))
    field = gameFunc.next_step(field, all_alive) # back end
    PrintF(field, o)
    pygame.display.update()
pygame.quit()
