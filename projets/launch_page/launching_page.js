let menucomplet = document.getElementById('menucomplet');
let menu = document.getElementById('menu');
let btn = document.getElementById('but');

btn.addEventListener('click',function(){
    menu.classList.toggle('apparaitre');
    menu.style.background = "black"
});