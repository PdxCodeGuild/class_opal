// use event listeners to detect user interactions with an element
const box = document.getElementById('box')
box.classList.add('red')
box.addEventListener('mouseover', () => console.log('we moused over'))
box.addEventListener('click', () => box.classList.toggle('red'))


// select all of the elements we need to change and/or listen to
const voter = document.getElementById('voter')
const button = document.querySelector('input[type=button]')
const checkboxes = document.querySelectorAll('input[type=checkbox]')


// check whether the button should be disabled or not
const checkValidity = () => {
    const checked = Array.from(checkboxes).filter(el => el.checked)
    if (checked.length > 0 && voter.value) {
        button.removeAttribute('disabled')
    } else {
        button.setAttribute('disabled', true)
    }
}

// add event listeners to check validity when input fields change
voter.addEventListener('input', () => { checkValidity() })
checkboxes.forEach(el => {
    el.addEventListener('change', () => { checkValidity() })
})

// this stuff all happens when we click the "vote" button
const voters = []
const vote = () => {
    const warning = document.getElementById('warning')

    // raise warning and exit if invalid voter
    const studentNodes = document.querySelectorAll('li')
    const students = Array.from(studentNodes).map(el => el.innerText)
    if (!students.includes(voter.value)) {
        warning.innerText = "Only students in Class Opal are allowed to vote"
        return
    }

    // raise warning and exit if user already voted
    if (voters.includes(voter.value)) {
        warning.innerText = "You can't vote more than once"
        return
    }

    // track voter
    voters.push(voter.value)
    document.getElementById(voter.value).classList.add('voted')

    // find checked boxes and increment tally
    const checked = Array.from(checkboxes).filter(el => el.checked)
    checked.forEach(el => {
        const tally = document.getElementById(el.value)
        tally.innerText++
    })

    // clear values
    checkboxes.forEach(el => el.checked = false)
    voter.value = ''
    warning.innerText = ''

    // change to a random image
    const image = document.querySelector('img')
    image.src = `static/logo${Math.ceil(Math.random() * 3)}.png`
}

button.addEventListener('click', vote)
