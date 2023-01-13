// const axios = require('axios');

new Vue ({
    el: '#app',
    data: {
        output: {},
        userInput: '',
        typeChoice: '',
        qotd: '',
        },
    mounted() {
        this.getQOTD()
    },
    methods: {
        getQuote() {
            console.log('GET request');
            axios.get('https://favqs.com/api/quotes/', {
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: {
                    'filter': this.userInput,
                    'type': this.typeChoice,
                }
    }).then(response => this.output = response.data.quotes)
    .then(data => console.log(data))
    .catch(error => console.error(error))
    },
        getQOTD() {
            console.log('GET request');
            axios.get('https://favqs.com/api/qotd/')
            .then(response => this.qotd = response.data.quote)
            .then(data => console.log(data))
            .catch(error => console.error(error))
        }
}})

// You must have at least one Vue component in your app. Review components here