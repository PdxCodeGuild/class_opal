//Rot 13//
let keys = "abcdefghijklmnopqrstuvwxyz"
let input = prompt("What letters or word do you want to encrypt? ")
let userWord = input.toLowerCase('input')
let n = parseInt(prompt("Enter the cipher rotation amount (1-25): "))
let output = ''

for (let i = 0; i < userWord.length; i++) {
    let oldIndex = keys.indexOf(userWord[i]) // string
    console.log(oldIndex)
    let newIndex = oldIndex + n
    if (newIndex > 26) {
        newIndex = newIndex % 26
    }
    let newLetter = keys.charAt(newIndex)
    output += newLetter
}
alert(output)