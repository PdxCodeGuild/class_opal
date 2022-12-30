const meterConversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
};

const distance = prompt("What is the distance?");
const inputUnits = prompt("What are the input units?");
const outputUnits = prompt("What are the output units?");

function convertToMeters(distance, inputUnits) {
    return meterConversions[inputUnits] * distance;
}

function convertFromMeters(distance, outputUnits) {
    return distance / meterConversions[outputUnits];
}

const distanceInMeters = convertToMeters(distance, inputUnits);
const distanceInOutputUnits = convertFromMeters(distanceInMeters, outputUnits);

alert(`${distance} ${inputUnits} is ${distanceInOutputUnits.toFixed(7)} ${outputUnits}`);
