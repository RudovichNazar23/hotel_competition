document.onvisibilitychange = () => {
    if(document.visibilityState === "hidden"){
//        document.getElementById("submit_button").click();
        alert("Current tab was hidden!!!");
    };
};