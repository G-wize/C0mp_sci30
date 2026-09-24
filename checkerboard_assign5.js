//Gabriel, 3099913@gscs.ca, Checkerboard_assign5

function setup() {
  createCanvas(200,200); // creates a 200 by 200 canvas
  background(200); // creates a greyish background for the canvas
  noStroke(); // removes the black outline for all shapes or strokes
  
  draw_chckrboard(); //this calls all the previous functions so that the checkerboard can be drawn at once
}

//this draws the first line of the checkerboard (an alternating line of 4 black and white squares) , with the first square being a white one
  function draw_first_line() 
  {
    fill(255); // shades the inside of the shape white
    rect(0,0,50,50); //draws a 50 by 50 square in the top left corner
    fill(0); //shades the inside of the square black
    rect(50,0,50,50); //draws a 50 by 50 square right next to the first square
    fill(255);
    rect(100,0,50,50);
    fill(0);
    rect(150,0,50,50);
  }
  
  //this draws the second line of the checkerboard, with the first square being a black one
  function draw_second_line() 
  {
    fill(0);
    rect(0,50,50,50);
    fill(255);
    rect(50,50,50,50);
    fill(0);
    rect(100,50,50,50);
    fill(255);
    rect(150,50,50,50);
  }
  
  //this draws the third line of the checkerboard, with the first square being a white one
  function draw_third_line()
  {
    fill(255);
    rect(0,100,50,50);
    fill(0);
    rect(50,100,50,50);
    fill(255);
    rect(100,100,50,50);
    fill(0);
    rect(150,100,50,50);
  }
  
    //this draws the second line of the checkerboard, with the first square being a black one
  function draw_last_line()
  {
    fill(0);
    rect(0,150,50,50);
    fill(255);
    rect(50,150,50,50);
    fill(0);
    rect(100,150,50,50);
    fill(255);
    rect(150,150,50,50);
  }
  
  //this combines all the previous functions into one big one
  function draw_chckrboard()
  {
    draw_first_line();
    draw_second_line();
    draw_third_line();
    draw_last_line();
  }

function draw() {

}
