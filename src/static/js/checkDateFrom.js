function checkDateFrom(){
    if(!dateFrom.value) return;
    const errorMessage = "Wybrany dzień nie może być mniejszy od dzisiejszego";

    if(new Date(dateFrom.value).getDate() < currentDate){
        addError(dateFrom, inputStyleAttrs());
        addError(dateFrom.nextElementSibling, errorDivStyleAttrs(), errorMessage);
        addError(submitButton, submitButtonStyleAttrs());
    }
    else{
        removeError(dateFrom, inputStyleAttrs(), false);
        removeError(dateFrom.nextElementSibling, errorDivStyleAttrs());
        removeError(submitButton, submitButtonStyleAttrs(), false);
    }
}