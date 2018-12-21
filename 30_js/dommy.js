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

// // helper functions
//
// // shows Fib of the 7th element
// var showFib = function(){
//   console.log(fibonacci(7));
//   document.getElementById("result").innerHTML = "Fibonacci: " + fibonacci(7);
// }
//
// // shows GCD of 48 and 16
// var showGcd = function(){
//   console.log(gcd(48,16));
//   document.getElementById("result").innerHTML = "GCD: " + gcd(48,16);
// }
//
// var showStudent = function(){
//   var selected_student = randomStudent();
//   console.log(selected_student);
//   document.getElementById("result").innerHTML = "The Random Student: " + selected_student;
// }
//
// // works with buttons
// var fib = document.getElementById('fib');
// fib.addEventListener("click", showFib);
//
// var gcd_button = document.getElementById('gcd');
// gcd_button.addEventListener("click", showGcd);
//
// var randomStudent_button = document.getElementById('randStudent');
// randomStudent_button.addEventListener('click', showStudent);
//

// change heading function
var changeHeading = function(e){
    var h = document.getElementById("h");
    h.innerHTML = e.target.innerHTML;
}

// function to remove an item from list
var removeItem = function(e){
    e.target.remove(); //can replace e.target with 'this'
};

// for every liste item, do :
var lis = document.getElementsByTagName("li");
for (var i = 0; i < lis.length; i++){
    // if mouse hovers over, change heading
    lis[i].addEventListener("mouseover", changeHeading);
    // if mouse goes away, go back to original heading
    lis[i].addEventListener("mouseout", function(){
	h.innerHTML = "Hello World!";
    })
    // if click on li, remove
    lis[i].addEventListener("click", removeItem);
}

// add item using button
var addItem = function(e){
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    list.appendChild(item);
};

// when button is clicked, call addItem
var button = document.getElementById("b");
button.addEventListener("click", addItem);

// fibnum keeps track of where in fibonacci sequence we are at
var fibnum = 0;
// checks if there is a fib list. if not, it creates
var addFib = function(e){
    console.log(e);
    if (document.getElementById("fib") == null){
	var list = document.createElement("ol");
	list.setAttribute("id", "fib");
	document.body.appendChild(list);
	console.log(list);
    }
    // call fib2() to add item
    addFib2();
};

// add list item based on where we are in fib sequence
var addFib2 = function(e) {
    console.log("made it here");
    var list = document.getElementById("fib");
    var item = document.createElement("li");
    item.innerHTML = fibonacci(fibnum);
    list.appendChild(item);
    fibnum += 1;
};

// if click on button, add to fib sequence
var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
