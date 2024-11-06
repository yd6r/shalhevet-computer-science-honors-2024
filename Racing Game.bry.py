cir_win_txt=Text("Green Wins!")
sq_win_txt=Text("Red Wins!")
def winner():
    if cir_x() >= 380-24:
        cir_win_txt.set_position(70,220)
        cir_win_txt.set_color(Color.green)
        cir_win_txt.set_font("40pt Helvetica")
        add(cir_win_txt)
        sq.set_position(-100,3)
    elif sq_x() >= 380-49:
        sq_win_txt.set_color(Color.red)
        sq_win_txt.set_position(70,220)
        sq_win_txt.set_font("40pt Helvetica")
        add(sq_win_txt)
        circle.set_position(-100,3)
        

circle=Circle(25)
circle.set_position(27,300)
circle.set_color(Color.green)
add(circle)

sq=Rectangle(50,50)
sq.set_position(1,100)
sq.set_color(Color.red)
add(sq)

def cir_x(): return circle.get_x()
def sq_x(): return sq.get_x()

def move_square(event):
    if event.key=="ArrowRight":
        sq.move(15,0)
    if event.key=="ArrowLeft":
        sq.move(-15,0)
    if event.key=="ArrowDown":
        sq.move(0,15)
    if event.key=="ArrowUp":
        sq.move(0,-15)
    if event.key=="w":
        circle.move(0,-15)
    if event.key=="a":
        circle.move(-15,0)
    if event.key=="d":
        circle.move(15,0)
    if event.key=="s":
        circle.move(0,15)
    winner()

def goalpost():
    rect=Rectangle(15,50)
    rect.set_position(380,20)
    add(rect)
    
    rect2=Rectangle(15,50)
    rect2.set_position(380,400)
    add(rect2)
    
    tag=Rectangle(15,380)
    tag.set_position(380,50)
    tag.set_color(Color.yellow)
    add(tag)
    
add_key_up_handler(move_square)
goalpost()

txt=Text("Race to the yellow line")
txt.set_position(20,420)
txt.set_font("10pt New Times Roman")
txt2=Text("Circle commands are WASD")
txt2.set_position(20,430)
txt2.set_font("10pt New Times Roman")
txt3=Text("Square commands are arrows")
txt3.set_position(20,440)
txt3.set_font("10pt New Times Roman")
add(txt)
add(txt2)
add(txt3)
