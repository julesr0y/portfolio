// Fonction ouvrir/fermer le menu
var menuOpened = false;
function openNav() {
    if (menuOpened == false) {
        menuOpened = true;
        document.getElementById("animationMenu").classList.add('is-active');
        document.getElementById("sidebarMenu").classList.add('slidebar-expand');
    } else {
        menuOpened = false;
        document.getElementById("animationMenu").classList.remove('is-active');
        document.getElementById("sidebarMenu").classList.remove('slidebar-expand');
    }
}

// Fonction troll "j'ai oublié mon mdp"
$(document).ready(function(){
    $(".mdp").click(function(){
      alert("Cheh ( ͡° ͜ʖ ͡°)");
    });
  });

  function search_product() {
    let input = document.getElementById('searchtextbox').value
    input=input.toLowerCase();
    let x = document.getElementsByClassName('produits');
      
    for (i = 0; i < x.length; i++) { 
        if (!x[i].getAttribute("search-data").toLowerCase().includes(input)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="initial";       
        }
    }
}

// Fonction troll panier
$(document).ready(function(){
    $(".cart-btn").click(function(){
      alert("Achat impossible. Cet article est trop volumineux pour contenir dans un panier. La prochaine fois, louez un semi remorque");
    });
  });