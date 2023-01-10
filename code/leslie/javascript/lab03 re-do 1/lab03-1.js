let numCards = {
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


let hand = [];
let firstCard = prompt("What's your first card?");
hand.push(firstCard);
let secondCard = prompt("What's your second card?");
hand.push(secondCard);
let thirdCard = prompt("What's your third card?");
hand.push(thirdCard);
console.log(hand);

let total = numCards[firstCard] + numCards[secondCard] + numCards[thirdCard];
console.log(total)

if (total <= 10 && hand.includes('A')) {
    numCards['A'] = 11
} else {
    numCards['A'] = 1
}


if (total < 17) {
    alert(`${total}, Hit!`);
} else if (total >= 17 && total < 21) {
    alert(`${total}, Stay`);
} else if (total == 21) {
    alert(`${total}, Blackjack!`);
} else if (total > 21) {
    alert(`${total}, Busted!`);
}