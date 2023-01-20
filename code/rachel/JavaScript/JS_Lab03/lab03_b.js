//ROT Cipher
let keys = "abcdefghijklmnopqrstuvwxyz"
const encrypt = document.querySelector('input[type=button]')

function cipher() {
    const input = document.getElementById('input').value
    const n = parseInt(document.getElementById('n').value)
    let userWord = input.toLowerCase('input')
    let output = ''
    for (let i = 0; i < userWord.length; i++) {
        let oldIndex = keys.indexOf(userWord[i])
        //console.log(oldIndex)
        let newIndex = oldIndex + n
        if (newIndex > 26) {
            newIndex = newIndex % 26
        }
        let newLetter = keys.charAt(newIndex)
        output += newLetter
    }
    const body = document.querySelector('body')
    const encryptedWord = document.createElement('encryptedWord')
    encryptedWord.innerText = `Your encrypted word is ${output}.`
    body.appendChild(encryptedWord)
}
encrypt.addEventListener('click', cipher)


