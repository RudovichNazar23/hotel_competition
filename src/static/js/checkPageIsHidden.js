document.onvisibilitychange = () => {
    if(document.visibilityState === "hidden"){
        let suspiciousActionsAmount = parseSuspiciousActions();
        suspiciousActionsAmount += 1;
        setSuspiciousActions(suspiciousActionsAmount);
    };
};