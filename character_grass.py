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
    
    for x in range(50, 750, 10):
        draw_boy(x, 550)
    pass

def run_right():
    print('RIGHT')
    
    for y in range(550, 50, -10):
        draw_boy(750, y)
    pass

def run_bottom():
    print('BOTTOM')

    for x in range(750, 50, -10):
        draw_boy(x, 50)
    pass

def run_left():
    print('LEFT')

    for y in range(50, 550, 10):
        draw_boy(50, y)
    pass

def run_rectangle():
    print('RECTANGLE')

    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_tri_bottom():
    for x in range(100, 700, 10):
        draw_boy(x, 50)
    print('TB')
    
    pass

def run_tri_side_right():
    x, y = 700, 50 
    for d in range(0, 600, 10):
        x = 700 - d * math.cos(math.radians(60))
        y = 50 + d * math.sin(math.radians(60))
        draw_boy(x, y)
    print('TSR')
    pass

def run_tri_side_left():
    oy = 50 + 600 * math.sin(math.radians(60))
    x, y = 300, oy
    for d in range(0, 600, 10):
        x = 400 - d * math.cos(math.radians(60))
        y = oy - d * math.sin(math.radians(60))
        draw_boy(x, y)
    print('TSL')
    pass
    
def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800 // 2, 800 // 2
    
    for d in range(0, 360):
        x = r*math.cos(math.radians(d)) + cx
        y = r*math.sin(math.radians(d)) + cy
        draw_boy(x, y)
    
    pass

def run_triangle():
    print('TRIANGLE')

    run_tri_bottom()
    run_tri_side_right()
    run_tri_side_left()
    
    pass

while True:
    
    #run_circle()
    #run_rectangle()
    run_triangle()
    break
    
close_canvas()
