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
        let form_group_div = this.createDivTag(["form-group",]);
        let label_name = this.createLabelTag("Name");
        let label_surname = this.createLabelTag("Surname");
        let label_clause = this.createLabelTag("Clause");
        let name_input = this.createInputTag("text");
        let surname_input = this.createInputTag("text");
        let clause_input = this.createInputTag("file");

        div1.append(head_div);
        form_group_div.append(
            label_name, name_input, label_surname, surname_input, label_clause, clause_input
        );
        div1.append(form_group_div);
        this.form.append(div1);
    };
};

let button = document.getElementById("team_member");
button.addEventListener("click", new CreateInputHandler())

