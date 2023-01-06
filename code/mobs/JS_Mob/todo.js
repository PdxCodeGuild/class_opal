


// select all of the elements we need to change and/or listen to
const new_item = document.getElementById('new_item').value
const button = document.querySelector('input[type=button]')
// const checkboxes = document.querySelectorAll('input[type=checkbox]')
button.addEventListener('click',)

// const completed_list = document.create

const completed_list = []
const incomplete_list = []



// check whether the button should be disabled or not
const checkValidity = () => {
    const checked = Array.from(checkboxes).filter(el => el.checked)
    if (checked.length > 0 && voter.value) {
        button.removeAttribute('disabled')
    } else {
        button.setAttribute('disabled', true)
    }
}
button.addEventListener('click', new_item)