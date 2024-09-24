from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)

def run_top():
    print('TOP')
    
    for x in range(0, 750, 10):
        draw_boy(x, 550)
    pass

def run_right():
    print('RIGHT')
    
    for y in range(550, 0, -10):
        draw_boy(800, y)
    pass

def run_bottom():
    print('BOTTOM')
    pass

def run_left():
    print('LEFT')
    pass

def run_rectangle():
    print('RECTANGLE')

    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800 // 2, 800 // 2
    
    for d in range(0, 360):
        x = r*math.cos(math.radians(d)) + cx
        y = r*math.sin(math.radians(d)) + cy
        draw_boy(x, y)
    
    pass


while True:
    
    #run_circle()
    run_rectangle()
    break
    
close_canvas()
