let timeFrom = document.getElementById("id_time_from");
let timeTo = document.getElementById("id_time_to");

function CheckTimeFrom(event){
    if(!timeFrom.value || !timeTo.value) return;

    let timeToSibling = timeTo.nextElementSibling;

    if(timeFrom.value >= timeTo.value){
        timeToSibling.innerHTML = "Godzina rozpoczęcia powinna być mniejsza od godziny zakończenia";
        timeToSibling.classList.add("m-1", "p-2", "text-danger");
        submitButton.classList.add("disabled");
        timeFrom.classList.add("border-danger");
        timeTo.classList.add("border-danger");
    }
    else{
        timeFrom.classList.remove("border-danger");
        timeTo.classList.remove("border-danger");
        timeToSibling.innerHTML = "";
        timeToSibling.classList.remove("m-1", "p-2", "text-danger");
        submitButton.classList.remove("disabled");
    }

};

timeFrom.addEventListener("blur", CheckTimeFrom);
timeTo.addEventListener("blur", CheckTimeFrom);
