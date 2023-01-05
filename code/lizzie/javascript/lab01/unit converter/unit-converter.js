const conversionDict = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254
}

const userDistance = parseFloat(prompt('What is the distance being converted?'));
const distance = parseFloat(userDistance);

const inputUnit = prompt('What are the input units?');

const outputUnit = prompt('What are the input units?');

const meterConversion = conversionDict[inputUnit] * distance
const conversion2 = meterConversion / conversionDict[outputUnit]

alert(`${distance} ${inputUnit} is ${conversion2.toFixed(3)} ${outputUnit}`)
