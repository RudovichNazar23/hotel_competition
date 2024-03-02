const nextButton = document.getElementById("next");
const createQuestionsForm = document.getElementById("questions");

function nextForm(event){
    event.preventDefault();
    event.currentTarget.parentElement.removeChild(event.currentTarget);
    createQuestionsForm.classList.remove("d-none");
    createQuestionsForm.scrollIntoView({"behavior": "smooth", "block": "end", "inline": "end"});
};

nextButton.addEventListener("click", nextForm);