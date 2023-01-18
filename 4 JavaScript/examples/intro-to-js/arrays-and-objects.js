/*
ARRAYS

JS arrays are a lot like python lists! 

*/

let colors = ['red', 'blue', 'green']
colors.push('magenta', 'orange') // push adds to end of array
let popped = colors.pop() // pop removes from end of array
console.log(popped, colors);

let shifted = colors.shift() // shift removes from beginning of array
console.log(shifted, colors);

colors.unshift('pink') // unshift adds to beginning of array
console.log(colors);


console.log(colors[1]); // access by index just like python
// console.log(colors[1: 3]); //Uncaught SyntaxError: Unexpected token ':' 
console.log(colors.slice(1, 3));
console.log(colors.slice(1)); // equivalent to colors[1:]

colors[1] = 'cerulean'
colors[4] = 'brown'
colors[7] = 'purple'

console.log(colors);
console.log(colors[6]);
console.log(colors.length);

delete colors[1] // deletes value and leaves its index empty
console.log(colors);

let subList = colors.splice(2, 3, 'violet')
console.log(subList, colors);

let pinkIndex = colors.indexOf('pink')
console.log(pinkIndex);
colors.splice(pinkIndex, 1)
console.log(colors);

if (colors.indexOf('green') !== -1) {
    colors.splice(colors.indexOf('green'), 1)
}

if (colors.indexOf('purple') !== -1) {
    colors.splice(colors.indexOf('purple'), 1)
}

console.log(colors);


/* 

OBJECTS 

A JS object is like a python dictionary AND like a python object

*/

const person = { firstName: 'Danny', lastName: 'Burrow' }

console.log(person['firstName'])
console.log(person.lastName)

person.title = 'instructor'
person.favoriteFood = 'beans'
person['firstName'] = 'Dan'

console.log(person);


let pizza = {
    toppings: ['pineapple', 'death', 'olives', { sausage: 'chorizo' }],
    pizzeria: {
        name: 'EGPL',
        'phone number': 1234567890, // use a string for keys if the key is illegal
        staff: {
            owner: 'Mr. Bossman',
            chef: 'Remy',
            signWaver: 'Greg'
        }
    }
}

console.log(pizza.pizzeria.staff.signWaver); // Greg
// use bracket notation when the key is a string
console.log(pizza.pizzeria["phone number"]); //1234567890

// use bracket notation when using a variable in the path
const res = 'pizzeria'
// console.log(pizza.res.staff); //arrays-and-objects.js:91 Uncaught TypeError: Cannot read properties of undefined (reading 'staff')
console.log(pizza[res].staff);

pizza.toppings.push('anchovies')
console.log(pizza);

console.log(pizza.toppings[3].sausage);


// Accesing the keys of an object
const pizzaKeys = Object.keys(pizza.pizzeria.staff)
console.log(pizzaKeys); //['toppings', 'pizzeria']

for (const prop in pizza) {
    console.log(`${prop}: ${pizza[prop]}`);
}
