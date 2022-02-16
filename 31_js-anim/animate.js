// Team Cappucino :: Daniel Sooknanan, Tami Takada
// SoftDev pd1
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

//access canvas and buttons via DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = "#42bdff"

var requestID;  //init global var for use with animation frames

var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight)
};


var radius = 40;
var growing = true;


var drawDot = (e) => {
  let max_radius = c.clientWidth / 2
  let min_radius = 0

  // Clear the canvas
  clear();

  // Repaint circle
  if (growing) {
    radius++;
  } else {
    radius--;
  }

  if (radius >= max_radius || radius <= min_radius) {
    growing = !growing
  }

  ctx.beginPath();
  ctx.arc(c.clientWidth / 2, c.clientHeight / 2, radius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke(); 

  // console.log(e)
  if (e && requestID != null) {
    window.cancelAnimationFrame(requestID)
  }
  requestID = window.requestAnimationFrame(drawDot);
  // console.log(requestID)
};


var stopIt = () => {
  console.log("stopIt invoked...")
  // console.log( requestID );
  window.cancelAnimationFrame(requestID)
};

dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
