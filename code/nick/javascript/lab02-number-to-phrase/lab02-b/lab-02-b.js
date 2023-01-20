const intWordsObj = {
    0: [''],
    1: ['one', '', 'one-hundred'],
    2: ['two', 'twenty', 'two-hundred'],
    3: ['three', 'thirty', 'three-hundred'],
    4: ['four', 'forty', 'four-hundred'],
    5: ['five', 'fifty', 'five-hundred'],
    6: ['six', 'sixty', 'six-hundred'],
    7: ['seven', 'seventy', 'seven-hundred'],
    8: ['eight', 'eighty', 'eight-hundred'],
    9: ['nine', 'ninety', 'nine-hundred'],
    10: ['ten'],
    11: ['eleven'],
    12: ['twelve'],
    13: ['thirteen'],
    14: ['fourteen'],
    15: ['fifteen'],
    16: ['sixteen'],
    17: ['seventeen'],
    18: ['eighteen'],
    19: ['nineteen'],
    1000: ['one thousand'],
}

const intRomanObj = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}

function intToWords(num) {
    console.log(num)
    if (Object.keys(intWordsObj).includes(num.toString())) 
        {return intWordsObj[num][0]}
    else { 
        const hundred = Math.floor(num / 100)
        
        if (hundred === 0) {
            const ten = Math.floor(num / 10)
            const one = num % 10
            const tenWord = intWordsObj[ten][1]
            const oneWord = intWordsObj[one][0]
            return `${tenWord}-${oneWord}`
        }   
        else {
            const hundredWord = intWordsObj[hundred][2]
            num = num%100
            return `${hundredWord} ${intToWords(num)}`
        }
    }
        
}


function intToRoman(num) {
    const resolutionOrder = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    let romanComplete = []
    for (x of resolutionOrder) {
        if (num != 0) {
            const quotient = Math.floor(num/x)
            if (quotient != 0) {
                for (let y = 0; y < quotient; y++) {romanComplete.push(intRomanObj[x])}
            }
            num = num % x
        }
    }
    return romanComplete.toString()
}


function timeConverter(time) {
    const timeSplit = time.split(':')
    console.log(timeSplit)
    const hourInt = parseInt(timeSplit[0])
    console.log(hourInt)
    const minuteInt = parseInt(timeSplit[1])
    console.log(minuteInt)
    const hourPhrase = intToWords(hourInt)
    const hourRoman = intToRoman(hourInt)
    const minutePhrase = intToWords(minuteInt)
    const minuteRoman = intToRoman(minuteInt)
    return `${hourPhrase} : ${minutePhrase}\n${hourRoman} : ${minuteRoman}`
}



function numberConverter(request) {
    const phrase = intToWords(request)
    const roman = intToRoman(request)
    return `${phrase}\n${roman}`
}


const button = document.querySelector('#button')


const convert = () => {
    const request = document.querySelector('#number').value
    
    if (request.includes(':')) {
        const endNumber = timeConverter(request)
        document.querySelector('#result').innerText = endNumber
    }
    else if (!parseInt(request)) {
        const endNumber = 'zero'
        document.querySelector('#result').innerText = endNumber
    }
    else {
        const endNumber = numberConverter(request)
        document.querySelector('#result').innerText = endNumber
    } 
}

button.addEventListener('click', () => { convert() })
