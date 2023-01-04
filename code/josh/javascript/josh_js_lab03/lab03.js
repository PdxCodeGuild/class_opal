// Python Lab 3 Version 2

let numList = []

while (true) {
    let userInput = prompt("Enter number or 'done' to quit: ")
    if (userInput == 'done') {
        alert(`The average is: ${average}`)
        break
    }
    else {
        userInput = parseInt(userInput)
        numList.push(userInput)
        let average = sum(numList)/numList.length
    }}