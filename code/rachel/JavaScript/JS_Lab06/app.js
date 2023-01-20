new Vue({
    el: '#app',
    data: () => {
        return {
            test: 'hello',
            output: {'quotes': {'body': ''}},
            openQuotes: '',
            body: '',
            keyword: '',
            author: '',
            tag: '',
        }
    },
    mounted() {
        console.log('mount test')
        this.openingQuotes()
    },
    methods: {
        openingQuotes() {
            // axios({
            //     method: 'get',
            //     url: 'https://favqs.com/api/quotes',
            //     // params: {'format': 'json'},
            //     headers: {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
            axios.get('https://favqs.com/api/quotes', {
                headers: {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
            //}).then(res => this.output = res) //this works; returns page of dictionaries
            }).then(response => this.openQuotes = response.data.quotes.body)
                .catch(err => console.error(err))
        }





    },

})
// are these Vue 2 or Vue 3?
