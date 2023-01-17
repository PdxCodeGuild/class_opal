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
        // searches Free Dictionary API with user input and loads definition and getAudio method 
        getDefinition() {
            console.log('GET Request');
            axios.get(`https://api.dictionaryapi.dev/api/v2/entries/en/${this.userInput}`)
            .then(response => this.output = response.data[0].meanings[0].definitions[0].definition)
            .then(data => console.log(data))
            .then(() => this.getAudio())
            // alerts user if user input is not found in dictionary
            .catch(error => this.searchError = true && alert('Your search did not produce any results.  Please check your spelling and try again.'))
        },
        // searches Free Dictionary API with user input and loads audio file URL
        getAudio() {
            console.log('GET Request');
            axios.get(`https://api.dictionaryapi.dev/api/v2/entries/en/${this.userInput}`)
            .then(response => this.audio = response.data[0].phonetics[0].audio)
            .then(data => console.log(data))
            .catch(error => console.error(error));
        },
        // saves unique word:definition pair objects to savedWords array, alerts user of attempted duplicates, and runs clearInput method
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
        // deletes words from savedWords array by index
        deleteWord(word) {
            console.log(word);
            let wordIndex = this.savedWords.indexOf(word);
            this.savedWords.splice(wordIndex, 1);
        },
        // clears unsaved user input from search field, loaded definition, and audio link 
        clearInput() {
            this.userInput = '';
            this.output = {};
            this.audio = '';
        },
        // stores saved words to local storage, alerts user, and empties savedWords array
        downloadWordList() {
            const download = this.savedWords
            localStorage.setItem('download', JSON.stringify(download));
            console.log(download);
            this.savedWords = [];
            alert('You have successfully downloaded your saved words.')
        },
        // loads stored words from local storage
        uploadWordList() {
            const upload = JSON.parse(localStorage.getItem('download'));
            this.savedWords = upload
        },
}})