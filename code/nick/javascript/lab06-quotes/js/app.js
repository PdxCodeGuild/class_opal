new Vue({
    el: '#app',
    data: {
        qotd: null,
        page: 1,
        lastPage: true,
        quotesArray: null,
        random: true,
        newSearchTerm: '',
        cacheSearchTerm: null,
        newSearchType: null,
        cacheSearchType: null,
    },
    mounted() {
        this.qotdFetcher();
        this.getRandomQuotes()
    },
    methods: {
        qotdFetcher() {
            axios.get('https://favqs.com/api/qotd')
                .then(res => this.qotd = res.data.quote)
                .catch(err => console.error(err))
        },
        getRandomQuotes() {
            axios.get('https://favqs.com/api/quotes/', {
                headers: { 'Authorization': 'Token token="e05700b902cbf08ec6e7b93660b66d06"', 'Content-Type': 'application/json' },
                params: { 'page': String(this.page) }
            }).then(res => {
                console.log(res)
                this.quotesArray = res.data.quotes
                this.page = res.data.page
                this.lastPage = res.data.last_page
            }).catch(err => console.error(err))
        },
        newQuotesSearch() {
            this.random = false
            this.page = 1
            this.cacheSearchTerm = this.newSearchTerm
            this.cacheSearchType = this.newSearchType
            axios.get('https://favqs.com/api/quotes/', {
                headers: { 'Authorization': 'Token token="e05700b902cbf08ec6e7b93660b66d06"', 'Content-Type': 'application/json' },
                params: this.searchParams
            })

        },
        iterativeQuotesSearch() {
            axios.get('https://favqs.com/api/quotes/', {
                headers: { 'Authorization': 'Token token="e05700b902cbf08ec6e7b93660b66d06"', 'Content-Type': 'application/json' },
                params: this.searchParams
            })
        },
        pageMove(direction) {
            if (direction == 'up') { this.page++ }
            else if (direction == 'down') { this.page-- };
            
            if (this.random) { this.getRandomQuotes() }
            else if (!this.random) {this.iterativeQuotesSearch()}
        },
    },
    computed: {
        disabled() {
            if (this.page == 1) { return true }
            else {return false}
        },
        searchParams() {
            const searchTypes = ['tag', 'author']
            if (searchTypes.includes(this.cacheSearchType)) {
                let parameters = { 'page': String(this.page), 'filter': this.cacheSearchTerm, 'type': this.cacheSearchType }
                return parameters
            }
            else {
                let parameters = { 'page': String(this.page), 'filter': this.cacheSearchTerm }
                return parameters
            }

        },

    }
})


Vue.component('QuoteItem', {
    template: `
    <div class="col s12">
        <div class="card cyan darken-4 center">
            <div class="card-content white-text">
                <p>{{ quote.body }}</p>
                <p class="right">-{{ quote.author }}</p>
            </div>
        </div>
    </div>
    `,
    props: {
        quote: {
            type: Object
        },
    },
})