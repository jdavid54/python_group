from turtle import *
import colorsys

def init():
    speed(6)
    hideturtle()
    bgcolor('black')
    tracer(5)
    width(3)
    

def motif():
    init()
    h=0.001
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    left(60)
    forward(100)
    right(120)
    circle(50)
    left(240)
    forward(100)
    left(60)
    forward(100)

#motif()


init()
h = 0.001
repeat = 9
for i in range(repeat):
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    left(60)
    forward(100)
    right(120)    
    circle(50)    
    left(240)    
    forward(100)
    
    left(60)
    
    forward(100)
    
    h += 0.02
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    right(60)
    forward(100)
    left(120)
    
    circle(-50)
    right(240)
    forward(100)
    right(60)
    forward(100)
    
    left(180//repeat)
    
    h += 0.02

done()
