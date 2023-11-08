class ValidatePhoneNumberHandler extends BaseFieldValidatorHandler{
    constructor(){
        super();
        this.valid_regex = /^(\+[1-9]{1}[0-9]{3,14})?([0-9]{9,14})$/;
        this.error_message = "Incorrect phone number";
    }
};

const tel_inputs = document.body.querySelectorAll("input[type=tel]");
for(let input of tel_inputs){
    input.addEventListener("blur", new ValidatePhoneNumberHandler());
};
