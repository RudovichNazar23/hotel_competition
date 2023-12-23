class CreateTeamMemberHandler{
    constructor(){
        this.form = document.getElementById("registration_form");
    };

    handleEvent(event){
          event.preventDefault();
          this.removeContainer(event.target.parentElement);
          this.build();

          let second_team_member = document.getElementById("second_team_member");
          second_team_member.append(this.createRemoveButton());
    };

    removeContainer(container){
        container.remove();
    };

    createLabelTag(labelText){
        let label = document.createElement("label");
        label.innerHTML = labelText;
        return label;
    };

    createInputTag(type, name){
        let new_input = document.createElement("input");
        new_input.type = type;
        new_input.name = name;
        new_input.classList.add("form-control");
        new_input.setAttribute("required", "")
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

    build(){
        let div1 = this.createDivTag(["container", "d-flex", "flex-column"]);
        div1.id = "second_team_member";
        let head_div = this.createDivTag(["text-center",], "<strong>Formularz drugiego członka</strong>");

        let name_form_group = this.createFormGroup("Imie uczęstnika:", "text", "second_member_name");
        let surname_form_group = this.createFormGroup("Nazwisko uczęstnika:", "text", "second_member_surname");
        let clause_form_group = this.createFormGroup("Klauzula uczęstnika:", "file", "second_member_clause");

        div1.append(head_div);
        div1.append(
            name_form_group, surname_form_group, clause_form_group
        );
        document.getElementById("recaptcha").before(div1);
        div1.scrollIntoView();
    };

    createRemoveButton(){
        let button = document.createElement("button");
        button.innerHTML = "Usunąć osobę";
        button.classList.add("bg-danger", "rounded", "mt-2", "p-2");
        button.addEventListener("click", new RemoveSecondTeamMember());
        return button
    };

    createFormGroup(label_name, input_type, input_name){
        let form_group_div = this.createDivTag(["form-group"]);
        let label = this.createLabelTag(label_name);
        let required = document.createElement("i");
        required.innerHTML = "*";
        required.classList.add("text-danger");
        label.append(required);
        let input = this.createInputTag(input_type, input_name);

        input.addEventListener("blur", checkFieldIsEmpty);
        input.addEventListener("focus", focusFormField);

        let error_div = this.createDivTag();
        form_group_div.append(label, input, error_div);
        return form_group_div;
    };
};

let button = document.getElementById("team_member");
button.addEventListener("click", new CreateTeamMemberHandler())

