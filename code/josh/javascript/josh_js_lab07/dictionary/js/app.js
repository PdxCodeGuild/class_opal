new Vue({
    el: '#app',
    data: {
        output: {},
        userInput: '',
        audio: '',
    },
    mounted() {
    },
    methods: {
        getDefinition() {
            console.log('GET Request');
            axios.get(`https://api.dictionaryapi.dev/api/v2/entries/en/${this.userInput}`)
            .then(response => this.output = response.data[0].meanings[0].definitions[0].definition)
            .then(data => console.log(data))
            .then(() => this.getAudio())
            .catch(error => console.error(error));
        },
        getAudio() {
            console.log('GET Request');
            axios.get(`https://api.dictionaryapi.dev/api/v2/entries/en/${this.userInput}`)
            .then(response => this.audio = response.data[0].phonetics[0].audio)
            .then(data => console.log(data))
            .catch(error => console.error(error));
        },
    }
})

// Your page should offer some sort of interactivity with the results. You should also apply some sort of basic professional styling.
// Using a CSS framework is totally fine. Your webpage should utilize Vue to build the interface and Axios for making ajax requests.
// https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html