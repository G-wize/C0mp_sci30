#Gabriel, 3099913@gscs.ca, interactive_circles_assign7

def setup():
    size(500, 500) #changes the canvaas size to 500 by 500
    #rect_mode(CENTER)
    #background(155)
    #frame_rate(120)

# this funtion repeatedly draws 2 circles at the mouse coordinates every 16.64 milliseconds
''' the computer repeatedly executes all the code embeded in function about 60 times a second
making it appear as a smooth transition of 2 circles following the mouse '''
def draw(): 
    background (155) # sets the background to a light grey colour
    fill(255,50,50) #changes fill colour to red
    ellipse(mouse_x, mouse_y, 100,100) # red cirlce that follows the mouse
    fill(0,120,255) #changes fill colour to blue
    ellipse(mouse_x,mouse_y, 50,50) # blue cirlce that follows the mouse
    #return
    
    