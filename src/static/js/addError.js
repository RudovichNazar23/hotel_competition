function addError(element, classListAttrs, errorMessage){
    errorMessage && (
        element.innerHTML = errorMessage
    );
    element.classList.add(...classListAttrs);
}