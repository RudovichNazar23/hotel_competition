class ValidatePostCodeHandler extends BaseFieldValidatorHandler{
    constructor(){
        super();
        this.valid_regex = /^\d{2}-\d{3}$/;
        this.error_message = "Nieprawidłowy kod pocztowy";
    }
};

const post_code_input = document.getElementById("id_post_code");
post_code_input.addEventListener("blur", new ValidatePostCodeHandler());

