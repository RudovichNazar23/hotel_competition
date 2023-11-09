class ValidatePhoneNumberHandler extends BaseFieldValidatorHandler{
    constructor(){
        super();
        this.valid_regex = /^\+48[0-9]{9}$/;
        this.error_message = "Incorrect phone number";
    }
};

const tel_inputs = document.body.querySelectorAll("input[type=tel]");
for(let input of tel_inputs){
    input.addEventListener("blur", new ValidatePhoneNumberHandler());
};
