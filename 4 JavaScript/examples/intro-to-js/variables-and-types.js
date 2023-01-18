console.log('hello world') // equivalent to python's print()

// snake_case
// kebab-case
// WordCase or PascalCase
// camelCase // JAVASCRIPT USES THIS ONE

/*
DECLARING VARIABLES
*/

var identifier = 'thing' // var is outdated, don't use it

let firstName = 'Danny'
const lastName = 'Burrow'

firstName = 'Dan'
// lastName = 'something else'
// Uncaught TypeError: Assignment to constant variable.

let newVar
console.log(newVar) //undefined

/*
TYPES 
*/

// Primitive types

let a = 'string' // string
let j = `template literals are like python's f${a}s`
console.log(j);
let b = 1.5 // number
let c = 1 // number
let d = 289289754720290327833989734578934789978345978398498345798354n // bigint
let f = true // boolean
let g = false
let k = null // used to clear a value
let l = undefined // when a value hasn't been assigned yet


// Reference types
let e = [1, 2, 'three', { 'key': 'val' }] // array

let h = new Set() // set
h.add(1)
h.add('beans')
console.log(h)

let i = { key: 'this is a value', key2: [1, 2, 3] } // object
console.log(i);

function myFunc(param1, param2) {
    return param1 + param2
}


/*
TYPE CONVERSION and TYPE COERCION

dynamically typed: variables can change type (type is determined at runtime) 
weakly typed: types can be coerced, JS will try to interpret any operation on any type

 */

let m = parseInt('2')
let n = parseFloat('3.5')
let o = m.toString()

let p = 'sens'
let q = 8

console.log(p + q); // sens8
console.log(p * q); // NaN (not a number)

let r = '1'
let s = 1

console.log(r == s); // true: these have equivalent values
console.log(r === s); // false: these (don't) have equivalent values AND the same type

console.log(r != s); // false
console.log(r !== s); // true
