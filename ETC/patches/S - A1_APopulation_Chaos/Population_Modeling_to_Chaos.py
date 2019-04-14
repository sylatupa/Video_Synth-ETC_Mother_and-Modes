import pygame
from pygame.locals import *
from math import *
import random

iterations = 1000
def getstring(iterations):
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
        s['rate1_w_increase'].append(n * 0.002 + 2)
        
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

def main(dim):
    pygame.init()
    screen = pygame.display.set_mode((int(dim[0]/.8), int(dim[1]/2)),pygame.FULLSCREEN)
    t=pygame.time.get_ticks()

    s = getstring(iterations)
    print(pygame.time.get_ticks()-t)
    
    t = pygame.time.get_ticks()
    pos = dim[0]-dim[0] ,dim[1]/2
    dx = 3
    dy = 3
    Xscaler = 50
    Yscaler = 500
    posPrev = ''
    posPrevR=''
    for n in range(0,iterations):
        #color = (230,150-(.001*n)%150,0)
        #pos = (s['Generation'][n],  dim[1]-10)
        #pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
        #pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))

        color=(0,255,0)
        #pos = (s['Generation'][n], s['adjustableRate'][n])
        #pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
        #pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))

        
        color=(255,0,0)
        pos = (s['Generation'][n]*Xscaler, s['ExperimentRed'][n] * Yscaler)

        if posPrevR:
            pygame.draw.line(screen,color,posPrevR,(pos[0],pos[1]))
        else:
            pygame.draw.line(screen,color,pos,(pos[0],pos[1]))
        posPrevR = pos
       
#pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))


#pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
        
        color=(255,255,255)
        pos = (s['Generation'][n]*Xscaler, (s['ExperimentWhite'][n] *Yscaler))


        if posPrev:
            pygame.draw.line(screen,color,posPrev,(pos[0],pos[1]))
        else:
            pygame.draw.line(screen,color,pos,(pos[0],pos[1]))
        posPrev = pos
       

        color=(0,0,255)
        pos = (s['Generation'][n]+Xscaler, (s['ExperimentBlue'][n] * Yscaler)  )
        
        pygame.draw.line(screen,color,pos,(pos[0]+dx,pos[1]+dy))
        pygame.display.update((pos[0]-1,pos[1]-1,pos[0]+dx+1,pos[1]+dy+1))
    pygame.display.update()


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
    main((iterations+20,iterations+20))
