// Unit Converter Part B

let userDistance = document.getElementById('user distance')
userDistance = parseInt(userDistance)
const unitsInput = document.getElementById('units input')
const unitsOutput = document.getElementById('units output')
const conversion = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254}
const newDistance = userDistance * conversion[unitsInput]
console.log(newDistance)
const newUnits = newDistance / conversion[unitsOutput]
function convert() {
    document.getElementById("converted units").innerHTML = `${userDistance} ${unitsInput} is ${newUnits} ${unitsOutput}.`
}