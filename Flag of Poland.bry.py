# shalhevet-computer-science-honors-2024
def top_left():
    rect1=Rectangle(100,200)
    rect1.set_position(0,0)
    rect1.set_color(Color.red)
    add(rect1)

def bottom_left():
    rect2=Rectangle(100,200)
    rect2.set_position(0,250)
    rect2.set_color(Color.red)
    add(rect2)

def top_right():
    rect3=Rectangle(500,200)
    rect3.set_color(Color.red)
    rect3.set_position(150,0)
    add(rect3)

def bottom_right():
    rect4=Rectangle(500,200)
    rect4.set_color(Color.red)
    rect4.set_position(150,250)
    add(rect4)
    
top_left()
bottom_left()
top_right()
bottom_right()
