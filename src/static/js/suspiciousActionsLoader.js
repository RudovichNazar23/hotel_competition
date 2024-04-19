if(!localStorage.getItem("suspiciousActions")){
    localStorage.setItem("suspiciousActions", JSON.stringify(0))
};

const suspiciousActionsInput = document.getElementById("suspicious_actions");

suspiciousActionsInput.value = JSON.parse(localStorage.getItem("suspiciousActions"));

function parseSuspiciousActions(){
    const suspiciousActions = JSON.parse(localStorage.getItem("suspiciousActions"));
    return suspiciousActions;
};

function setSuspiciousActions(value){
    localStorage.setItem("suspiciousActions", JSON.stringify(value));
    suspiciousActionsInput.value = parseSuspiciousActions();
};

