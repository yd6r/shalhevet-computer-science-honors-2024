# Constants for body
HEAD_RADIUS = 35
BODY_WIDTH = HEAD_RADIUS * 2
BODY_HEIGHT = 60
NUM_FEET = 3
FOOT_RADIUS = (BODY_WIDTH) / (NUM_FEET * 2)

# Constants for eyes
PUPIL_RADIUS = 4
PUPIL_LEFT_OFFSET = 8
PUPIL_RIGHT_OFFSET = 20
EYE_RADIUS = 10
EYE_OFFSET = 14


#Draws a ghost at location (x,y) with color (color)
def draw_ghost(x, y, color):
    FOOT_HEIGHT=y+BODY_WIDTH-5/6*FOOT_RADIUS
    hd=Circle(HEAD_RADIUS)
    hd.set_position(x,y)
    hd.set_color(color)
    add(hd)
    body=Rectangle(BODY_WIDTH, BODY_HEIGHT)
    body.set_position(x-HEAD_RADIUS, y)
    body.set_color(color)
    add(body)
    ft_1=Circle(FOOT_RADIUS)
    ft_1.set_position(x, FOOT_HEIGHT)
    ft_1.set_color(color)
    add(ft_1)
    ft_2=Circle(FOOT_RADIUS)
    ft_2.set_position(x-FOOT_RADIUS*2, FOOT_HEIGHT)
    ft_2.set_color(color)
    add(ft_2)
    ft_3=Circle(FOOT_RADIUS)
    ft_3.set_position(x+FOOT_RADIUS*2, FOOT_HEIGHT)
    ft_3.set_color(color)
    add(ft_3)
    eye_1=Circle(EYE_RADIUS)
    eye_1_pos=x-EYE_RADIUS
    eye_1.set_position(eye_1_pos, y)
    eye_1.set_color(Color.white)
    add(eye_1)
    eye_2=Circle(EYE_RADIUS)
    eye_2_pos=eye_1_pos+EYE_RADIUS+EYE_OFFSET
    eye_2.set_position(eye_2_pos,y)
    eye_2.set_color(Color.white)
    add(eye_2)
    pupil_1=Circle(PUPIL_RADIUS)
    pupil_1.set_position(eye_1_pos+6, y)
    pupil_1.set_color(Color.blue)
    add(pupil_1)
    pupil_2=Circle(PUPIL_RADIUS)
    pupil_2.set_position(eye_2_pos+6, y)
    pupil_2.set_color(Color.blue)
    add(pupil_2)



draw_ghost(50,100,Color.red)
draw_ghost(100,340,Color.green)
draw_ghost(240,100,Color.orange)
