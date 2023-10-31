function checkFieldIsEmpty(event){
    let input = event.target;
    if(!input.value){
        input.classList.add("invalid_field");
        input.nextElementSibling.classList.add("p-2", "m-2", "text-danger");
        input.nextElementSibling.innerHTML = "This field is empty";
    }
    else{
        $.ajax(
            {
                type: "POST",
                url: this.action,
                headers: {"X-CSRFTOKEN": getCookie("csrftoken")},
                data: $(event.target).serialize(),
                dataType: "json",
            }
        );
    }
};

function focusFormField(event){
    let input = event.target;
    if (input.classList.contains("invalid_field")){
        input.classList.remove("invalid_field");
        input.nextElementSibling.classList.remove("p-2", "m-2", "text-danger");
        input.nextElementSibling.innerHTML = "";
    }
};

let inputs = document.body.querySelectorAll("input");

for(let input of inputs){
    input.addEventListener("blur", checkFieldIsEmpty);
    input.addEventListener("focus", focusFormField);
};
