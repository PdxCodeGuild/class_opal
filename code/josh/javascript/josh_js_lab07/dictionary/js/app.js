new Vue({
    el: '#app',
    data: {
        output: {},
        userInput: '',
        audio: '',
        savedWords: [],
        searchError: false,
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
            .catch(error => this.searchError = true && alert('Your search did not produce any results.  Please check your spelling and try again.'))
        },
        getAudio() {
            console.log('GET Request');
            axios.get(`https://api.dictionaryapi.dev/api/v2/entries/en/${this.userInput}`)
            .then(response => this.audio = response.data[0].phonetics[0].audio)
            .then(data => console.log(data))
            .catch(error => console.error(error));
        },
        saveNewWord() {
            if (this.savedWords.length >= 1) {
                for (el of this.savedWords) {
                    console.log(el.word)
                    if (this.userInput === el.word) {
                        alert('You have already saved this word.');
                        break;
                    } else {
                        this.savedWords.push({word: this.userInput, definition: this.output});
                        break;
                    }
                }
            } else {
                this.savedWords.push({word: this.userInput, definition: this.output});
            };
            this.clearInput();
        },
        deleteWord(word) {
            console.log(word);
            let wordIndex = this.savedWords.indexOf(word);
            this.savedWords.splice(wordIndex, 1);
        },
        clearInput() {
            this.userInput = '';
            this.output = {};
            this.audio = '';
        },
        // not working yet
        downloadWordList() {
            // in order to use this, I would have to npm install node
            const fs = require('fs');
            fs.writeFile("./savedWords.json", JSON.stringify(this.savedWords), error => {
                if (error) {
                    console.log(error);
                } else {
                    console.log('File successfully written.')
                }
            });
            // console.log(jsonString);
            // this.savedWords.writeFileSync("./savedWords.json", JSON.stringify(this.savedWords));
        },
        // not working yet
        uploadWordList() {
            const savedWordsFromFile = JSON.parse(this.savedWords.readFileSync("./savedWords.json", "utf8"));
            console.log("Words from file:", savedWordsFromFile);  
        },
}})

// You should also apply some sort of basic professional styling. Using a CSS framework is fine.
// https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html