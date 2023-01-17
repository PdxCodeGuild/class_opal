new Vue({
    el: '#app',
    data() {
        return {
            characters: {},
            char: '',
            res: '',
            myChar: {},
            searchInput: '',
            searchResults: ''
        }
    },
    mounted() {
        this.getCharPics()
    },
    methods: {
        getCharPics() {
            myParams = { limit: 100 }
            axios.get('https://bobsburgers-api.herokuapp.com/characters/', {
                params: myParams
            }).then(res => {
                this.characters = res.data
            }).catch(err => console.error(err))
        },
        searchForChar() {
            axios.get('https://bobsburgers-api.herokuapp.com/characters/').then(res => {
                for (char of res.data) {
                    if (char.name.includes(this.searchInput)) {
                        console.log(char)
                        this.searchResults = char
                        break
                    }
                }
            }
            )
        }

    }
})