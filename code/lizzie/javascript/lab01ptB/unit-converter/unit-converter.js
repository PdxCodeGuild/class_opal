const distance = document.getElementById('distance');
const userInputUnit = document.getElementById('input_unit');
const userOutputUnit = document.getElementById('output_unit');
const run_bt = document.querySelector('#run_bt');
const outputAdvice = document.querySelector('#output_advice');

run_bt.onclick = function() {
    const userDistance = distance.value
    const inputUnit = userInputUnit.value
    const outputUnit = userOutputUnit.value

    const conversionDict = {
        ft: 0.3048,
        mi: 1609.34,
        m: 1,
        km: 1000,
        yd: 0.9144,
        in: 0.0254
    }

    const meterConversion = conversionDict[inputUnit] * userDistance
    const conversion2 = meterConversion / conversionDict[outputUnit]

    outputAdvice.innerText = `${userDistance} ${inputUnit} is ${conversion2.toFixed(2)} ${outputUnit}`
}