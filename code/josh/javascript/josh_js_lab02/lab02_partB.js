// Lab 2 Python to JS: Number to Phrase (Handle numbers from 0-999)

let converter = document.getElementById('converter')
converter.addEventListener('click', convert)
function convert() {
    let number = document.getElementById('number').value
    const numberListTo19 = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    const numberListForTeensOver100 = {
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    const numberListByTens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    const numberListByTensOver100 = {
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }
    const tensPlaceNumberList = {
        0: "",
        2: "twenty-",
        3: "thirty-",
        4: "forty-",
        5: "fifty-",
        6: "sixty-",
        7: "seventy-",
        8: "eighty-",
        9: "ninety-"
    }
    const hundredsPlaceNumberList = {
        1: "one hundred",
        2: "two hundred",
        3: "three hundred",
        4: "four hundred",
        5: "five hundred",
        6: "six hundred",
        7: "seven hundred",
        8: "eight hundred",
        9: "nine hundred"
    }
    unitsPlace = number%10
    tensPlace = Math.floor(number/10)
    hundredsPlace = Math.floor(number/100)
    hundredsRemainder = Math.floor(number%100/10)
    unitsRemainder = number%100%10
    teensRemainder = number%100

    if (number < 0) {
        alert("Your entry is invalid.  You did not enter a number from 0 to 999.")
    } else if (number == 0) {
        alert("0 is written out as zero.")
    } else if (number <= 19) {
        alert(`${number} is written out as ${numberListTo19[number]}.`)
    } else if (number == 20 || number == 30 || number == 40 || number == 50 || number == 60 || number == 70 || number == 80 || number == 90) {
        alert(`${number} is written out as ${numberListByTens[number]}.`)
    } else if (number >= 21 && number <= 99) {
        alert(`${number} is written out as ${tensPlaceNumberList[tensPlace]}${numberListTo19[unitsPlace]}.`)
    } else if (number >= 100 && number <= 999) {
        if (number == 100 || number == 200 || number == 300 || number == 400 || number == 500 || number == 600 || number == 700 || number == 800 || number == 900) {
            alert(`${number} is written out as ${hundredsPlaceNumberList[hundredsPlace]}`)
        } else if (unitsRemainder == 0) {
            alert(`${number} is written out as ${hundredsPlaceNumberList[hundredsPlace]} ${numberListByTensOver100[hundredsRemainder]}`)
        } else if (hundredsRemainder == 1) {
            alert(`${number} is written out as ${hundredsPlaceNumberList[hundredsPlace]} ${numberListForTeensOver100[teensRemainder]}`)
        } else {
            alert(`${number} is written out as ${hundredsPlaceNumberList[hundredsPlace]} ${tensPlaceNumberList[hundredsRemainder]}${numberListTo19[unitsRemainder]}.`)
        }
    } else {
        alert("Your entry is invalid.  You did not enter a number from 0 to 999.")
    }}