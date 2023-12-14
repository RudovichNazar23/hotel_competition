class SendFormDataHandler{

    handleEvent(event){
        event.preventDefault();
        if(this.checkErrors()){
            return;
        }
        else{
            this.sendFormData();
        }
    };

    createFormDataObject(){
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

    sendFormData(){
        $.ajax(
            {
                "type": "POST",
                "url": document.getElementById("registration_form").action,
                "data": this.createFormDataObject(),
                headers: {"X-CSRFTOKEN": getCookie("csrftoken")},
                processData: false,
                contentType: false,
                success: function(response){
                    if(response.status === 200){
                        window.location.replace(window.location.origin + "/registration/" + `${response.success_url_name}`);
                    }
                    else{
                        window.location.replace(window.location.origin + "/registration/" + `${response.error_url_name}`);
                    }
                },
            }
        );
    };

    checkErrors(){
        let inputs = document.body.querySelectorAll("input[required]");
        let button = document.getElementById("submit_button");

        for(let input of inputs){
            if(input.classList.contains("invalid_field")){
                input.scrollIntoView({"behavior": "smooth", "block": "end", "inline": "nearest"});
                return true;
            }
        };
    };
};


const submit_button = document.getElementById("submit_button");
submit_button.addEventListener("click", new SendFormDataHandler());

