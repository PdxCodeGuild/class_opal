const card1 = document.getElementById('card1');
const card2 = document.getElementById('card2');
const card3 = document.getElementById('card3');
const run_bt = document.querySelector('#run_bt');
const outputAdvice = document.querySelector('#output_advice');


run_bt.onclick = function() {
    const dictCards = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    const numCard1 = dictCards[card1.value]
    const numCard2 = dictCards[card2.value]
    const numCard3 = dictCards[card3.value]

    const total = numCard1 + numCard2 + numCard3

    if (total < 17) {
        outputAdvice.innerText = `Your total is: ${total}. Hit.`;
    } else if (total >= 17 && total < 21) {
        outputAdvice.innerText = `Your total is: ${total}. Stay.`;
    } else if (total == 21) {
        outputAdvice.innerText = `Your total is: ${total}. Blackjack!`;
    } else {
        outputAdvice.innerText = `Your total is: ${total}. Already busted.`;
    }
}