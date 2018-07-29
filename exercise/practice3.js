var elements = document.getElementsByClassName('menu2')
for(var i = 0 ; i < elements.length ; i++) {
  elements[i].addEventListener('click', function(evt) {
    alert(evt.target.text)
  });
}
// var elements = document.getElementsByClassName('menu2')
// for(var i = 0 ; i < elements.length ; i++) {
//   elements[i].addEventListener('click', function() {
//     alert(this.text)
//   });
// }

var btn = document.getElementById('btn-menu');
btn.addEventListener('click', function(evt) {
  var menu = document.getElementById('header-menubar');
  var noticemargin = document.getElementById('notice');
  // var menuDisplay = document.getElementById('header-menubar').style.display;
  if (menu.style.height == 0 || menu.style.height == '0px') {
  menu.style.height = '100px';
  noticemargin.style.marginTop = '150px';
  }
  else {
  menu.style.height=0;
  noticemargin.style.marginTop = '30px';
  }
})


