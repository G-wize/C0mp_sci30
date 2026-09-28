def setup():
    size(300, 200)
    rect_mode(CENTER)
    background(155)
    #frame_rate(120)

def mouse_pressed():
    #circle that spawns every time the mouse is pressed
    fill(0,120,255)
    ellipse(mouse_x, mouse_y, 10, 10)
    
def key_pressed():
    background(155)
    

def draw():
    # blue cirlce that follows the mosue
    fill(0,0,255)
    background (155)
    ellipse(mouse_x,mouse_y, 50,50)
    return
    '''background(0)
    ellipse(mouse_x, mouse_y, 50,50) '''

    