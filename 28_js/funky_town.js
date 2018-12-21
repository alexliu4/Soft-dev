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
var gcd = (a, b) => {
  if ( b == 0 ) {
    return a;
  }
  return gcd(b, a % b);
}
// var gcd = (a,b) => {
//   if (a == 1) return 1;
//   if (b % a == 0) return a;
//   return gcd(a - 1, b);
// }

// made list of students
var studentList = ["MaiJ", "LiuA", "adayR", "aschJ","belkebirl","chenJ","chowdhuryJ"]

// chooses a random student from list using Math.random()
var randomStudent = function(){
     var index = parseInt(Math.random() * studentList.length);
  return studentList[index];
}
