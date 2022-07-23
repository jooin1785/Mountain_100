window.onload = function(){
    cf1 = document.getElementById("cf1")
    cf2 = document.getElementById("cf2")
    cf3 = document.getElementById("cf3")

    card1=document.getElementById("card1")
    card2=document.getElementById("card2")
    card3=document.getElementById("card3")

    cf1.addEventListener('mouseover',function(){
        card1.style.border = "2px solid black";
    });
    cf1.addEventListener('mouseout',function(){
        card1.style.border = "1px solid rgba(0, 0, 0, 0.125)";
    });

    cf2.addEventListener('mouseover',function(){
        card2.style.border = "2px solid black";
    });
    cf2.addEventListener('mouseout',function(){
        card2.style.border = "1px solid rgba(0, 0, 0, 0.125)";
    });

    cf3.addEventListener('mouseover',function(){
        card3.style.border = "2px solid black";
    });
    cf3.addEventListener('mouseout',function(){
        card3.style.border = "1px solid rgba(0, 0, 0, 0.125)";
    });
}