from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    
    b = x1 - x0
    a = y1 - y0
    d = 2 * a - b
    d = abs(d)
    xchange = 1
    if b < 0:
        xchange = -1
    ychange = 1
    if a < 0:
        ychange = -1
    a = abs(a) * 2
    b = abs(b) * 2
    
    #non-vertical lines
    while x0 != x1:
        plot(screen,color,x0,y0)
        while d > 0:
            y0+= ychange
            d-= b
            if(d > 0):
                plot(screen,color,x0,y0)
        x0+= xchange
        d+= a
        
    #vertical line
    if (x0 == x1):
        for a in range(y0,y1,ychange):
            plot(screen,color,x0,a)
        
    
    
