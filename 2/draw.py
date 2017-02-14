from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    b = x1 - x0
    a = y1 - y0
    d = 2 * a - b
    d = abs(d)
    xchange = b / abs(b) 
    ychange = a / abs(a)
    a = abs(a) * 2
    b = abs(b) * 2
    while x0 != x1:
        plot(screen,color,x0,y0)
        while d > 0:
            y0+= ychange
            d-= b
            if(d > 0):
                plot(screen,color,x0,y0)
        x0+= xchange
        d+= a
    
        
    
    
