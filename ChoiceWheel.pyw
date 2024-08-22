import pygame
from pygame import gfxdraw
import sys
import random
import math

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def displayresult(result):
    fanfare.play()
    textsurface = font.render(result, True, (0, 255, 0))
    textrect = textsurface.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(textsurface, textrect)
    pygame.display.update()

decisionlist = ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4']
probabilities = [0.50, 0.25, 0.20, 0.05]

pygame.init()
font = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 28)
screen = pygame.display.set_mode((400, 400))
degree = 0
elapsedtime = 1
end = random.randint(200, 560)
spin1 = pygame.mixer.Sound("spin1.wav")
spin2 = pygame.mixer.Sound("spin2.wav")
spin3 = pygame.mixer.Sound("spin3.wav")
fanfare = pygame.mixer.Sound("fanfare.wav")
x = 1
resultlist = []
cx = cy = r = 200
dividers = len(decisionlist)
radconvert = math.pi / 180
divvies = int(360 / dividers)

def weighted_random_choice(choices, weights):
    return random.choices(choices, weights)[0]

for _ in range(len(decisionlist)):
    choice = weighted_random_choice(decisionlist, probabilities)
    resultlist.append(choice)
    index = decisionlist.index(choice)
    decisionlist.pop(index)
    probabilities.pop(index)

print(resultlist)

while x == 1:
    pygame.display.flip()
    screen.fill([255, 255, 255])
    
    surf = pygame.Surface((100, 100))
    surf.fill((255, 255, 255))
    surf.set_colorkey((255, 255, 255))

    surf = pygame.image.load('cool.png').convert_alpha()
    where = 180, 10

    blittedRect = screen.blit(surf, where)
    screen.fill([255, 255, 255])
    pygame.draw.circle(screen, (0, 0, 0), (cx, cy), r, 3)
    for i in range(dividers):
        gfxdraw.pie(screen, cx, cy, r, i * divvies, divvies, (0, 0, 0))
    i = 1
    iters = range(1, dividers * 2, 2)
    for i in iters:
        textChoice = font2.render(resultlist[iters.index(i)], False, (0, 0, 0))
        textwidth = textChoice.get_rect().width
        textheight = textChoice.get_rect().height
        textChoice = pygame.transform.rotate(textChoice, (i - (2 * i)) * (360 / (dividers * 2)))
        textwidth = textChoice.get_rect().width
        textheight = textChoice.get_rect().height
        screen.blit(textChoice, (
            (cx - (textwidth / 2))
            + ((r - 100) * math.cos(((i * (360 / (dividers * 2)))) * radconvert)),
            (cy - (textheight / 2))
            + ((r - 100) * math.sin(((i * (360 / (dividers * 2)))) * radconvert))
        ))
        textChoice = ''
    oldCenter = blittedRect.center

    rotatedSurf = pygame.transform.rotate(surf, degree)

    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter

    screen.blit(rotatedSurf, rotRect)

    degree -= 2
    if degree == -360:
        degree = 0

    pygame.display.flip()

    quit()

    if elapsedtime == 1:
        spin1.play(-1)
        elapsedtime += 1
    elif elapsedtime < end / 6:
        pygame.time.wait(2)
        elapsedtime += 1
    elif elapsedtime < end / 4:
        pygame.time.wait(5)
        elapsedtime += 1
    elif elapsedtime < end / 2:
        pygame.time.wait(10)
        elapsedtime += 1
    elif elapsedtime < end / 1.5:
        pygame.time.wait(15)
        elapsedtime += 1
    elif elapsedtime < end / 1.2:
        spin3.stop()
        spin3.play()
        pygame.time.wait(30)
        elapsedtime += 1
    elif elapsedtime < end / 1.1:
        spin3.stop()
        spin3.play()
        pygame.time.wait(70)
        elapsedtime += 1
    elif elapsedtime < end / 1.05:
        spin1.fadeout(1000)
        spin3.stop()
        spin3.play()
        pygame.time.wait(150)
        elapsedtime += 1
    elif elapsedtime < end:
        spin1.stop()
        spin3.stop()
        spin3.play()
        pygame.time.wait(200)
        elapsedtime += 1
    elif elapsedtime == end:
        spin1.stop()
        degCheck = degree
        degCheck = (-1 * degCheck) - 90
        if degCheck < 0:
            degCheck = degCheck + 360
        x = 2
        while x == 2:
            screen.blit(rotatedSurf, rotRect)
            for i in range(len(resultlist)):
                if degCheck > i * (360 / len(resultlist)) and degCheck < (i + 1) * (360 / len(resultlist)):
                    x = 3
                    result = resultlist[i]
                    displayresult(result)
                    while x == 3:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x = 1
                                elapsedtime = 1
                                end = random.randint(200, 560)
                                break
                        quit()
                elif degCheck % (360 / len(resultlist)) == 0:
                    x = 3
                    displayresult('Spinning Again')
                    pygame.time.wait(1)
                    x = 1
                    elapsedtime = 1
                    end = random.randint(200, 560)
                    while x == 3:
                        quit()
            quit()
