class ValidateEmailHandler extends BaseFieldValidatorHandler{
    constructor(){
        super();
        this.valid_regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        this.error_message = "Nieprawidłowy adres e-mail";
    };
};

const email_fields = document.body.querySelectorAll("input[type=email]");

for(let input of email_fields){
    input.addEventListener("blur", new ValidateEmailHandler());
    input.addEventListener("focus", focusFormField);
}

