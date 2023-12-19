class InputHandler{
    constructor(target){
        this.target = target;
        this.target_parent = target.parentElement;
    };

    handleEvent(event){
        event.preventDefault();
        if(this.get_errors() || this.get_empty_fields()){ return; }

        this.target_parent.nextElementSibling.classList.remove("d-none");
        this.target_parent.removeChild(event.target);
        this.target_parent.nextElementSibling.scrollIntoView();
    };

    getNextSibling(element){
        return element.nextElementSibling;
    };

    getFormInputs(){
        let form_inputs = Array.from(this.target_parent.querySelectorAll("input[required]"));
        return form_inputs;
    };

    get_errors(){
        let form_inputs = this.getFormInputs();
        let invalid_fields = form_inputs.filter((input) => input.classList.contains("invalid_field"));
        if(invalid_fields.length > 0) {
            return true;
        }
        else {
            return false;
        }
    };

    get_empty_fields(){
        let form_inputs = this.getFormInputs();
        let empty_fields = form_inputs.filter((input) => !input.value);
        if(empty_fields.length > 0){
            return true;
        }
        else{
            return false;
        }
    };

};

let continue_buttons = document.body.querySelectorAll("button[data-action='continue']");

for(let button of continue_buttons){
    button.addEventListener("click", new InputHandler(button));
};

