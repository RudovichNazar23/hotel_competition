document.onvisibilitychange = () => {
    if(document.visibilityState === "hidden"){
        document.getElementById("submit_button").click();
    };
};