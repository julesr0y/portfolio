/*partie case 1*/
$(document).ready(function(){ /*lors du survol du lien de contact pc, ne colore pas en rouge*/
    $('.lien').hover(function(){
        $('.lienspecial').css('color','white'); $('#lien2').css('color','white'); $('#lien3').css('color','white');
    });
});

$(document).ready(function(){ /*lors du survol du lien de contact texte, se colore en rouge et colore lien de contact pc en rouge*/
    $('.lienspecial').hover(function(){
        $('.lien').css('color','red'); $('.lienspecial').css('color','red');
    },function(){
        $('a').css('color','white');
    });
});

/*partie contact.html*/
$(document).ready(function(){
    $("#bouton1").click(function(){
      alert("Attention, le bouton de contact par mail ne fonctionne que sur mobile. Si vous utilisez un PC, je vous recommande de me contacter via Linkedin");
    });
  });