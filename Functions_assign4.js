/* Gabriel,
3099913@gscs.ca, 
Functions and Abstraction-assignment 4
*/

function setup() {
  createCanvas(500,500) // extends canvas to 500 by 500
  
  draw_fixed_square();
  draw_circle(40,40,20);
  draw_concentric_circles(135,135)

}

   //function to draw a 50x50 squaree
  function draw_fixed_square()
  {
    //draws 50 by 50 square
    rect(50,50,50,50);
    //line(50,53,100,53);
  }
  
  //function to draw a circle with its center at based on the given parameters (x,y,d,d)
  /* (x,y) : defines the x and y coordinates of the center of the cirlce
     (d) : defines the diameter of the circle */
  function draw_circle(x,y,d)
  {
    //draws circle 
    ellipse(x,y,d,d);
  }
  
  //function to draw 3 circles of varying radii within the giver parrameters (x,y)
  // (x,y) : defines the x and y coordinates of the center of the cirlces
  // note: the diameters of the circles are already predetermined
  function draw_concentric_circles(x,y)
  {
    //draws circle with raduis 90
    ellipse(x,y,90,90);
    //draws circle with raduis 60
    ellipse(x,y,60,60);
    //draws circle with raduis 30
    ellipse(x,y,30,30);
  }

function draw() {

}
