const wrapper = document.getElementById("pageWrapper");
const menuBtn = document.getElementById("menuBtn");

function clearAll(){
    const input = document.getElementById("inputText");
    const result = document.getElementById("resultText");

    if(input) input.value = "";
    if(result) result.innerText = "";
}

function updateLayout(){
    const userOpen = wrapper.classList.contains("user-open");
    const historyOpen = wrapper.classList.contains("history-open");
    const helpOpen = wrapper.classList.contains("help-open");

    wrapper.classList.toggle("both-open", userOpen && (historyOpen || helpOpen));
}

// USER PANEL
function openUser(){
    wrapper.classList.add("user-open");

    if(menuBtn){
        menuBtn.classList.add("hidden");
    }

    updateLayout();
}

function closeUser(){
    wrapper.classList.remove("user-open");

    if(menuBtn){
        menuBtn.classList.remove("hidden");
    }

    updateLayout();
}

// HISTORY PANEL
function openHistory(){
    wrapper.classList.toggle("history-open");
    updateLayout();
}

function closeHistory(){
    wrapper.classList.remove("history-open");
    updateLayout();
}

// HELP PANEL
function openHelp(){
    wrapper.classList.add("help-open");
    updateLayout();
}

function closeHelp(){
    wrapper.classList.remove("help-open");
    updateLayout();
}

// AUDIO
function playMorse(){
    const text = document.getElementById("resultText").innerText.trim();
    if(!text) return;

    let unit = 250;

    const context = new (window.AudioContext || window.webkitAudioContext)();
    let time = context.currentTime;

    function beep(duration){
        const oscillator = context.createOscillator();
        const gain = context.createGain();

        oscillator.type = "sine";
        oscillator.frequency.value = 600;

        oscillator.connect(gain);
        gain.connect(context.destination);

        oscillator.start(time);
        oscillator.stop(time + duration);

        time += duration + (unit / 1000);
    }

    for(let char of text){
        if(char === "."){
            beep(unit / 1000);
        }
        else if(char === "-"){
            beep((unit * 3) / 1000);
        }
        else if(char === "/"){
            time += (unit * 3) / 1000;
        }
        else{
            time += unit / 1000;
        }
    }
}