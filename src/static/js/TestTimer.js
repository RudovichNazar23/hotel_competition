
const hours = document.getElementById("hours");
const minutes = document.getElementById("minutes");
const seconds = document.getElementById("seconds");


let splittedTime = new String(testDuration).split(":");

hours.innerText = splittedTime[0].toString().padStart(2, "0");
minutes.innerText = splittedTime[1].toString().padStart(2, "0");
seconds.innerText = splittedTime[2].toString().padEnd(2, "0");

let timeInSeconds = (Number(splittedTime[0]) * 60 * 60) + (Number(splittedTime[1]) * 60) + Number(splittedTime[2]);

setInterval(updateTimeRemains, 1000);

function updateTimeRemains(){
    const hoursRemains = Math.floor(timeInSeconds / 60 / 60);
    const minutesRemains = Math.floor(timeInSeconds / 60 % 60);
    const secondsRemains = Math.floor(timeInSeconds % 60);
    
    hours.innerText = hoursRemains.toString().padStart(2, "0");
    minutes.innerText = minutesRemains.toString().padStart(2, "0");
    seconds.innerText = secondsRemains.toString().padStart(2, "0");

    timeInSeconds--;
};