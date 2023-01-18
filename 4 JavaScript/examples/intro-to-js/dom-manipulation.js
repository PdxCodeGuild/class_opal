const header = document.querySelector('h3') // returns the first match it encounters (DON'T RELY ON THIS)
header.innerText = 'hello world :) '
header.innerHTML = "Class Opal <i>rules</i>"

const students = document.querySelectorAll('li') // returns a NodeList
let span = document.querySelectorAll('span') // also returns a NodeList even though there's just one
span[0].style.fontSize = '1.5em'

const subheader = document.querySelector('#subheader')
//const subheader = document.getElementById('subheader')
console.log(subheader)

//subheader.name = 'students-list'
subheader.style.color = 'red'

for (element of students) {
    if (element.innerText == 'Nick') {
        element.classList.add('freaky-super-genius')
    }
    if (element.innerText == 'Lizzie') {
        element.classList.remove('freaky-super-genius')
    }
    if (element.innerText == 'Jim') {
        element.classList.replace('super-genius', 'freaky-super-genius')
    }
}

const geniuses = document.querySelectorAll('.freaky-super-genius')
for (el of geniuses) {
    el.style.color = 'purple'
}

// Change HTML attributes
console.log(subheader.hasAttribute('name')) // false
console.log(subheader.getAttribute('name')) // null
subheader.setAttribute('name', 'class description')
console.log(subheader.hasAttribute('name')) // true
console.log(subheader.getAttribute('name')) // class description

subheader.removeAttribute('name')
console.log(subheader.hasAttribute('name')) // false
console.log(subheader.getAttribute('name')) // null


// Create and add element
const quote = document.createElement('blockquote')
quote.innerHTML = "It's better to remain silent and be thought a fool than to open your mouth and remove all doubt... PSYCH, don't think like this"
console.log(quote)

//const body = document.getElementsByTagName('body')[0]
const body = document.querySelector('body')
console.log(body)

body.appendChild(quote)

const abc = document.createElement('abc')
abc.innerText = 'will this work?'
body.appendChild(abc)