const submitButton = document.getElementById("submit_button");

function TimeValidator(event){
    let nextSibling = event.target.nextElementSibling;

    if(!event.target.value){
        event.target.classList.add("border-danger");
        nextSibling.innerHTML = "Pole jest puste",
        nextSibling.classList.add("p-2", "m-1", "text-danger");
    }
    else{
        const isValid = /^(?:[01][0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?$/.test(event.target.value);

        !isValid
        ? (
            event.target.classList.add("border-danger"),
            nextSibling.innerHTML = "Wpisana godzina nie jest prawidłowa",
            nextSibling.classList.add("p-2", "m-1", "text-danger"),
            submitButton.classList.add("disabled")
            )
        : null;
    }
};

let timeFields = document.body.querySelectorAll("input[type=text]");

for(let field of timeFields){
    field.addEventListener("blur", TimeValidator);
    field.addEventListener("focus", function(event){
        event.target.classList.remove("border-danger");
        let nextSibling = event.target.nextElementSibling;
        nextSibling.innerHTML = "";
        nextSibling.classList.remove("p-2", "m-1", "text-danger");
        submitButton.classList.remove("disabled");
    });
}

