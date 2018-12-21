// Alex -  Alex Liu
// SoftDev1 pd7
// K30 -- Sequential Progression
// 2018-12-20 W

// recursive fibonacci
var fibonacci = function(n){
  if (n == 0) return 0;
  if (n <= 2) return 1;
  return fibonacci(n - 1) + fibonacci(n-2);
}

// fibnum keeps track of where in fibonacci sequence we are at
var fibnum = 0;
var fibList = document.getElementById("fibList");

document.getElementById("fb").addEventListener('click', function(){
  // forgot whether its just numbers or bullet points

  var li = document.createElement("ol");
  // var li = document.createElement("li");
  li.innerHTML= fibnum + ". " + fibonacci(fibnum);
  // add fib to sequence
  document.body.appendChild(li);
  fibnum++;
});

// add "WORD" to list function
var wordAdd = function(e){
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  // sets header to word if mouse is over it
  item.addEventListener("mouseover", itemHeading);
  // resets to "Hello World" after
  item.addEventListener("mouseout", function(){
    head.innerHTML = "Hello World!";
  })
  // if clicked remove
  item.addEventListener("click", remover);
  list.appendChild(item);
};

// when button is clicked use wordAdd function
var button = document.getElementById("word");
button.addEventListener("click", wordAdd);


// helper function to change the "HELLO WORLD" header to item
var itemHeading = function(e){
  var head = document.getElementById("head");
  head.innerHTML = e.target.innerHTML; //sets the head to what the mouse is currently pointing to
}

// helper function to remove 'clicked' item from list
var remover = function(e){
  e.target.remove();
};

// to change header of list and remove elements (for items)
var listed = document.getElementsByTagName("li");
for (var i = 0; i < listed.length; i++){
  // if mouse hovers over change heading to the item being hovered over
  listed[i].addEventListener("mouseover", itemHeading);
  // if mouse goes away changed heading back to "HELLO WORLD"
  listed[i].addEventListener("mouseout", function(){
    head.innerHTML = "Hello World!";
  })
  // if the list item is clicked remove it
  listed[i].addEventListener("click", remover);
}
