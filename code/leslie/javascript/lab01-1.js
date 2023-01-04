const conversions = {
    'inch': 0.0254,
    'feet': 0.3048,
    'yard': 0.9144,
    'meter': 1,
    'kilometer': 1000,
    'mile': 1609.34
}


let distance = prompt("What is the distance?")
let inputUnits = prompt("What are the units?")
let outputUnits = prompt("What unit are you converting to?")

let distanceInMeters = (conversions[inputUnits] * distance);
console.log(distanceInMeters);

let distanceInOutputUnits = (distanceInMeters / conversions[outputUnits]);
console.log(distanceInOutputUnits);

alert(`${distance} ${inputUnits} is ${distanceInOutputUnits} ${outputUnits}`)


