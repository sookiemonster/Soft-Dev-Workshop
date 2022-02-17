// Daniel Sooknanan, Lucas Tom Wong
//SoftDev pd1
// K32 -- Screensaving
// 2022-02-17

// model for HTML5 canvas-based animation


function clamp(n, min, max) {
    if (n > max) {
        return max;
    }
    else if (n < min) {
        return min;
    }
    return n;
}

//access canvas and buttons via DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var movieButton = document.getElementById("buttonDVD");
var stopButton = document.getElementById("buttonStop");

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = "#ff335c"

var requestID;  //init global var for use with animation frames

var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight)
};


var radius = 0;
var growing = true;


var drawDot = () => {
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

  window.cancelAnimationFrame(requestID)
  requestID = window.requestAnimationFrame(drawDot);
};

// Instantiate DVD logo coordinates
var pos_x;
var pos_y;

// Define Image Dimensions
let IMG_WIDTH = 120
let IMG_HEIGHT = 80
// Get DVD Image
let DVD_IMAGE = new Image(IMG_WIDTH, IMG_HEIGHT);
DVD_IMAGE.src = 'logo_dvd.jpg';

let dy = -1;
let dx = 1;

var drawDVD = () => {
  clear() 
  if (pos_x <= 0 || pos_x + IMG_WIDTH >= c.clientWidth) {
    dx *= -1
  }

  if (pos_y <= 0 || pos_y + IMG_HEIGHT >= c.clientHeight) {
    dy *= -1
  }

  pos_x += dx
  pos_y += dy
  ctx.drawImage(DVD_IMAGE, pos_x, pos_y, IMG_WIDTH, IMG_HEIGHT);

  window.cancelAnimationFrame(requestID);
  requestID = window.requestAnimationFrame(drawDVD);
}

var stopIt = () => {
  window.cancelAnimationFrame(requestID)
};

dotButton.addEventListener( "click", function() {
  stopIt();
  drawDot();
});

movieButton.addEventListener( "click", function() {
  stopIt();
  pos_x = clamp(
      Math.floor(Math.random() * c.clientWidth) - IMG_WIDTH, 1, c.clientWidth - 1
  )
  pos_y = clamp(
      Math.floor(Math.random() * c.clientHeight) - IMG_HEIGHT, 1, c.clientHeight - 1
  )
  console.log(`${pos_x}, ${pos_y}`)
  drawDVD();
});

stopButton.addEventListener( "click",  stopIt );
