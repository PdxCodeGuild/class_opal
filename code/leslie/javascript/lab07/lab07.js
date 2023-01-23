new Vue({
    el: '#app',
    data() {
        return {
            characters: {},
            char: '',
            res: '',
            myChar: {},
            searchInput: '',
            searchResults: '',
            charNotFound: false
        }
    },
    mounted() {
        this.getCharPics()
    },
    methods: {
        getCharPics() {

            axios.get('https://bobsburgers-api.herokuapp.com/characters/').then(res => {
                this.characters = res.data
            }).catch(err => console.error(err))
        },
        searchForChar() {
            for (char of this.characters) {
                if (char.name.includes(this.searchInput)) {
                    console.log(char)
                    this.searchResults = char
                    this.charNotFound = false
                    break
                }
                else {
                    this.charNotFound = true
                    this.searchResults = ''
                }
            }
        }

    }
})