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
'''
brownian string
def getstring(iterations):
    s = [1]
    n=0
    while n<iterations:
        rInt = random.randint(0,360)
        s.append(rInt)
        s.append('A')
        n=n+1
    return s
'''
'''
flower string
def getstring(iterations):

    s = ['X']
    #s = ['-','F','X']
    for i in range(iterations):
        #X -> F-[[X]+X]+F[+FX]-X
        #F-FF
        X_make = ['F', '-', '[', '[', 'X', ']', '+', 'X', ']', '+', 'F', '[', '+', 'F', 'X', ']', '-', 'X']
        F_make = ['F','F']
        j = 0
        while j<len(s):
            if s[j] == 'X':
                s.pop(j)#replace X with our X_make list
                for item in X_make[::-1]:
                    s.insert(j,item)
                j+=17#bump j up to skip over added items
            elif s[j] == 'F':
                s.pop(j)
                for item in F_make[::-1]:
                    s.insert(j,item)
                j+=1
            j+=1
    return s
'''
'''
random walk
'''
'''
def getstring(iterations):
    s = ['A']
    n=0
    while n<iterations:
        rInt = random.randint(0,3)
        if rInt == 0:
            s.append('A')
        elif rInt == 1:
            s.append('-')
            s.append('-')
            s.append('A')
        elif rInt == '2':
            s.append('-')
            s.append('A')
            n = n+1
            
        elif rInt == '3':
            s.append('-')
            s.append('-')
            s.append('-')
            s.append('A')
        n=n+1
    return s
'''
'''
chaos modeling
'''
def getstring(iterations,generation_rate=.002):
    s = dict()
    n=0
    s['rate1_w_increase'] = []
    s['Generation'] = []
    s['adjustableRate'] = []
    s['ExperimentRed'] = []    
    s['ExperimentBlue'] = []    
    s['ExperimentWhite'] = []        
    while n<iterations:
        s['Generation'].append(n)
        s['rate1_w_increase'].append(n * generation_rate + 2)
        if n == 0:
            s['adjustableRate'].append(0.125 * s['rate1_w_increase'][n] * (1-0.125))
            s['ExperimentRed'].append(.99)    
            s['ExperimentBlue'].append(.025)    
            s['ExperimentWhite'].append(.025)                
        else:
            s['adjustableRate'].append(s['adjustableRate'][n-1] * s['rate1_w_increase'][n] * s['adjustableRate'][n-1])
            s['ExperimentRed'].append(s['ExperimentRed'][n-1] * s['rate1_w_increase'][n] * (1-s['ExperimentRed'][n-1]))
            s['ExperimentBlue'].append(s['ExperimentBlue'][n-1] * s['rate1_w_increase'][n] * (1-s['ExperimentBlue'][n-1]))
            s['ExperimentWhite'].append(s['ExperimentWhite'][n-1] * 3.0 * (1-s['ExperimentWhite'][n-1]))
        n=n+1
    return s


def setup(screen, etc) :
    pass
'''
brownian
'''
count = 0
pos = 500,500
angleG = 0
da = -45
angle=angleG
iterations = 11

'''
flower
'''
iterations = 7 #flower
iterations = 3 #flower
iterations = 111 #random walk
unit = 2.5
angle = -70
da = 20
saved_angles = []
saved_poses = []

'''
random walk
'''
iterations = 9000
unit =  5
angleG = 0
da = -45
angle=angleG

s = getstring(iterations)
maxCount = len(s)
maxCount = iterations
def draw(screen, etc) :
    etc.auto_clear = False
    global trigger, yList, widthList, countList, speedList, xden, yden, count, pos, angleG, da, angle,s,saved_angles,saved_poses,maxCount,iterations
    
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
    osciliscope
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
    #t = pygame.time.get_ticks()
 
 
    '''
    osciliscope
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
    for n in range(count,count+30):
        if count >= iterations-1:
            #pos = random.randint(0,1000),random.randint(0,500)
            count = 0
            iterations = random.randint(0,444)
            s = getstring(iterations, random.randint(0,1)/1)
            maxCount = iterations
        else:
            count = count + 1

        n = count
        '''
        brownian
        
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
        '''
        '''
        flower
        #F -> draw forward
        #+ -> turn right 25 degrees
        #- -> turn left 25 degrees
        #[ -> save position + angle
        #] -> restored position + angle
        '''
        '''
        flower
        
        if letter == 'F':
            dx = cos(radians(angle))*unit
            dy = sin(radians(angle))*unit

            a = abs(angle)
            color = (230,150-(.4*a)%150,0)
            pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
            #pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
            
            pos = (pos[0]+dx, pos[1]+dy)
            
        elif letter == '+':
            angle += da
        elif letter == '-':
            angle -= da
        elif letter == '[':
            saved_poses.append(pos)
            saved_angles.append(angle)
        elif letter == ']':
            pos = saved_poses.pop()
            angle = saved_angles.pop()
        '''
        
        '''
        random walk
        
        if letter == 'A' or  letter == 'B' :
            dx = cos(radians(angle))*unit
            dy = sin(radians(angle))*unit

            a = abs(angle)
            color = (230,150-(.4*a)%150,0)
            pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
            pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
            
            pos = (pos[0]+dx, pos[1]+dy)
        elif letter == '-':
            angle -= da
 
    trigger = False
    '''
        dx = 3
        dy = 3
        Xscaler = 50
        Yscaler = 500
        posPrev = ''
        posPrevR=''
        color = (230,150-(.001*n)%150,0)
        #pos = (s['Generation'][n],  dim[1]-10)
        #pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
        #pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))

        color=(0,255,0)
        pos = (s['Generation'][n], s['adjustableRate'][n])
        pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
        pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))

        
        color=(255,0,0)
        pos = (s['Generation'][n]*Xscaler, s['ExperimentRed'][n] * Yscaler)

        if posPrevR:
            pygame.draw.line(screen,color,posPrevR,(pos[0],pos[1]))
        else:
            pygame.draw.line(screen,color,pos,(pos[0],pos[1]))
        posPrevR = pos
       
        pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))


        #pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
    
        color=(255,255,255)
        pos = (s['Generation'][n]*Xscaler, (s['ExperimentWhite'][n] *Yscaler))

        if posPrev:
            pygame.draw.line(screen,color,posPrev,(pos[0],pos[1]))
        else:
            pass
            pygame.draw.line(screen,color,pos,(pos[0],pos[1]))
        posPrev = pos

        color=(0,0,255)
        pos = (s['Generation'][n]+Xscaler, (s['ExperimentBlue'][n] * Yscaler)  )
        
        pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))

