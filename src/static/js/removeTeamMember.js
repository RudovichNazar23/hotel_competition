class RemoveSecondTeamMember{
    handleEvent(event){
        event.preventDefault();
        this.RemoveCurrentContainer(event.target);
        let hr = document.getElementById("hr");
        hr.after(this.build());
    };

    RemoveCurrentContainer(button){
        button.parentElement.remove();
    };

    build(){
        let div = this.CreateDivContainer();
        let button = this.CreateAddButton();

        div.appendChild(button);
        return div;
    };

    CreateDivContainer(){
        let div = document.createElement("div");
        div.classList.add("container", "bg-light", "p-3", "mt-3", "rounded");
        div.id = "add_container";
        return div;
    };

    CreateAddButton(){
        let button = document.createElement("button");
        button.classList.add("btn", "btn-info");
        button.id = "team_member";
        button.innerHTML = "Dodać osobę";
        button.addEventListener("click", new CreateTeamMemberHandler());
        return button;
    };
};
