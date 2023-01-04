// Unit Converter Part B

let userDistance = document.getElementById('user distance')
userDistance = parseInt(userDistance)
const unitsInput = document.getElementById('units input')
const unitsOutput = document.getElementById('units output')
conversion = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254}
const newDistance = userDistance * conversion[unitsInput]
const newUnits = newDistance / conversion[unitsOutput]
// alert(`${userDistance} ${unitsInput} is ${newUnits} ${unitsOutput}.`)