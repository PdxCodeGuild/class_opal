// Python to JS Lab 3 Part B

const average = document.getElementById('average')
average.addEventListener('click', findAverage)
const reset = document.getElementById('reset')
reset.addEventListener('click', resetNumArr)
let numArr = []


function findAverage() {
    let number = document.getElementById('number').value
    if (number == 'done') {
        return document.getElementById("output").innerText = `The average is: ${average}. Click reset to start over.`
    }
    else {
        number = parseInt(number)
        numArr.push(number)
        let numRedArr = numArr.reduce((x, y) => x + y)
        average = numRedArr/numArr.length
        return document.getElementById("output").innerText = `The average is: ${average}.  Enter another number to continue averaging or 'done' to quit.`
    }}

    
function resetNumArr() {
    numArr = []
}