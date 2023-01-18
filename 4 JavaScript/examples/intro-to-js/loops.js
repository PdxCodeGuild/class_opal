/*
LOOPS

There are LOT of ways to loop in JS
*/

// old school, classic, weird
for (let i = 1; i <= 5; i++) {
    console.log(i);
}

// vanilla while loop
let i = 0
while (i < 5) {
    i++
    console.log(i)
}


// ITERATING OVER AN ARRAY

const numArray = [1, 2, 3, 4, 5]

// old school
for (let i = 0; i < numArray.length; i++) {
    console.log(numArray[i]);
}

// with a while loop
let x = 0
while (x < numArray.length) {
    console.log(numArray[x]);
    x++
}


// BETTER WAY!!
numArray.forEach(x => console.log(x))


// ANOTHER BETTER WAY!!
// for..of
for (x of numArray) {
    console.log(x);
}

// map, filter, reduce
// for when you want a new version of the array

const doubled = numArray.map(x => x * 2)
console.log(doubled);

const evens = numArray.filter(x => x % 2 == 0)
console.log(evens);

const sum = numArray.reduce((x, y) => x + y)
console.log(sum);


// Iterating over an object

let myObj = {
    1: 'one',
    2: 'two',
    3: 'three'
}

// for..in 
// loops over the keys
for (thing in myObj) {
    console.log(thing);
    console.log(myObj[thing]);
}

// loop over Object.entries()
console.log(Object.entries(myObj));

Object.entries(myObj).forEach(x => console.log(x[0], x[1]))


// loop over Object.keys()
for (key of Object.keys(myObj)) {
    console.log(myObj[key]);
}