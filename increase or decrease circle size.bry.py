my_circle=Circle(100)
my_circle.set_position(250,250)
add(my_circle)

def change_size(event):
    if event.key=="ArrowLeft":
        cur_radius=my_circle.get_radius()
        my_circle.set_radius(cur_radius-10)
        if cur_radius==10:
            my_circle.set_radius(10)
    if event.key=="ArrowRight":
        cur_radius=my_circle.get_radius()
        my_circle.set_radius(cur_radius+10)
        if cur_radius==400:
            my_circle.set_radius(400)
add_key_down_handler(change_size)
