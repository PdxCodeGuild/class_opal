//Blackjack advice//

let cardValues = {a: 1, Ace: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, j: 10, jack: 10, q: 10, queen: 10, k: 10, king: 10}

let firstCard = prompt("What's your first card? Enter the number, or for face cards, enter j for jack, q for queen, k for king, and a for ace. ")
//console.log(typeof firstCard)
let secondCard = prompt("What's your second card? ")
let thirdCard = prompt("What's your third card? ")

let value1 = cardValues[firstCard]
let value2  = cardValues[secondCard]
let value3 = cardValues[thirdCard]
console.log("value1", firstCard, value1)
console.log("value2", secondCard, value2)
console.log("value3", thirdCard, value3)

let cardsTotal = value1 + value2 + value3
console.log("cards total", cardsTotal)


if (cardsTotal <= 16) {
    alert(cardsTotal + " hit me")
} else if (cardsTotal <= 20) {
    alert(cardsTotal + " stay")
} else if (cardsTotal == 21) {
    alert(cardsTotal + " blackjack!")
} else if (cardsTotal > 21) { 
    alert(cardsTotal + " Busted!")
}