class CreateTeamMemberHandler{
    constructor(){
        this.form = document.getElementById("registration_form");
        this.add_container = document.getElementById("add_container");
    };

    handleEvent(event){
          event.preventDefault();
          this.removeAddContainer();
          this.build();
    };

    removeAddContainer(){
        this.add_container.parentNode.removeChild(this.add_container);
    };

    createLabelTag(labelText){
        let label = document.createElement("label");
        label.innerHTML = labelText;
        return label;
    };

    createInputTag(type){
        let new_input = document.createElement("input");
        new_input.type = type;
        new_input.name = "second_member";
        new_input.classList.add("form-control");
        return new_input;
    };

    createDivTag(class_attrs, text){
        let div = document.createElement("div");
        if(class_attrs){ div.classList.add(...class_attrs) };
        if(text){
            div.innerHTML = text;
        };
        return div;
    };

    build(inputs){
        let div1 = this.createDivTag(["container", "d-flex", "flex-column"]);
        let head_div = this.createDivTag(["text-center",], "<strong>Team member2 form</strong>");

        let name_form_group = this.createFormGroup("Name", "text");
        let surname_form_group = this.createFormGroup("Surname", "text");
        let clause_form_group = this.createFormGroup("Clause", "file");

        div1.append(head_div);
        div1.append(
            name_form_group, surname_form_group, clause_form_group
        );
        this.form.insertBefore(div1, document.getElementById("button"));
        div1.scrollIntoView();
    };

    createFormGroup(label_name, input_type){
        let form_group_div = this.createDivTag(["form-group"]);
        let label = this.createLabelTag(label_name);
        let input = this.createInputTag(input_type);

        input.addEventListener("blur", checkFieldIsEmpty);
        input.addEventListener("focus", focusFormField);

        let error_div = this.createDivTag();
        form_group_div.append(label, input, error_div);
        return form_group_div;
    };
};

let button = document.getElementById("team_member");
button.addEventListener("click", new CreateTeamMemberHandler())

