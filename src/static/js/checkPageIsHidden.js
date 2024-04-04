document.onvisibilitychange = () => {
    if(document.visibilityState === "hidden"){
        alert("Current tab was hidden!!!");
    };
};