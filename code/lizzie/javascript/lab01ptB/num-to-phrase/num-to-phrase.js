const userHour = document.getElementById('hour');
const userMinute = document.getElementById('minute');
const run_bt = document.querySelector('#run_bt');
const outputPhrase = document.querySelector('#output_phrase');

run_bt.onclick = function() {
    const hoursList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'noon', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    const onesList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    const tensList = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty']

    hour = userHour.value
    minute = userMinute.value
    const onesDigit = minute%10
    const tensDigit = Math.floor((minute / 10) % 10)

    if (onesDigit == 0 && tensDigit == 0) {
        if (hour < 12) {
            outputPhrase.innerText = `Good morning! The time is ${hoursList[hour]} a.m.!`;
        } else if (hour == 12) {
            outputPhrase.innerText = `It is noon!`;
        } else if (hour == 24) {
            outputPhrase.innerText = `It is midnight. Go to bed!`;
        } else if (hour > 12 && hour < 19) {
            outputPhrase.innerText = `Good afternoon! The time is ${hoursList[hour]} p.m.!`;
        } else {
            outputPhrase.innerText = `Good evening. The time is ${hoursList[hour]} p.m.!`;
        }
    } else if (tensDigit == 0) {
        outputPhrase.innerText = `The time is ${hoursList[hour]}-oh-${onesList[minute]}.`;
    } else if (minute < 20) {
        outputPhrase.innerText = `The time is ${hoursList[hour]}-${onesList[minute]}.`;
    } else if (onesDigit == 0) {
        outputPhrase.innerText = `The time is ${hoursList[hour]} ${tensList[tensDigit]}.`;
    } else {
        outputPhrase.innerText = `The time is ${hoursList[hour]} ${tensList[tensDigit]}-${onesList[onesDigit]}`;
    }
}
