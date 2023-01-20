Vue.component('SearchButtons', {
    methods: {
        getQuoteByKeyword() {
            let keyword = document.getElementById('search').value;
            myParams = { filter: keyword }
            axios.get('https://favqs.com/api/quotes', {
                headers: {
                    Authorization:
                        "Token 855df50978dc9afd6bf86579913c9f8b"
                }
                , params: myParams
            }).then(res => this.newQuotes = res.data.quotes)

        },
        getQuoteByAuthor() {
            let searchByAuthor = document.getElementById('authorSearch').value;
            myParams = { filter: searchByAuthor, type: 'author' }
            axios.get('https://favqs.com/api/quotes', {
                headers: {
                    Authorization:
                        "Token 855df50978dc9afd6bf86579913c9f8b"
                }
                , params: myParams
            }).then(res => this.newQuotes = res.data.quotes)
                .catch(err => console.error(err))
        },
        getQuoteByTag() {
            
            let searchByTag = document.getElementById('tagSearch').value;
            myParams = { filter: searchByTag, type: 'tag' }
            axios.get('https://favqs.com/api/quotes', {
                headers: {
                    Authorization:
                        "Token 855df50978dc9afd6bf86579913c9f8b"
                }
                , params: myParams
            }).then(res => this.newQuotes = res.data.quotes)
                .catch(err => console.error(err))
        }
    },

    template: `
    <div>
    
    <button @click='getQuoteByKeyword'>Keyword</button>
    <button @click='getQuoteByAuthor'>Author</button>
    <button @click='getQuoteByTag'>Tag</button>
    <ul v-for="r in newQuotes">
        <li>{{ r.body }} -- {{ r.author }}</li>
    </ul>
    </div>  `,

    data: () => {
        return {
            keyword: '',
            author: '',
            tag: '',
            newQuotes: {}
        }
    }
})
    ;

new Vue({
    el: '#app',
    data() {
        return {
            quotes: {},
            res: '',
            quote: ''

        }

    },
    mounted() {
        this.getQuote()
    },
    methods: {

        getQuote() {
            axios.get('https://favqs.com/api/quotes', {
                headers: {
                    Authorization:
                        "Token 855df50978dc9afd6bf86579913c9f8b"
                }
            }).then(res => (this.quotes = res.data.quotes))
        },



    }
})
