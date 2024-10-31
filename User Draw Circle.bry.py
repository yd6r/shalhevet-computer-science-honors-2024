import random

colors=['blue', 'green', 'banana']

def draw_circle(x, y):
    cir = Circle(20)
    cir.set_color(random.choice(colors))
    cir.set_position(x, y)
    add(cir)


add_mouse_click_handler(draw_circle)
