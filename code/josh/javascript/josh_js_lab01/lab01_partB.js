// Unit Converter Part B
let converter = document.getElementById('converter')
converter.addEventListener('click', convert)
function convert() {
    let userDistance = document.getElementById('user_distance').value
    userDistance = parseInt(userDistance)
    const unitsInput = document.getElementById('units_input').value
    console.log(unitsInput)
    const unitsOutput = document.getElementById('units_output').value
    const conversion = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254}
    const newDistance = userDistance * conversion[unitsInput]
    const newUnits = newDistance / conversion[unitsOutput]
    document.getElementById("converted_units").innerText = `${userDistance} ${unitsInput} is ${newUnits} ${unitsOutput}.`
}