// Python to JS Lab 3 Part B

let average = document.getElementById('average')
average.addEventListener('click', findAverage)
function findAverage() {
    let number = document.getElementById('number').value
    let numArr = []
    while (true) {
        let userInput = prompt("Enter number or 'done' to quit: ")
        if (userInput == 'done') {
            alert(`The average is: ${average}`)
            break
        }
        else {
            userInput = parseInt(userInput)
            numArr.push(userInput)
            let numRedArr = numArr.reduce((x, y) => x + y)
            average = numRedArr/numArr.length
        }}}