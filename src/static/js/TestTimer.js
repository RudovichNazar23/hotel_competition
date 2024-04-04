const hours = document.getElementById("hours");
const minutes = document.getElementById("minutes");
const seconds = document.getElementById("seconds");
const performer_time = document.getElementById("performer_time");
const submitButton = document.getElementById("submit_button");
const durationInfo = document.getElementById("duration_info");

let splittedTime = new String(testDuration).split(":");

hours.innerText = validTimeFormat(splittedTime[0]);
minutes.innerText = validTimeFormat(splittedTime[1]);
seconds.innerText = validTimeFormat(splittedTime[2]);

durationInfo.innerText = `${validTimeFormat(splittedTime[0])} : ${validTimeFormat(splittedTime[1])} : ${validTimeFormat(splittedTime[2])}`;

let timeInSeconds =
  Number(splittedTime[0]) * 60 * 60 +
  Number(splittedTime[1]) * 60 +
  Number(splittedTime[2]);

if(!localStorage.getItem("timeinSecondsRemains")){
  localStorage.setItem("timeinSecondsRemains", timeInSeconds)
};

timeInSeconds = Number(localStorage.getItem("timeinSecondsRemains"));

setInterval(updateTimeRemains, 1000);

function validTimeFormat(timeValue) {
  return timeValue.toString().padStart(2, "0");
};

function updateTimeRemains() {
  if(timeInSeconds < 0){
    submitButton.click();
  }
  else{
    const hoursRemains = Math.floor(timeInSeconds / 60 / 60);
    const minutesRemains = Math.floor((timeInSeconds / 60) % 60);
    const secondsRemains = Math.floor(timeInSeconds % 60);

    hours.innerText = validTimeFormat(hoursRemains);
    minutes.innerText = validTimeFormat(minutesRemains);
    seconds.innerText = validTimeFormat(secondsRemains);

    performer_time.value = `${timeInSeconds}`;
    localStorage.setItem("timeinSecondsRemains", timeInSeconds--);
  };
}
