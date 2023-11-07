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
    $.ajax(
        {
            "type": "POST",
            "url": document.getElementById("registration_form").action,
            "data": createFormDataObject(),
            headers: {"X-CSRFTOKEN": getCookie("csrftoken")},
            processData: false,
            contentType: false,
            success: function(response){
                window.location.replace(window.location.origin + "/registration/" + `${response.success_url_name}`);
            },
        }
    );
    
};


const submit_button = document.getElementById("submit_button");
submit_button.addEventListener("click", sendFormData);
