let likeBtnEl= document.querySelector("#like-btn-el")
const LikeIcon = document.querySelector("#icon")
const CountButton = document.querySelector("#count")

// let clicked = false
let count = 0;

// likeBtnEl.addEventListener("click", function(){
    // if(!clicked){
        clicked = true;
        count += 1
        CountButton.innerHTML = count
  
    // } else {
        // clicked = false
    // }

// } )



 function likeButton (){
    count += 1;
     LikeIcon.textContent =count

 }

 function save(){
     let countStr =count + " - "
     CountButton.textContent += countStr
     CountButton.textContent = 0
     count = 0


// }


