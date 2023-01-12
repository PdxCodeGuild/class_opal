new Vue({
    el: '#app',
    data() {
        return {
            output: {},
            res: ''
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
            }).then(res => (this.output = res.data.quotes))
        },
        getQuoteByKeyword() {
            let keyword = document.getElementById('search').value;
            myParams = { filter: keyword }
            axios.get('https://favqs.com/api/quotes', {
                headers: {
                    Authorization:
                        "Token 855df50978dc9afd6bf86579913c9f8b"
                }
                , params: myParams
            }).then(res => this.output = res.data.quotes)
            // .catch(err => console.error(err))
        },
        getQuoteByAuthor() {
            let searchByAuthor = document.getElementById('authorSearch').value;
            myParams = {filter: searchByAuthor, type: 'author'}
            axios.get('https://favqs.com/api/quotes', {
                headers: {
                    Authorization:
                        "Token 855df50978dc9afd6bf86579913c9f8b"
                }
                , params: myParams
            }).then(res => this.output = res.data.quotes)
            .catch(err => console.error(err))
        },
        getQuoteByTag() {
            let searchByTag = document.getElementById('tagSearch').value;
            myParams = {filter: searchByTag, type: 'tag'}
            axios.get('https://favqs.com/api/quotes', {
                headers: {
                    Authorization:
                        "Token 855df50978dc9afd6bf86579913c9f8b"
                }
                , params: myParams
            }).then(res => this.output = res.data.quotes)
            .catch(err => console.error(err))
        }


    }
})
