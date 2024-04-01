const hours = document.getElementById("hours");
const minutes = document.getElementById("minutes");
const seconds = document.getElementById("seconds");
const performer_time = document.getElementById("performer_time");


let splittedTime = new String(testDuration).split(":");

hours.innerText = splittedTime[0].toString().padStart(2, "0");
minutes.innerText = splittedTime[1].toString().padStart(2, "0");
seconds.innerText = splittedTime[2].toString().padEnd(2, "0");

let timeInSeconds = (Number(splittedTime[0]) * 60 * 60) + (Number(splittedTime[1]) * 60) + Number(splittedTime[2]);

setInterval(updateTimeRemains, 1000);

function validTimeFormat(timeValue){
    return timeValue.toString().padStart(2, "0");
};


function updateTimeRemains(){
    const hoursRemains = Math.floor(timeInSeconds / 60 / 60);
    const minutesRemains = Math.floor(timeInSeconds / 60 % 60);
    const secondsRemains = Math.floor(timeInSeconds % 60);
    
    hours.innerText = validTimeFormat(hoursRemains);
    minutes.innerText = validTimeFormat(minutesRemains);
    seconds.innerText = validTimeFormat(secondsRemains);

    performer_time.value = `${timeInSeconds}`;
    timeInSeconds--;
};