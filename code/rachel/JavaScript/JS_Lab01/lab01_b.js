//Unit Converter//

//Version 1//
// const meter = 0.3048
// const inputNum = document.getElementById('inputNum')
// const submit = document.querySelector('input[type=button]')

// const output = () => {
//     const inputNum = document.getElementById('inputNum').value //use .value to get the actual value from inputNum
//     const meter = 0.3048
//     const totalMeters = meter * inputNum
//     let outputNum = `${inputNum} feet is equal to ${totalMeters} meters.`

//     console.log(outputNum)
// }
// submit.addEventListener('click', output) //1) the function needs to be called in the event listener 2) Order matters: event listener should come after function

// Version 4
const conversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'meter': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}
const submit = document.querySelector('input[type=button]')
const convert = document.querySelector('input[type=button]')

function conversion() {

    const inputUnit = document.getElementById('inputUnit').value
    const inputDist = document.getElementById('inputDist').value
    let inputConv = inputDist * conversions[inputUnit]
    const outputUnit = document.getElementById('outputUnit').value
    let outputConv = inputConv / conversions[outputUnit]
    //console.log(outputConv)
    alert(`${inputDist} ${inputUnit} is equal to ${outputConv} ${outputUnit}.`)
}

convert.addEventListener('click', conversion) 
