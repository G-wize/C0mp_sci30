#Gabriel, 3099913@gscs.ca, Checkerboard_assign5

def setup():
    size(500, 500)
    background(200)
    
    draw_robot(150,200,160,0) #calls the draw robot function
    
#function to draw the mouse's head using parrameters (pc)
# (pc): defines the grayscale colour for the body/skin of the mouse
def draw_head(pc):
    fill(pc) # shades the inside of the shape whatever number pc is set to in the argument
    ellipse(80,80,30,30) #draws left ear
    ellipse(120,80,30,30) #draws right ear
    ellipse(100,100,50,50) #draws a 50 by 50 circle (head) in the middle of the ears
    fill(0) #changes fill colour to black
    ellipse(110,100,10,10) #draws right eye
    ellipse(90, 100,10,10) #draws left eye
    
#function to draw the mouse's body using parameters (pc)
# (pc): defines the grayscale colour for the body/skin of the mouse
def draw_body(pc):
    fill(pc) 
    ellipse(100,175,70,100) #draws the frame of the body
    fill(255,0,0) #changes fill colour to red
    ellipse(100,175,10,10) #draws the middle button 
    fill(0,255,0) #changes fill colour to green
    ellipse(80,175,10,10) #draws the flet button
    fill(0,0,255) #changes fill colour to blue
    ellipse(120,175,10,10) #draws the right button

# function to draw the left and right arms of the mouse using parameters (pc,sc1,sc2,sc3)
# (pc): defines the grayscale colour for the body/skin of the mouse
# (sc1,sc2,sc3): defines the RGB colour scale for the hands/fists of the mouse
def draw_arms(pc,sc1,sc2,sc3):
    fill(pc) 
    rect(20,150,50,10) #draws the frame of the left arm
    rect(130,150,50,10) #draws the frame of the right arm
    fill(sc1,sc2,sc3) # shades the inside of the shape whatever number sc1,sc2 and sc3 are set to in the argument
    ellipse(20,155,30,30) #draws a fist for the left hand
    ellipse(180,155,30,30) #draws a fist for the right hand
    
# function to draw the left and right legs of the mouse using parameters (pc,sc1,sc2,sc3)
# (pc): defines the grayscale colour for the body/skin of the mouse
# (sc1,sc2,sc3): defines the RGB colour scale for the foot/feet of the mouse 
def draw_legs(pc,sc1,sc2,sc3):
    fill(pc)
    rect(80, 215,10,50) #draws the frame of the left leg
    rect(110,215,10,50) #draws the frame of the right leg
    fill(sc1,sc2,sc3) # shades the inside of the shape whatever number sc1,sc2 and sc3 are set to in the argument
    ellipse(85,265,30,30) #draws a ball for the left foot
    ellipse(115,265,30,30) #draws a ball for the right foot
    
# funtion to draw all the parts (head,body,arms,legs) of the mouse at once using the previous parameters (pc,sc1,sc2,sc3)
# (pc): defines the grayscale colour for the body/skin of the mouse
# (sc1,sc2,sc3): defines the RGB colour scale for the hands/feet of the mouse
def draw_robot(pc,sc1,sc2,sc3):    
    draw_head(pc) #calls the draw head function
    draw_arms(pc,sc1,sc2,sc3) #calls the draw arms function
    draw_legs(pc,sc1,sc2,sc3) #calls the draw legs function
    draw_body(pc) #calls the draw body function
                  #note: the draw body function is called last to ensure that the rectangles for the arms and legs are not visibly infront of the body
        
#def draw():
    
    
    
    '''stroke(255,0,0)
    fill(255, 255, 0)
    rect(50,50, 50, 50)
    
    stroke(0,150,255)
    fill(255,100,255)
    ellipse(160,160, 100,50)'''
    
    
    
