function AddFieldAttributes(obj, attrs, text){
    if(attrs){ obj.classList.add(...attrs) }
    if(text){ obj.innerHTML = text }
}

function checkFieldIsEmpty(event){
    let input = event.target;
    if(!input.value){
        input.classList.remove("success_field");
        AddFieldAttributes(input, ["invalid_field",]);
        AddFieldAttributes(input.nextElementSibling, ["p-2", "m-2", "text-danger"],  "This field is empty");
    }
};

function checkFieldData(event){
    if(!event.target.value){ return; }
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
                if(response.status === 200){
                    event.target.classList.add("success_field")
                }
                else{
                    let sibling = event.target.nextElementSibling;
                    AddFieldAttributes(event.target, ["invalid_field",]);
                    AddFieldAttributes(sibling, ["p-2", "m-2", "text-danger"], response.message);
                }
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
