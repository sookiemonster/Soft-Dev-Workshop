// Cappuccino :: Daniel Sooknanan, Tami Takada
// SoftDev pd1
// K29 -- DOMfoolery++
// 2022-02-09
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        }


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

var fact = function(n) {
  if (n <= 1) {
    return 1;
  }
  return n * fact(n - 1);
}

var fib = function(n) {
  let fib_list = [0, 1];
  for (let i = 2; i <= n; i++) {
    fib_list.push(
      fib_list[i-1] + fib_list[i-2]
    )
  }
  return fib_list[n];
}

var gcd = function(a, b) {
  // Euclidean Method for getting GCD
  let gcd_helper = function(low, high) {
    if (high % low != 0) {
      return gcd_helper(high % low, low)
    }
    return low;
  }

  if (a == 0 || b == 0) {
    return 0;
  }
  else if (a < b) {
    return gcd_helper(a, b);
  }
  else {
    return gcd_helper(b, a);
  }
}

// Factorial Button
let fact_btn = document.getElementById('fact-btn');
let fact_result = document.getElementById('fact-result');
fact_btn.addEventListener('click', function() {
  let randInt = Math.floor(Math.random() * 20);
  fact_result.innerHTML = `${randInt}! = ${fact(randInt)}`;
});

// Fibonacci Button
let fib_btn = document.getElementById('fib-btn');
let fib_result = document.getElementById('fib-result');
fib_btn.addEventListener('click', function() {
  let randInt = Math.floor(Math.random() * 20);
  fib_result.innerHTML = `(n = ${randInt}) of Fibonnaci = ${fib(randInt)}`;
});

// GCD Button
let gcd_btn = document.getElementById('gcd-btn');
let gcd_result = document.getElementById('gcd-result');
gcd_btn.addEventListener('click', function() {
  let randInt1 = Math.floor(Math.random() * 100);
  let randInt2 = Math.floor(Math.random() * 100);
  gcd_result.innerHTML = `GCD of ${randInt1} & ${randInt2} = ${gcd(randInt1, randInt2)}`;
});