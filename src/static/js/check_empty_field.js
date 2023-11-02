function checkFieldIsEmpty(event){
    let input = event.target;
    if(!input.value){
        input.classList.add("invalid_field");
        input.nextElementSibling.classList.add("p-2", "m-2", "text-danger");
        input.nextElementSibling.innerHTML = "This field is empty";
    }
};

function checkFieldData(event){
    $.ajax(
        {
            type: "POST",
            url: this.action,
            headers: {"X-CSRFTOKEN": getCookie("csrftoken")},
            data: {
                "field_value": event.target.value,
                "field_name": event.target.name
            },
            dataType: "json",
            success: function(response){
               console.log(response);
            }
        }
    );
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

let check_inputs = Array.from(document.body.querySelectorAll("input[type=email], input[type=tel]"));
let full_name_school_input = document.getElementById("id_full_name");
check_inputs.push(full_name_school_input);

for(let input of check_inputs){
    input.addEventListener("blur", checkFieldData);
};
