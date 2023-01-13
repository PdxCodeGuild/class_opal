new Vue({
    el: #app,
    data: {
        output: {},
        userInput: '',
    },
    mounted() {
    },
    methods: {
        getDefinition() {
            console.log('GET Request');
            axios.get('https://api.dictionaryapi.dev/api/v2/entries/en/<word>', {
                params: {
                    'word': this.userInput,
                    'phonetics': this.userInput,
                    'meanings': this.userInput,
                }
            }).then(response => this.output = response)
            .then(data => console.log(data))
            .catch(error => console.error(error))
        },
    }
})






// Choose any API and write a page to interact with it.
// Your page should take in some sort of user input and return different results based on that input.API
// Your page should offer some sort of interactivity in the results. You should also apply some sort of basic professional styling.
// Using a CSS framework is totally fine. Your webpage should utilize Vue to build the interface and Axios for making ajax requests.
// https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html