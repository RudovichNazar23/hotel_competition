function checkFieldData(event){
    if(!event.target.value){ return; }
    $.ajax(
        {
            type: "POST",
            url: window.location.href,
            headers: {"X-CSRFTOKEN": getCookie("csrftoken")},
            data: {
                "field_value": event.target.value,
                "field_name": event.target.name
            },
            dataType: "json",
            success: function(response){
                if(response.status !== 200){
                    let sibling = event.target.nextElementSibling;
                    AddFieldAttributes(event.target, ["invalid_field",]);
                    AddFieldAttributes(sibling, ["p-2", "m-2", "text-danger"], response.message);
                }
            }
        }
    );
};

let check_inputs = Array.from(document.body.querySelectorAll("input[type=email], input[type=tel]"));
let full_name_school_input = document.getElementById("id_full_name");
check_inputs.push(full_name_school_input);

for(let input of check_inputs){
    input.addEventListener("blur", checkFieldData);
};
