const conversions = {
    'inches': 0.0254,
    'feet': 0.3048,
    'yards': 0.9144,
    'meters': 1,
    'kilometers': 1000,
    'miles': 1609.34
}


let distance = prompt("What is the distance?")
let inputUnits = prompt("What are the units?")
let outputUnits = prompt("What unit are you converting to?")

let distanceInMeters = (conversions[inputUnits] * distance);
console.log(distanceInMeters);

let distanceInOutputUnits = (distanceInMeters / conversions[outputUnits]);
console.log(distanceInOutputUnits);

alert(`${distance} ${inputUnits} is ${distanceInOutputUnits} ${outputUnits}`)


