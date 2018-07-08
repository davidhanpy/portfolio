// console.log(add(5, 10));

// 함수
// 함수선언식
// function add(a, b) {
//   return a + b;
// }
// 함수표현식
// var add = function(a, b) {
//   return a + b;
// }

var printAlt = function(evt) {
  // alt 출력
  alert(evt.target.alt)
};

// 이미지 이벤트 리스너
var elements = document.getElementsByTagName('img');
for(var i = 0 ; i < elements.length ; i++) {
  elements[i].addEventListener('click', function(evt) {
    // alt 출력
    alert(evt.target.alt)
  });
}

var element = document.getElementsByTagName('h1')[0];
var count = 0;
window.setInterval(function() {
  switch(count) {
    case 0:
    element.style.left = '200px';
    count++;
    break;
    case 1:
    element.style.top = '200px';
    element.style.left = '200px';
    count++;
    break;
    case 2:
    element.style.left = '0px';
    count++;
    break;
    case 3:
    element.style.top = '0px';
    count = 0;
    default: count = 0;
  }
  
}, 2000);

// object
// var obj = {
//   key:'value',
//   key2:function() {

//   },
//   key3: {

//   }
// }

