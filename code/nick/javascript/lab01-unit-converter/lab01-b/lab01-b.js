function measurementConverter(distance, start, end) {
    const meterConversionTable = {
        'in': .0254,
        'ft': .3048,
        'yd': .9144,
        'm': 1,
        'km': 1000,
        'mi':1609.34,
    }

    let meters = distance * meterConversionTable[start]
    let distanceEnd = meters / meterConversionTable[end]
    return distanceEnd
}


const validInputs = "in, ft, yd, m, km, mi"

document.querySelector('#unitStart').placeholder = validInputs
document.querySelector('#unitEnd').placeholder = validInputs


const button = document.querySelector('#button')

const calculate = () => {
    const distanceStart = document.querySelector('#startDistance').value
    const unitStart = document.querySelector('#unitStart').value
    const unitEnd = document.querySelector('#unitEnd').value
    const distanceEnd = measurementConverter(distanceStart, unitStart, unitEnd).toFixed(3)
    if (distanceEnd != NaN) {
        document.querySelector('#result').innerText = `${distanceStart} ${unitStart} = ${distanceEnd} ${unitEnd}`
    }
}

button.addEventListener('click', () => { calculate() })

