Vue.component('save-quote', {
    data: function () {
        return {
            savedQuotes: []
        }
    },
    template: '<button v-on:click="saveNewQuote">Save Quote</button>',
    props: ['favQuotes'],    
    methods: {
        saveNewQuote() {
            console.log(this.favQuotes)
            if (this.savedQuotes.length >= 1) {
                for (el of this.savedQuotes) {
                    console.log(el.quote)
                    if (this.userInput === el.quote) {
                        alert('You have already saved this quote.');
                        break;
                    } else {
                        this.savedQuotes.push(this.favQuotes);
                        break;
                    }
                }
            } else {
                this.savedQuotes.push(this.favQuotes);
            };
        },
    },
})

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