//Unit Converter//
//Version 1//
// const meter = 0.3048
// let unit = prompt("Enter the number of feet: ")
// const totalMeters = unit * meter

// let output = `${unit} feet is equal to ${totalMeters} meters.`

// alert (output)

//Version 4//
const conversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'meter': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

let inputUnit = prompt("Enter the type of unit you want converted: ft, mi, meter, km, yd, in ")
console.log(inputUnit)


let inputDist = prompt(`How many ${inputUnit} do you want to convert? `)

console.log(inputDist)

let inputConv = inputDist * conversions[inputUnit]

let outputUnit = prompt("Enter the type of unit you want to convert to: ft, mi, meter, km, yd, in ")

let outputConv = inputConv / conversions[outputUnit]

alert(`${inputDist} ${inputUnit} is equal to ${outputConv} ${outputUnit}.`)