//Blackjack advice//
const cardValues = {a: 1, Ace: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, j: 10, jack: 10, q: 10, queen: 10, k: 10, king: 10}

const body = document.querySelector('body')
const submit = document.getElementById('submit')


function blackJack() {
    const firstCard = document.getElementById('firstCard').value
    const secondCard = document.getElementById('secondCard').value
    const thirdCard = document.getElementById('thirdCard').value
    

    let value1 = cardValues[firstCard]
    let value2  = cardValues[secondCard]
    let value3 = cardValues[thirdCard]

    let cardsTotal = value1 + value2 + value3

    const advice = document.createElement('advice')

    if (cardsTotal <= 16) {
        advice.innerText = `${cardsTotal} hit me`
        body.appendChild(advice)
    } else if (cardsTotal <= 20) {
        advice.innerText = `${cardsTotal} stay`
        body.appendChild(advice)
    } else if (cardsTotal == 21) {
        advice.innerText = `${cardsTotal} BLACKJACK!`
        body.appendChild(advice)
    } else if (cardsTotal > 21) { 
        advice.innerText = `${cardsTotal} busted`
        body.appendChild(advice)
    }
}

submit.addEventListener('click', blackJack)