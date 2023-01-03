/*
CONDITIONALS
*/

const a = 0
const b = 1
const c = false
const isFalse = a == b

console.log(a == b); // checks if values are the same
console.log(a === b); // checks if values AND TYPE are the same
console.log(a != b);
console.log(a !== b);

// and is &&
// or is ||

if (isFalse) {
    console.log("this won't execute");
} else if (a <= b && true || !isFalse && c) {
    console.log("this will!");
} else {
    console.log("this won't again");
}


// Ternary operator
// [condition] ? [output if true] : [output if false]

let valA
if (a > b) {
    valA = 'thing1'
} else {
    valA = 'thing2'
}

const valB = a > b ? 'thing1' : 'thing2'

const valC = a > b && 1 > 0 || c || !isFalse && a === c

if (valC) {
    console.log('do something based on complicated condition');
}

const myObj = {
    key1: valC ? 'thing1' : 'thing2'
}

console.log(myObj)



/* 
FUNCTIONS
*/

// standard function declaration
function add(x, y) {
    return x + y
}

console.log(add(1, 3));

// assign to a variable
const subtract = function (x, y) {
    return x - y
}

console.log(subtract(1, 3));

// ES6 arrow function, rocket function

const multiply = (x, y) => x * y

console.log(multiply(6, 3));


const divide = (x, y) => {
    console.log('this line introduces complexity')
    return x / y
}

console.log(divide(6, 3));


// CALLBACKS
// Callbacks are often anonymous, but they don't have to be
// Anonymous functions don't have names


let numArray = [1, 2, 3, 4, 5]


const filterHelper = (x) => {
    if (x > 2) {
        return x
    }
}

// The function passed to another function is the "callback"
const filteredArray = numArray.filter(filterHelper)


// The same as filterHelper, but written as an anonymous function
const filteredArray2 = numArray.filter(x => {
    console.log('there may or may not be complexity here');
    return x > 2
})


// The same again, without the optional brackets and return keyword
const filteredArray3 = numArray.filter(x => x > 2)
