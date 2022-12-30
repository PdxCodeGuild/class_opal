document.getElementById("submit-button").addEventListener("click", function () {
    const number = parseInt(document.getElementById("number-input").value);

    const hundreds_digit = Math.floor(number / 100);
    const tens_digit = Math.floor(number / 10) % 10;
    const ones_digit = number % 10;

    const english_ones_digit = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    };

    const english_teens = {
        0: "ten",
        1: "eleven",
        2: "twelve",
        3: "thirteen",
        4: "fourteen",
        5: "fifteen",
        6: "sixteen",
        7: "seventeen",
        8: "eighteen",
        9: "nineteen",
    };

    const english_tens_digit = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    };

    let response;
    if (number < 10) {
        response = english_ones_digit[ones_digit];
    } else if (number < 20) {
        response = english_teens[ones_digit];
    } else if (number < 100) {
        if (ones_digit !== 0) {
            response = english_tens_digit[tens_digit] + "-" + english_ones_digit[ones_digit];
        } else {
            response = english_tens_digit[tens_digit];
        }
    } else if (number < 1000) {
        if (tens_digit === 0) {
            response =
                english_ones_digit[hundreds_digit] + " hundred " + english_ones_digit[ones_digit];
        } else if (tens_digit === 1) {
            response =
                english_ones_digit[hundreds_digit] + " hundred " + english_teens[ones_digit];
        } else {
            if (ones_digit !== 0) {
                response =
                    english_ones_digit[hundreds_digit] +
                    " hundred " +
                    english_tens_digit[tens_digit] +
                    "-" +
                    english_ones_digit[ones_digit];
            } else {
                response =
                    english_ones_digit[hundreds_digit] + " hundred " + english_tens_digit[tens_digit];
            }
        }
    } else {
        response = "Have a nice day!";
    }

    const outputDiv = document.getElementById("output");
    outputDiv.textContent = response;
});
