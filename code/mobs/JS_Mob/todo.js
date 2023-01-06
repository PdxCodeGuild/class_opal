


// select all of the elements we need to change and/or listen to
const new_item = document.getElementById('new_item').value
const myButton = document.querySelector('#button')
// const checkboxes = document.querySelectorAll('input[type=checkbox]')

// const completed_list = document.create

const completedList = []
const incompleteList = ['check that code works', 'a', 'b', 'check for back ticks']

// check whether the button should be disabled or not
// const checkValidity = () => {
//     const checked = Array.from(checkboxes).filter(el => el.checked)
//     if (checked.length > 0 && voter.value) {
//         myButton.removeAttribute('disabled')
//     } else {
//         myButton.setAttribute('disabled', true)
//     }
// }

for(item of incompleteList) {
    const newDiv = document.createElement('div')
    const checkbox = document.createElement('input')
    checkbox.type='checkbox'
    checkbox.id=`checkbox${incompleteList.indexOf(item)}`
    const input = document.createTextNode(item)
    const deleteButton = document.createElement('button')
    deleteButton.id=`delete${incompleteList.indexOf(item)}`
    deleteButton.innerText='delete'
    newDiv.appendChild(checkbox)
    newDiv.appendChild(input)
    newDiv.appendChild(deleteButton)
    const literallyAnything = document.getElementById('new_todo')
    document.body.after(newDiv, literallyAnything)

    // create element div
    // create element checkbox
    // create element input
    // create element button with innertext delete
    // append child to go inside div
    // publish in line
}

myButton.addEventListener('click', () => {
    incompleteList.push(querySelector("#newItem").value)

    // Take input and push to the events
    alert('Here!')
    alert(`${incompleteList}`)
})