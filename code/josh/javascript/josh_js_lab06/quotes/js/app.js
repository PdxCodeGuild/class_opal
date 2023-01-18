Vue.component('save-quote', {
    data: function () {
        savedQuotes: [];
        },
    template: '<button v-on:click="saveNewQuote">Save Quote</button>',
    methods: {
        saveNewQuote() {
            if (this.savedQuotes.length >= 1) {
                for (el of this.savedQuotes) {
                    console.log(el.quote)
                    if (this.userInput === el.quote) {
                        alert('You have already saved this quote.');
                        break;
                    } else {
                        this.savedQuotes.push({quote: this.output.body, author: this.output.author});
                        break;
                    }
                }
            } else {
                this.savedQuotes.push({word: this.output.body, definition: this.output.author});
            };
            this.clearInput();
        },
        // clears unsaved user input from search field, loaded definition, and audio link 
        clearInput() {
            this.userInput = '';
            this.output = {};
            this.audio = '';
        },
        // stores saved words to local storage, alerts user, and empties savedWords array
        downloadQuoteList() {
            const download = this.savedWords
            localStorage.setItem('download', JSON.stringify(download));
            console.log(download);
            this.savedWords = [];
            alert('You have successfully downloaded your saved quotes.')
        },
        // loads stored words from local storage
        uploadQuoteList() {
            const upload = JSON.parse(localStorage.getItem('download'));
            this.savedWords = upload
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