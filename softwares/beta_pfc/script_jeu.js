let place_tour_joueur = document.getElementById("tour_joueur");
let place_tour_ia = document.getElementById("tour_ia");
let place_score_joueur = document.getElementById("int_joueur");
let place_score_ia = document.getElementById("int_ia");
let place_message_resultat = document.getElementById("texte_resultat");
let place_nb_tours = document.getElementById("nb_tours");

var compteur_joueur = 0;
var compteur_ia = 0;
var nb_tours = 0;

function restart(){
    place_tour_joueur.innerHTML = "";
    place_tour_ia.innerHTML = "";
    place_score_joueur.innerHTML = "0";
    place_score_ia.innerHTML = "0";
}

function score_max(score_joueur, score_ia, nb_de_tours){
    place_score_joueur.innerHTML = score_joueur;
    place_score_ia.innerHTML = score_ia;
    place_nb_tours.innerHTML = nb_de_tours;
    if(score_joueur >=5){
        place_message_resultat.innerHTML = "Partie terminée, vous avez gagné !";
        return false; //si la partie est finie, on retourne false
    }else if(score_ia >= 5){
        place_message_resultat.innerHTML = "Partie terminée, l'IA a gagnée";
        return false; //si la partie est finie, on retourne false
    }
}

function jeu(val) {
    const values = ['Pierre', 'Feuille', 'Ciseaux'];
    const random = Math.floor(Math.random() * values.length);
    adversaire = values[random];

    if(nb_tours == 0){
        restart();
    }
    place_message_resultat.innerHTML = "";

    if(val == 'Pierre' && adversaire == 'Feuille'){
        place_tour_joueur.innerHTML = "🪨";
        place_tour_ia.innerHTML = "🍃";
        compteur_ia++;
    }
    else if(val == 'Feuille' && adversaire == 'Pierre'){
        place_tour_joueur.innerHTML = "🍃";
        place_tour_ia.innerHTML = "🪨";
        compteur_joueur++;
    }
    else if(val == 'Pierre' && adversaire == 'Ciseaux'){
        place_tour_joueur.innerHTML = "🪨";
        place_tour_ia.innerHTML = "✂️";
        compteur_joueur++;
    }
    else if(val == 'Ciseaux' && adversaire == 'Pierre'){
        place_tour_joueur.innerHTML = "✂️";
        place_tour_ia.innerHTML = "🪨";
        compteur_ia++;
    }
    else if(val == 'Feuille' && adversaire == 'Ciseaux'){
        place_tour_joueur.innerHTML = "🍃";
        place_tour_ia.innerHTML = "✂️";
        compteur_ia++;
    }
    else if(val == 'Ciseaux' && adversaire == 'Feuille'){
        place_tour_joueur.innerHTML = "✂️";
        place_tour_ia.innerHTML = "🍃";
        compteur_joueur++;
    }
    else{
        place_tour_joueur.innerHTML = "Match nul";
        place_tour_ia.innerHTML = "Match nul";
    }
    nb_tours++;

    if(score_max(compteur_joueur, compteur_ia, nb_tours) == false){ //on soumet le code a un test pour vérifier si la partie est finie ou non
        //si la partie est finie (false), on réinitialise les compteurs
        compteur_joueur = 0;
        compteur_ia = 0;
        nb_tours = 0;
    }
}

let btn1 = document.getElementById("btn1");
let value_btn1 = document.getElementById("btn1").value;
btn1.addEventListener('click', event => {
    jeu(value_btn1);
    console.log(value_btn1);
});

let btn2 = document.getElementById("btn2");
let value_btn2 = document.getElementById("btn2").value;
btn2.addEventListener('click', event => {
    jeu(value_btn2);
});

let btn3 = document.getElementById("btn3");
let value_btn3 = document.getElementById("btn3").value;
btn3.addEventListener('click', event => {
    jeu(value_btn3);
});