const meterConversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
};

function convertToMeters(distance, inputUnits) {
    return meterConversions[inputUnits] * distance;
}

function convertFromMeters(distance, outputUnits) {
    return distance / meterConversions[outputUnits];
}

document.getElementById("convert").addEventListener("click", function () {
    const distance = document.getElementById("distance").value;
    const inputUnits = document.getElementById("inputUnits").value;
    const outputUnits = document.getElementById("outputUnits").value;

    const distanceInMeters = convertToMeters(distance, inputUnits);
    const distanceInOutputUnits = convertFromMeters(distanceInMeters, outputUnits);

    document.getElementById("result").innerHTML = `${distance} ${inputUnits} is ${distanceInOutputUnits.toFixed(7)} ${outputUnits}`;
});
