function checkDateRange() {
    const errorMessage = "Dzien zakończenia rejestracji nie może być mniejszy od dnia rozpoczęcia";

    if(!dateFrom.value || !dateTo.value ) return;

    if(dateFrom.value >= dateTo.value){
        addError(dateTo.nextElementSibling, errorDivStyleAttrs(), errorMessage);
        addError(dateTo, inputStyleAttrs());

       addError(submitButton, submitButtonStyleAttrs());
    }
    else{
        removeError(dateTo, inputStyleAttrs(), false);
        removeError(dateTo.nextElementSibling, errorDivStyleAttrs());
        removeError(submitButton, submitButtonStyleAttrs(), false);
    }
}