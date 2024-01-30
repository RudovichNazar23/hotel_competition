
function SelectAllHandler(event){
    let children = Array.from(event.target.parentNode.parentNode.querySelectorAll("input[type=checkbox]")).slice(1);

    event.target.checked ? 
        (
            children.map((input) =>  input.checked = true)
        ) : 
        (
            children.map((input) =>  input.checked = false)
        )
}

let select_inputs = Array.from(document.body.querySelectorAll("input[data-action='select']"));

select_inputs.map((input) => input.addEventListener("click", SelectAllHandler))