// Alex - Jiajie Mai, Alex Liu
// SoftDev1 pd7
// K28 -- Sequential Progression
// 2018-12-19 W

// recursive fibonacci
var fibonacci = function(n){
    if (n == 0) return 0;
    if (n <= 2) return 1;

    return fibonacci(n - 1) + fibonacci(n-2);
}

// var gcd = (a,b) => {
//     var i,out = 0;
//     while(i < a || i < b){
// 	if(a % i == 0 && b % i == 0) {out = i;}
// 	i++
//     }
//     return i;
// }

//recursive gcd
var gcd = (a, b) => {
  if ( b == 0 ) {
    return a;
  }
  return gcd(b, a % b);
}

// made list of students
var studentList = ["MaiJ", "LiuA", "adayR", "aschJ","belkebirl","chenJ","chowdhuryJ"]

// chooses a random student from list using Math.random()
var randomStudent = function(){
     var index = parseInt(Math.random() * studentList.length);
  return studentList[index];
}

// helper functions

// shows Fib of the 7th element
var showFib = function(){
  console.log(fibonacci(7));
  document.getElementById("result").innerHTML = "Fibonacci: " + fibonacci(7);
}

// shows GCD of 48 and 16
var showGcd = function(){
  console.log(gcd(48,16));
  document.getElementById("result").innerHTML = "GCD: " + gcd(48,16);
}

var showStudent = function(){
  var selected_student = randomStudent();
  console.log(selected_student);
  document.getElementById("result").innerHTML = "The Random Student: " + selected_student;
}

// works with buttons
var fib = document.getElementById('fib');
fib.addEventListener("click", showFib);

var gcd_button = document.getElementById('gcd');
gcd_button.addEventListener("click", showGcd);

var randomStudent_button = document.getElementById('randStudent');
randomStudent_button.addEventListener('click', showStudent);
