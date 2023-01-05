alert(`Welcome to the (bad) Blackjack Advice-Giver!
Available cards: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, and K. 
This assumes ace has a value of 1.`)

const card1 = prompt('Please enter your first card: ')
const card2 = prompt('Please enter your second card: ')
const card3 = prompt('Please enter your third card: ')

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

const numCard1 = dictCards[card1]
const numCard2 = dictCards[card2]
const numCard3 = dictCards[card3]

const total = numCard1 + numCard2 + numCard3

if (total < 17) {
    alert(`Your total is: ${total}. Hit.`);
} else if (total >= 17 && total < 21) {
    alert(`Your total is: ${total}. Stay.`);
} else if (total == 21) {
    alert(`Your total is: ${total}. Blackjack!`);
} else {
    alert(`Your total is: ${total}. Already busted!`)
}