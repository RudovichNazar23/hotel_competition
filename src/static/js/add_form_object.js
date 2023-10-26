class InputHandler{
    constructor(target){
        this.target = target;
        this.target_parent = target.parentElement;
    };

    handleEvent(event){
        event.preventDefault();
        if(this.get_errors() || this.get_empty_fields()){ return; }

        this.target.parentElement.removeChild(this.target);

        let sibling = this.getNextSibling(this.target_parent);
        let next_sibling = this.getNextSibling(sibling);

        sibling.classList.remove("d-none");
        next_sibling.classList.remove("d-none");
        next_sibling.scrollIntoView();

        let sec_team_member = this.getNextSibling(next_sibling.nextElementSibling);
        if(sec_team_member.id === "add_container"){
            sec_team_member.classList.remove("d-none");
            this.getNextSibling(sec_team_member).classList.remove("d-none");
        };

    };

    getNextSibling(element){
        return element.nextElementSibling;
    };

    getFormInputs(){
        let form_inputs = Array.from(this.target_parent.querySelectorAll("input"));
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

