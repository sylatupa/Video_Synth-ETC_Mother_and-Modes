#https://en.wikipedia.org/wiki/L-system#Examples_of_L-systems
#Credits go to http://www.mediafire.com/file/5rteoppprwqcb72/flowersystem.py
#http://pygame.org/project/1755/3062
#Edits made continue to be made

import os
import pygame
import random

#from pygame.locals import *
from math import *


speedList = [random.randrange(-1,1)+.1 for i in range(0,20)]
yList = [random.randrange(-50,770) for i in range(0,20)]
widthList = [random.randrange(20,200) for i in range(0,20)]
countList = [i for i in range(0,20)]
xden = 1
yden = 1
trigger = False
def getstring(iterations):
    s = [1]
    n=0
    while n<iterations:
        rInt = random.randint(0,360)
        s.append(rInt)
        s.append('A')
        n=n+1
    return s


def setup(screen, etc) :
    pass

count = 0
pos = 500,500
angleG = 0
da = -45
angle=angleG
iterations = 11
s = getstring(iterations)
 
def draw(screen, etc) :
    global trigger, yList, widthList, countList, speedList, xden, yden, count, pos, angleG, da, angle,s
    
    color = etc.color_picker() #on knob4
    
    if yden != (int(etc.knob1 * 19) + 1) :
        yden = (int(etc.knob1 * 19) + 1)
        speedList = [random.randrange(-2,2)+.1 for i in range(0,20)]
        yList = [random.randrange(-50,770) for i in range(0,20)]
        widthList = [random.randrange(20,200) for i in range(0,20)]
    
    if xden != (int(etc.knob2 * 19) + 1) :
        xden = (int(etc.knob2 * 19) + 1)
        speedList = [random.randrange(-2,2)+.1 for i in range(0,20)]
        yList = [random.randrange(-50,770) for i in range(0,20)]
        widthList = [random.randrange(20,200) for i in range(0,20)]
    ''' 
    for i in range (0,yden) :
        
        y0 = yList[i]
        for j in range (0,xden) :
            
            width = widthList[i]
            y1 = y0 + (etc.audio_in[j+i] / 500)
            countList[i] = countList[i] + speedList[i]
            modSpeed = countList[i]%(1280+width*2)
            x = (j * (width/5)) + (modSpeed-width)
            pygame.draw.line(screen, color, [x, y1], [x, y0], int(etc.knob3*100+1))
    '''
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
 
    #F -> draw forward
    #+ -> turn right 25 degrees
    #- -> turn left 25 degrees
    #[ -> save position + angle
    #] -> restored position + angle
    #pos = dim[0]/2 ,dim[1]/2
    #iterations = 11
    #s = getstring(iterations)
 
    maxCount = len(s)
    t = pygame.time.get_ticks()

    '''
    for letter in s:
        t = pygame.time.get_ticks()
        unit =  random.randint(0,30)
        if letter == 'A' or  letter == 'B' :
            dx = cos(radians(angle))*unit
            dy = sin(radians(angle))*unit

            a = abs(angle)
            color = (230,150-(.4*a)%150,0)
            pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
            #pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
            
            pos = (pos[0]+dx, pos[1]+dy)
        else:
            angle = letter
        '''
    if True:
        print(count, ' ' , maxCount)
        if count >= maxCount:
            pos = random.randint(0,1000),random.randint(0,500)
            count = 0
            iterations = 11
            s = getstring(iterations)
            
        else:
            count = count + 1
        letter = s[count]
        unit =  random.randint(0,50)
        if letter == 'A' or  letter == 'B' :
            dx = cos(radians(angle))*unit
            dy = sin(radians(angle))*unit

            a = abs(angle)
            color = (230,150-(.4*a)%150,0)
            pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
            #pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
            
            pos = (pos[0]+dx, pos[1]+dy)
        else:
            angle = letter
         
    trigger = False

