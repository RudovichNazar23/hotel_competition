const pageAccessedByReload = (
    (window.performance.navigation && window.performance.navigation.type === 1) ||
        window.performance
        .getEntriesByType('navigation')
        .map((nav) => nav.type)
        .includes('reload')
);
if(pageAccessedByReload){
    const userAnswers = JSON.parse(localStorage.getItem("answers"));
    
    for(let userAnswer of userAnswers){
        const answerInputObject = document.getElementById(userAnswer.answerContent);
        answerInputObject.checked = true;
    };
};
