let inputString = prompt("Please enter a string :").toLowerCase();
let rotation = prompt("Please enter number of rotations: ")
let abc = "abcdefghijklmnopqrstuvwxyz"
let output = ""


for (let char of inputString) {
    let inputIndex = abc.indexOf(char);
    let outputIndex = (inputIndex - rotation);
    if (outputIndex < 0) {
        outputIndex += 26
    }
    output += abc[outputIndex]
}
console.log(output)


alert(`Original string: ${inputString}; Rotated ${rotation} times; New string: ${output}`)
