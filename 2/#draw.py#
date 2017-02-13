from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    b = x0 - x1
    a = y1 - y0
    d = 2 * a + b
    a *= 2
    b *= 2
    while x0 < x1:
        plot(screen,color,x0,y0)
        if d > 0:
            y0+= 1
            d+= b
        while d > 0:
            plot(screen,color,x0,y0)
            y0+= 1
            d+=b
        x0+= 1
        d+= a
    
        
    
    
