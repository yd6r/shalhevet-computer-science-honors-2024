cir_win_txt=Text("Green Wins!")
sq_win_txt=Text("Red Wins!")
red_leading_txt=Text("RED IS WINNING")
green_leading_txt=Text("GREEN IS WINNING")
green_leading_txt.set_color(Color.green)
red_leading_txt.set_color(Color.red)
green_leading_txt.set_font("10pt Pacifico")
red_leading_txt.set_font("10pt Pacifico")

bottom_line=Line(1,450,379,450)
add(bottom_line)
top_line=Line(1,30,379,30)
add(top_line)

def winner():
    if cir_x() >= 380:
        remove(green_leading_txt)
        cir_win_txt.set_position(70,220)
        cir_win_txt.set_color(Color.green)
        cir_win_txt.set_font("40pt Impact")
        add(cir_win_txt)
        remove(red_leading_txt)
        sq.set_position(-100,3)
    elif sq_x() >= 380:
        remove(red_leading_txt)
        sq_win_txt.set_color(Color.red)
        sq_win_txt.set_position(70,220)
        sq_win_txt.set_font("40pt Impact")
        add(sq_win_txt)
        circle.set_position(-100,3)
        remove(green_leading_txt)
    if cir_x() > sq_x() and cir_x() < 380:
        green_leading_txt.set_position(100,50)
        remove(red_leading_txt)
        remove(green_leading_txt)
        add(green_leading_txt)
    if sq_x() > cir_x() and sq_x() < 380:
        red_leading_txt.set_position(100,50)
        remove(green_leading_txt)
        remove(red_leading_txt)
        add(red_leading_txt)
        
top_y=top_line.get_y()
bottom_y=bottom_line.get_y()


def cir_x(): return circle.get_x()-24
def sq_x(): return sq.get_x()
def cir_y(): return circle.get_y()
def sq_y(): return sq.get_y()



def wall_collision():
    print(top_y, bottom_y)
   # print("working")  
    if top_y>=cir_y:
        #circle.set_position(cir_x, top_y)
        print("out of bounds")
    if top_y>=sq_y:
        sq.set_position(sq_x,top_y)
        print("out of bounds")
    if bottom_y<=cir_y:
        circle.set_position(cir_x,bottom_y)
        print("out of bounds")
    if bottom_y<=sq_y:
        sq.set_position(sq_x,bottom_y)
        print("out of bounds")
        
circle=Circle(25)
circle.set_position(27,300)
circle.set_color(Color.green)
add(circle)

sq=Rectangle(50,50)
sq.set_position(1,100)
sq.set_color(Color.red)
add(sq)

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
    wall_collision()

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
