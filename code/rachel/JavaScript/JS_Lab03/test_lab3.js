let keys = "abcdefghijklmnopqrstuvwxyz"
//let keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
let input = prompt("What letters or word do you want to encrypt? ")
let userWord = input.toLowerCase('input')
//console.log(userWord)
let n = parseInt(prompt("Enter the cipher rotation amount (1-25): "))
//console.log(typeof n)
let output = ''

for (let i = 0; i < userWord.length; i++) {
    //let oldIndex = keys.findIndex(i) // array
    //console.log(userWord[i])
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