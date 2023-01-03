// Lab 1 - Unit Converter, Version 4

// Creates a variable that stores user input of a distance as units
let userDistance = prompt("What is the distance (ft, mi, m, km, yd or in)? ")
// Typecasts user input to an integer for conversion
userDistance = parseInt(userDistance)
// Creates a variable that stores user input of a starting unit of measure
const unitsInput = prompt("What are the input units (ft, mi, m, km, yd, or in)? ")
// Creates a variable that stores the user's desired unit of measure as an output 
const unitsOutput = prompt("What are the output units (ft, mi, m, km, yd, or in)? ")
// Creates a dictionary that stores units of measure as keys and numeric conversions as values
conversion = {"ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254}
// Creates a variable that converts user input of distance to meters, according to user input of
// desired starting units
const newDistance = userDistance * conversion[unitsInput]
// Creates a variable that converts meter conversion to user input of desired output units 
const newUnits = newDistance / conversion[unitsOutput]
// Displays the conversion of user's inputs of distance and unit measure to user's desired unit 
// measureoutput
alert(`${userDistance} ${unitsInput} is ${newUnits} ${unitsOutput}.`)