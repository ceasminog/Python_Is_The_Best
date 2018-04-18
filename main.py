# Импортируем библиотеку pygame
#timer.tick(60)
#timer = pygame.time.Clock()
#if e.type == KEYUP and e.key == K_LSHIFT:
#           running = False

import pygame
from pygame import *
from pygame.locals import *
import time
import gameFunc


WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (690, 700)
BACKGROUND_COLOR = "#b2ff59"
pygame.init()
pygame.font.init()

def PrintF(field, generation):
    font = pygame.font.SysFont("comicsansms", 50)
    allStr = ''
    p = len(field)
    for i in range(len(field)):
        allStr = ''
        result = [str(item) for item in field[i]]
        for j in range(len(result)):
            if result[j] =='-1':
                result[j]='R'
            if result[j] =='1':
                result[j]='F'
            if result[j] =='2':
                result[j]='S'
            if result[j] == '0':
                result[j] = '~'
        a =''.join(result)
        # allStr = allStr + a
        text = font.render(a, True, (255, 193, 7))
        screen.blit(text, [20, 20 + 40 * i])
        #text = font.render(allStr, True, (255, 193, 7))
        #screen.blit(text,(10 + text.get_width() + j * 10, 10 + text.get_height() + j ))
    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("Number of generation: " + str(generation), True, (255, 193, 7))
    screen.blit(text, [20, 50 + 40 * p])
    return allStr

#Объявляем переменные

screen = pygame.display.set_mode(DISPLAY) # Создаем окно
pygame.display.set_caption("Game of Life") # Пишем в шапку
bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом


font = pygame.font.SysFont("comicsansms", 50)
#a =['asd', 'asdefrgt' , 'sdfrgthyu']
#myString = ' '.join(a)
#text = font.render(myString , True, (255, 193, 7) )

field = []
allAlive = [[], []]
field = gameFunc.AddToFieldFromFile(allAlive)
PrintF(field, 0)
# field = gameFunc.AddToFieldFromFile(allAlive) # back end
# PrintF(field)

# font = pygame.font.Font(None, 25)
mainLoop = True
# i = 0
o = 0
clock = pygame.time.Clock()

while mainLoop:
    clock.tick(1)
    o += 1
    # text = font.render("My text", True, (255, 193, 7))
    # screen.blit(text, [250, 250])
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
    screen.blit(bg, (0, 0))
    field = gameFunc.NextStep(field, allAlive) # back end
    PrintF(field, o)
    # allStr = PrintF(field)
    font = pygame.font.SysFont("comicsansms", 20)
    #text = font.render( "Number of generation: " + str(o), True, (255, 193, 7))
    #screen.blit(text, [400, 30])
    pygame.display.update()
    #time.sleep(4)
    # text = font.render(allStr, True, (255, 193, 7))
    # screen.blit(text,
    #           (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    #text = font.render(allStr, True, (255, 193, 7))
    #screen.blit(text,
   #             (120 - text.get_width() // 2, 140 - text.get_height() // 2))
    #i = 1
pygame.quit()

