// Python to JS Lab 3 Part B

let average = document.getElementById('average')
average.addEventListener('click', findAverage)
let reset = document.getElementById('reset')
reset.addEventListener('click', resetNumArr)
let numArr = []

function findAverage() {
    let number = document.getElementById('number').value
    if (number == 'done') {
        document.getElementById('number').value = ''
        return document.getElementById("output").innerText = `The average is: ${average}. Click reset to start over.`
    }
    else if (isNaN(number)) {
        document.getElementById('number').value = ''
        document.getElementById('output').innerText = 'You didn\'t make a valid entry.  Click reset and try again.'
    }
    else {
        number = parseInt(number)
        numArr.push(number)
        let numRedArr = numArr.reduce((x, y) => x + y)
        average = numRedArr/numArr.length
        document.getElementById('number').value = ''
        return document.getElementById("output").innerText = `The average is: ${average}.  Enter another number to continue averaging or 'done' to quit.`
    }}
    
function resetNumArr() {
    numArr = []
    document.getElementById('number').value = ''
    document.getElementById('output').innerText = ''

}