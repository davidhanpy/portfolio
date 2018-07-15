var button = document.getElementById('btn-menu');

button.addEventListener('click', function(evt) {
  var headerNav = document.getElementById('header-nav');
  var headerNavDisplay = document.getElementById('header-nav').style.display;
  // console.log(headerNav, typeof(headerNav));
  // console.log(headerNavDisplay, typeof(headerNavDisplay));
  console.log(headerNav.style.height);
  if(headerNav.style.height == 0 || headerNav.style.height == '0px')
    headerNav.style.height = '600px';
  else
    headerNav.style.height = 0;

  // 논리연산자
  // AND :  &&
  // OR  :  ||
  // 비트연산자
  // AND : & 
  // OR  : |
  // 110010010101
  // 100001000001
  // 100000000001
})