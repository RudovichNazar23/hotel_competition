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

function focusFormField(event){
    let input = event.target;
    if (input.classList.contains("invalid_field")){
        input.classList.remove("invalid_field");
        input.nextElementSibling.classList.remove("p-2", "m-2", "text-danger");
        input.nextElementSibling.innerHTML = "";
    }
};

let inputs = document.body.querySelectorAll("input[required]");

for(let input of inputs){
    input.addEventListener("blur", checkFieldIsEmpty);
    input.addEventListener("focus", focusFormField);
};

