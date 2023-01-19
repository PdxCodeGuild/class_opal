Vue.component('save-quote', {
    data: function () {
        return {
            savedQuotes: []
        }
    },
    template: '<div :id="savedQuotes"><button v-on:click="saveNewQuote">Save Quote</button><br><h2>Saved Quotes List</h2><br><p v-for="(item) in savedQuotes">{{ item }}</p></div>',
    props: ['favQuotes'],    
    methods: {
        saveNewQuote() {
            let userSearch = document.getElementById('search').value
            this.savedQuotes.push(this.favQuotes);
            console.log(this.savedQuotes)
            if (this.savedQuotes.length >= 1) {
                for (el of this.savedQuotes) {
                    console.log(el)
                    if (userSearch === el) {
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