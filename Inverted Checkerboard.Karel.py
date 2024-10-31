#Make a row of red-to-black starting from the left
def paint_row_1():    
    while front_is_clear():
        paint(color["red"])
        move()
        paint(color["black"])
        if front_is_clear():
            move()
    return        

#Make a row od black-to-red starting from the right           
def paint_row_2():
    turn_left()
    move()
    turn_left()
    while front_is_clear():
        paint(color["black"])
        move()
        paint(color["red"])
        if front_is_clear():
            move()
    return

#Make a full red and black checkerboard
def paint_2_rows():
    for i in range(5):
        paint_row_1()
        turn_left()
        move()
        turn_left()
        paint_row_1()
        turn_right()
        if front_is_clear():
            move()
            turn_right()
    return

#Make a full red and black checkerboard and go to the 
#starting position
def build_and_go_to_start():
    paint_2_rows()
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    return

#turns south and goes to the bottom of the screen
#Should be used to return to the starting point
def return_to_start():
    if facing_west():
        turn_left()
    if facing_north():
        turn_around()
    if facing_east():
        turn_right()
    while front_is_clear():
        move()
    turn_left()
    return

#Changes the colors of a single row from red to blue and
#black to yellow
def invert_row():
    for i in range(5):
        while color_is(color["red"]):
            paint(color['blue'])
            if front_is_clear():
                move()
        while color_is(color['black']):
            paint(color['yellow'])
            if front_is_clear():
                move()
    return

#Builds a checkerboard of red and black, then
#changes the colors of the whole checkerboard from red to 
#blue and black to yellow and returns to the bottom of
#the world
def invert_checkerboard():
    build_and_go_to_start()
    for i in range(5):
        invert_row()
        turn_left()
        if front_is_clear():
            move()
        turn_left()
        invert_row()
        turn_right()
        if front_is_clear():
            move()
        turn_right()
    return_to_start()
    return

#Builds a checkerboard of red and black, then
#changes the colors of the whole checkerboard from red to 
#blue and black to yellow, then back to red and black and
#goes to the starting position
def invert_twice():
    invert_checkerboard()
    build_and_go_to_start()


invert_twice()
