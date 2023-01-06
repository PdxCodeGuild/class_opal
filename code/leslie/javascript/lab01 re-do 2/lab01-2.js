const conversions = {
    'inches': 0.0254,
    'feet': 0.3048,
    'yards': 0.9144,
    'meters': 1,
    'kilometers': 1000,
    'miles': 1609.34
}


const myButton = document.getElementById('myButton')
const checkboxes = document.querySelectorAll('input[type=checkbox]')

function convert() {
    const distance = document.getElementById('distance').value
    const inputUnits = document.querySelectorAll('.inputUnits')
    const outputUnits = document.querySelectorAll('.outputUnits')
    const inputChecked = Array.from(inputUnits).filter(el => el.checked)
    const outputChecked = Array.from(outputUnits).filter(el => el.checked)
    const inputValue = inputChecked[0].value
    const outputValue = outputChecked[0].value

    let distanceInMeters = conversions[inputChecked[0].value] * Number(distance);

    let distanceInOutputUnits = distanceInMeters / conversions[outputChecked[0].value];

    let result = document.getElementById('resultDiv')
    result.innerHTML = `${distance} ${inputValue} is ${distanceInOutputUnits} ${outputValue}`


}

myButton.addEventListener('click', convert)
