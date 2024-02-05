class BaseFieldValidatorHandler{
    constructor(){
        this.valid_regex = undefined;
        this.error_message = undefined;
    }
    handleEvent(event){
        if(!event.target.value){ return; }
        if(!this.valid_regex.test(event.target.value)){
            AddFieldAttributes(event.target, ["invalid_field"]);
            AddFieldAttributes(event.target.nextElementSibling, ["text-danger", "m-2", "p-2"], this.error_message);
        };
    };
};