from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
draw_line(screen,0,0,100,200,color)
draw_line(screen,0,0,-100,200,color)
draw_line(screen,0,0,100,-200,color)
draw_line(screen,0,0,-100,-200,color)
draw_line(screen,0,0,200,100,color)
draw_line(screen,0,0,-200,100,color)
draw_line(screen,0,0,200,-100,color)
draw_line(screen,0,0,-200,-100,color)
draw_line(screen,0,0,0,200,color)
draw_line(screen,0,0,0,-200,color)
draw_line(screen,0,0,200,0,color)
draw_line(screen,0,0,-200,0,color)
display(screen)
save_extension(screen, 'img.png')


