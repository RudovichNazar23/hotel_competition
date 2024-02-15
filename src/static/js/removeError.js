function removeError(element, classListAttrs, errorMessage = true){
    errorMessage && (
        element.innerHTML = ""
    );
    element.classList.remove(...classListAttrs);
};