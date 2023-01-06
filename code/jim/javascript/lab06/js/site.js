Vue.component('section-title', {
    props: ['isSearch'],
    template: '<h2>{{ title }}</h2>',
    computed: {
        title() {
            return this.isSearch ? 'Search Results' : 'Random Quotes';
        }
    }
});

new Vue({
    el: '#app',
    data() {
        return {
            searchTerm: '',
            searchOption: '',
            searchOptions: [
                { value: 'filter', label: 'Keyword', type: '' },
                { value: 'author', label: 'Author', type: 'author' },
                { value: 'tag', label: 'Tag', type: 'tag' }
            ],
            quotes: [],
            page: 0,
            isSearch: false
        }
    },
    methods: {
        async fetchQuotes() {
            try {
                const response = await axios.get(`https://favqs.com/api/quotes`, {
                    headers: {
                        Authorization: "Token 0a4edf08f6b912ba6c7d40002c58570e"
                    },
                    // params: {
                    //     filter: 'funny',
                    //     type: '',
                    // }
                });
                this.quotes = response.data.quotes;
                this.page += 1;
            } catch (error) {
                console.error(error);
            }
        },
        async searchQuotes() {
            try {
                this.isSearch = true;
                const response = await axios.get(`https://favqs.com/api/quotes`, {
                    params: {
                        filter: this.searchTerm,
                        type: this.searchOption
                    },
                    headers: {
                        Authorization: 'Token 0a4edf08f6b912ba6c7d40002c58570e'
                    }
                });
                this.quotes = response.data.quotes;
            } catch (error) {
                console.error(error);
            }
        }
    },
    created() {
        this.fetchQuotes();
    },
})
