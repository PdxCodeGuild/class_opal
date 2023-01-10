const numCards = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'A': 1,
    'J': 10,
    'Q': 10,
    'K': 10
}

const myButton = document.getElementById('myButton');
let hand = [];
const addToHand = (card) => {
    let firstCard = document.getElementById('firstCard').value;
    let secondCard = document.getElementById('secondCard').value;
    let thirdCard = document.getElementById('thirdCard').value;
    hand.push(firstCard, secondCard, thirdCard);
    console.log(hand)


    let total = numCards[hand[0]] + numCards[hand[1]] + numCards[hand[2]]
    let myTotal = document.getElementById('resultDiv')

    total <= 10 && hand.includes('A') ? numCards['A'] = 11 : numCards['A'] = 1;

    if (total < 17) {
        myTotal.innerText = `${total}, Hit!`;
    } else if (total >= 17 && total < 21) {
        myTotal.innerText = `${total}, Stay`;
    } else if (total == 21) {
        myTotal.innerText = `${total}, Blackjack!`;
    } else if (total > 21) {
        myTotal.innerText = `${total}, Busted!`;
    }

}
myButton.addEventListener('click', addToHand);