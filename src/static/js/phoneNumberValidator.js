class ValidatePhoneNumberHandler extends BaseFieldValidatorHandler{
    constructor(){
        super();
        this.valid_regex = /^[0-9]{9}$/;
        this.error_message = "Nieprawidłowy numer telefonu";
    }
};

const tel_inputs = document.body.querySelectorAll("input[type=tel]");
for(let input of tel_inputs){
    input.addEventListener("blur", new ValidatePhoneNumberHandler());
};
