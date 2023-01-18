const printStrings = () => {
    console.log('thing 1')
    setTimeout(() => console.log('thing 2'), 1000)
    console.log('thing 3')
}

// printStrings()


const examplePromise = new Promise((resolve, reject) => {
    if (false) {
        setTimeout(() => {
            resolve('promise resolved')
        }, 1000)
    } else {
        reject('promise rejected :(')
    }
})

const secondPromise = () => {
    return new Promise((rslv, rjct) => {
        rslv('this one always resolves')
    })
}

// console.log(examplePromise.then(msg => console.log(msg)))

examplePromise
    .then(msg => console.log(msg))
    .then(secondPromise)
    .then(msg => console.log(msg))
    .catch(msg => console.error(msg))




// Async / await are syntactic sugar for promises

// the async keyword means this function will automatically return a Promise
async function exampleAsync() {
    return 1
}

const exampleAwait = async () => {
    try {
        // await can only be used in an async function
        return await examplePromise
    } catch (err) {
        return 'something went wrong'
    }
}

console.log(exampleAwait());

exampleAwait()
    .then(msg => console.log(msg))
    .then(secondPromise)
    .then(msg => console.log(msg))