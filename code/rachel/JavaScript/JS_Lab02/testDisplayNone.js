//Blackjack advice//
const cardValues = {a: 1, Ace: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, j: 10, jack: 10, q: 10, queen: 10, k: 10, king: 10}

const body = document.querySelector('body')
const firstCard = document.getElementById('firstCard').value
const firstSubmit = document.querySelector('#firstSubmit')

function blackJack() {
    document.getElementById('second').style.display = "block";
    const secondCard = document.getElementById('secondCard').value
    const secondSubmit = document.querySelector('#secondSubmit')
    

    function third() {
        document.getElementById('third').style.display = "block";
        const thirdCard = document.getElementById('thirdCard').value
        const thirdSubmit = document.querySelector('#thirdSubmit')
        return thirdCard
    }
    secondSubmit.addEventListener('click', third) 
    // secondSubmit.addEventListener('click', function third() {
    //     document.getElementById('third').style.display = "block";
    //     const thirdCard = document.getElementById('thirdCard').value
    //     const thirdSubmit = document.querySelector('#thirdSubmit')
    //     return thirdCard
    // })

    let value1 = cardValues[firstCard]
    let value2  = cardValues[secondCard]
    let value3 = cardValues[third()]

    let cardsTotal = value1 + value2 + value3

    console.log(cardsTotal)

    // const advice = document.createElement('advice')

    // if (cardsTotal <= 16) {
    //     advice.innerText = `${cardsTotal} hit me`
    //     body.appendChild(advice)
    // } else if (cardsTotal <= 20) {
    //     advice.innerText = `${cardsTotal} stay`
    //     body.appendChild(advice)
    // } else if (cardsTotal == 21) {
    //     advice.innerText = `${cardsTotal} BLACKJACK!`
    //     body.appendChild(advice)
    // } else if (cardsTotal > 21) { 
    //     advice.innerText = `${cardsTotal} busted`
    //     body.appendChild(advice)
    // }
}

firstSubmit.addEventListener('click', blackJack)
    //add event listener for first card, then run blackjack function
