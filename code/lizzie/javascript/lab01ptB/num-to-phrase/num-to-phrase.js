alert(`Welcome to the number to phrase converter!
The site will prompt you for an hour and minute and return the time in text.
Thank you!
(Please note for times in the afternoon, please enter it using military time)`)
const hour = parseInt(prompt("Please give your current hour (in military time): "))
const minute = parseInt(prompt("Please give your current minute: "))

const onesDigit = minute%10
const tensDigit = Math.floor((minute / 10) % 10)
// console.log(`${onesDigit}`)
// console.log(tensDigit)

const hoursList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'noon', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
const onesList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
const tensList = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty']

if (onesDigit == 0 && tensDigit == 0) {
    if (hour < 12) {
        alert(`Good morning! The time is ${hoursList[hour]} a.m.!`)
    } else if (hour == 12) {
        alert(`It is noon!`)
    } else if (hour == 24) {
        alert(`It is midnight. Go to bed!`)
    } else if (hour > 12 && hour < 19) {
        alert(`Good afternoon. The time is ${hoursList[hour]} p.m..`)
    } else {
        alert(`Good evening. The time is ${hoursList[hour]} p.m..`)
    }
} else if (tensDigit == 0) {
    alert(`The time is ${hoursList[hour]}-oh-${onesList[minute]}.`)
} else if (minute < 20) {
    alert(`The time is ${hoursList[hour]}-${onesList[minute]}.`)
} else if (onesDigit == 0) {
    alert(`The time is ${hoursList[hour]} ${tensList[tensDigit]}.`)
} else {
    alert(`The time is ${hoursList[hour]} ${tensList[tensDigit]}-${onesList[onesDigit]}.`)
}