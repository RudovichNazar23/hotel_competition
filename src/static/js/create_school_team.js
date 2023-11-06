function createFormDataObject(){
    let form_data = new FormData();
    for(let input of document.body.querySelectorAll("input")){
        if(input.type === "file"){
            form_data.append(input.name, input.files[0]);
        }
        else{
            form_data.append(input.name, input.value);
        }
    }
    return form_data;
};

function sendFormData(event){
    event.preventDefault();
    event.target.click(
        $.ajax(
            {
                "type": "POST",
                "url": document.getElementById("registration_form").action,
                "data": createFormDataObject(),
                headers: {"X-CSRFTOKEN": getCookie("csrftoken")},
                processData: false,
                contentType: false
            }
        ).always(
            function(){
                createFormDataObject();
            }
        )
    )
};


const submit_button = document.getElementById("submit_button");
submit_button.addEventListener("click", sendFormData);

