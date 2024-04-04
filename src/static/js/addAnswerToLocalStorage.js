if(!localStorage.getItem("answers")){
    localStorage.setItem("answers", JSON.stringify([]));
};

function addAnswerToLocalStorage(event){
    const questionContent = event.currentTarget.name;
    const answerContent = event.currentTarget.value;

    const userAnswers = JSON.parse(localStorage.getItem("answers"));
    
    const selectedAnswer = userAnswers.filter((oldAnswer) => oldAnswer.questionContent === questionContent);

    selectedAnswer.length > 0
    ?
        userAnswers[userAnswers.indexOf(selectedAnswer[0])].answerContent = answerContent
    :
        userAnswers.push({"answerContent": answerContent, "questionContent": questionContent});

    localStorage.setItem("answers", JSON.stringify(userAnswers));
};

const answers = Array.from(document.body.querySelectorAll("input[type=radio]"));

answers.map(
    (answerInputObject) => {
        answerInputObject.addEventListener("click", addAnswerToLocalStorage);
    }
);
