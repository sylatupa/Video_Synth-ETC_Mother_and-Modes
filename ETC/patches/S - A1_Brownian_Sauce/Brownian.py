#Credits go to http://www.mediafire.com/file/5rteoppprwqcb72/flowersystem.py
#http://pygame.org/project/1755/3062
#Edits made continue to be made

import pygame
from pygame.locals import *
from math import *
import random
if True:
    print('a')
elif True:
    print('b')
def getstring(iterations):
    s = [1]
    n=0
    while n<iterations:
        rInt = random.randint(0,360)
        s.append(rInt)
        s.append('A')
        n=n+1
    return s

def main(dim):
    pygame.init()
    screen = pygame.display.set_mode((dim[0], dim[1]),pygame.FULLSCREEN)

    #F -> draw forward
    #+ -> turn right 25 degrees
    #- -> turn left 25 degrees
    #[ -> save position + angle
    #] -> restored position + angle
    
    t=pygame.time.get_ticks()

    iterations = 10000
    s = getstring(iterations)
    print(pygame.time.get_ticks()-t)
    
    t = pygame.time.get_ticks()
    pos = dim[0]/2 ,dim[1]/2
    angleG = 0
    da = -45
    angle=angleG
    print(s)
    for letter in s:
        unit =  random.randint(0,20)
        if letter == 'A' or  letter == 'B' :
            dx = cos(radians(angle))*unit
            dy = sin(radians(angle))*unit

            a = abs(angle)
            color = (230,150-(.4*a)%150,0)
            pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
            pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
            
            pos = (pos[0]+dx, pos[1]+dy)
        else:
            angle = letter
         
    print(pygame.time.get_ticks()-t)


    
    try:
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break
            pygame.display.flip()
    finally:
        pygame.quit()

if __name__ == '__main__':
    #main((1920,1080))
    main((int(1920/2),int(1080/2)))
#https://en.wikipedia.org/wiki/L-system#Examples_of_L-systems
