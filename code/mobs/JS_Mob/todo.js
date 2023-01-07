const new_item = document.getElementById('new_item').value
const myButton = document.querySelector('#button')
const completedList = []
const incompleteList = []

function incompleteListFunction () {
    for(item of incompleteList) {
        const newDiv = document.createElement('div')
        const container = document.querySelector('#container')
        const checkbox = document.createElement('input')
        checkbox.type='checkbox'
        checkbox.id=`checkbox${incompleteList.indexOf(item)}`
        const input = document.createTextNode(item)
        const deleteButton = document.createElement('button')
        deleteButton.id=`delete-${incompleteList.indexOf(item)}`
        deleteButton.innerText='delete'
        newDiv.appendChild(checkbox)
        newDiv.appendChild(input)
        newDiv.appendChild(deleteButton)
        container.appendChild(newDiv)
}}

document.body.onload = incompleteListFunction()
myButton.addEventListener('click', () => {
    incompleteList.push(document.getElementById("new_item").value)
    while (document.getElementById('container').firstElementChild) {
        document.getElementById('container').firstElementChild.remove()
    }
    incompleteListFunction()
})

deleteButton.addEventListener('click', () => { 
const deleteIndex = deleteButton.id.split('-')[1]
deleteIndex.remove()
completedList = []
completedList.appendChild()
})