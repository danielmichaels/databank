var endDate = new Date("Feb 1 2021").getTime();
console.log(endDate)

var timer = setInterval(() => {
    let now = new Date().getTime();
    let timeLeft = endDate - now;

    if (timeLeft >= 0) {
        let days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        let hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
        let minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60))
        let seconds = Math.floor((timeLeft % (1000 * 60)) / 1000)

        document.getElementById("timer-days").innerHTML = days + "<span class='label'>:</span>"

        document.getElementById("timer-hours").innerHTML = ("0" + hours).slice(-2) + "<span class='label'>:</span>"

        document.getElementById("timer-minutes").innerHTML = ("0" + minutes).slice(-2) + "<span class='label'>:</span>"

        document.getElementById("timer-seconds").innerHTML = ("0" + seconds).slice(-2) + "<span class='label'></span>"

    } else {
        document.getElementById("timer").innerHTML = "Times up!"
    }
}, 1000);
