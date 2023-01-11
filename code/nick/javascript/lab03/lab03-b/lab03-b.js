const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        
function ceasar(startText, shiftAmount, cipherDirection) {
    let endText = ''
    while (shiftAmount >= 26) { shiftAmount = shiftAmount % 26 }
    if (cipherDirection == 'decode') { shiftAmount *= -1 }
    for (char of startText) {
        console.log(char)
        let newChar = char
        if (alphabet.includes(char)) {
            newChar = alphabet[alphabet.indexOf(char) + shiftAmount]
            console.log(newChar)
        }
        endText += newChar
        console.log(endText)
    }
    const endResult = [cipherDirection, endText]
    return endResult
}

const button = document.querySelector('#run')


const cipher = () => {
    console.log('Hello')
    const text = document.querySelector('#start-text').value.toLowerCase()
    console.log(text)
    const shift = parseInt(document.querySelector('#shift').value)
    console.log(shift)
    const direction = document.querySelector('#direction').value.toLowerCase()
    console.log(direction)
    const result = ceasar(text, shift, direction)
    console.log(result)
    document.querySelector('#result').innerText = `Your ${result[0]}d message is ${result[1]}`
}

button.addEventListener('click', cipher )
// console.log(button)