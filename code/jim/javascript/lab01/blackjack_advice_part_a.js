const playingCards = ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", 'J', 'Q', 'K'];
const inputErrorMessage = "You must enter a valid playing card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).";

// get user to input three card values
let card1;
while (true) {
    card1 = prompt("What's your first card?: ");
    if (playingCards.includes(card1)) {
        break;
    } else {
        console.log(inputErrorMessage);
    }
}

let card2;
while (true) {
    card2 = prompt("What's your second card?: ");
    if (playingCards.includes(card2)) {
        break;
    } else {
        console.log(inputErrorMessage);
    }
}

let card3;
while (true) {
    card3 = prompt("What's your third card?: ");
    if (playingCards.includes(card3)) {
        break;
    } else {
        console.log(inputErrorMessage);
    }
}

// collect cards in array
const cards = [card1, card2, card3];

const cardValues = [];
let total = 0;

// convert Ace and face cards to integer values
const pointValueConversions = {
    'A': 11,
    'J': 10,
    'Q': 10,
    'K': 10
};

for (const card of cards) {
    let convertedCardValue;
    try {
        convertedCardValue = pointValueConversions[card];
    } catch (error) {
        // do nothing
    }
    cardValues.push(convertedCardValue || card);
}

// convert number cards to integer values and calculate hand total
for (let cardValue of cardValues) {
    cardValue = parseInt(cardValue, 10);
    total += cardValue;
}

// output strategic advice based on hand total
let advice;
if (total < 17) {
    advice = "Hit";
} else if (total < 21) {
    advice = "Stay";
} else if (total === 21) {
    advice = "Blackjack!";
} else {
    if (cards.filter(card => card === 'A').length === 0) {
        advice = "Already Busted";
    } else if (cards.filter(card => card === 'A').length === 1) {
        total = total - 10;
        if (total < 17) {
            advice = "Hit";
        } else if (total < 21) {
            advice = "Stay";
        } else if (total === 21) {
            advice = "Blackjack!";
        } else {
            advice = "Already Busted";
        }
    } else if (cards.filter(card => card === 'A').length === 2) {
        if (total < 17 + 10) {
            total = total - 10;
            advice = "Hit";
        } else if (total < 21 + 10) {
            total = total - 10;
            advice = "Stay";
        } else if (total === 21 + 10) {
            total = total - 10;
            advice = "Blackjack!";
        } else {
            total = total - 20;
            advice = "Hit";
        }
    }
    else {
        total = 13;
        advice = "Hit"
    }
}

alert(`${total} ${advice}`)


