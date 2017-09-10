/*
    Copyright (c) 2017 HappinessLab.
    Created by Shota Shimazu on 2017/09/10
*/



var three_cards = document.getElementsByClassName("hp_card");

three_cards[0].addEventListener("animationend",function(e){
    three_cards[0].classList.add("hp_card_after_animation");
});

three_cards[1].addEventListener("animationend",function(e){
    three_cards[1].classList.add("hp_card_after_animation");
});

three_cards[2].addEventListener("animationend",function(e){
    three_cards[2].classList.add("hp_card_after_animation");
});
