var elements = document.getElementsByClassName('menu2')
for(var i = 0 ; i < elements.length ; i++) {
  elements[i].addEventListener('click', function(evt) {
    // alt 출력
    alert(evt.target.text)
  });
}
// function print(a) {
//     return alert(a);
// }
// print(element)