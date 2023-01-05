// Python to JS Lab 3 Part B

let average = document.getElementById('average')
average.addEventListener('click', findAverage)
function findAverage() {
    let number = document.getElementById('number')
    let numArr = []
    while (true) {
        if (number == 'done') {
            document.getElementById("output").innerText = `The average is: ${average}.`
            break
        }
        else {
            number = parseInt(number)
            numArr.push(number)
            let numRedArr = numArr.reduce((x, y) => x + y)
            average = numRedArr/numArr.length
        }}}