const myButton = document.getElementById('myButton')

function rotate() {
    const inputString = document.getElementById('inputString').value
    const rotations = document.getElementById('rotations').value
    const abc = "abcdefghijklmnopqrstuvwxyz"
    let output = ""

    for (let char of inputString) {
        let inputIndex = abc.indexOf(char);
        let outputIndex = (inputIndex - rotations);
        output += abc[outputIndex]
    }

    let result = document.getElementById('resultDiv')
    result.innerHTML = `Original string: ${inputString}; Rotated ${rotations} times; New string: ${output}`

}
myButton.addEventListener('click', rotate)