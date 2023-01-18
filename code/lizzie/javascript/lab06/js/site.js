Vue.component('QuoteTitle', {
  props: ['isSearch'],
  template: '<h2>{{ title }}</h2>',
  computed: {
    title() {
      // condition is: this.isSearch ? True : False
      return this.isSearch ? 'Your Results' : 'Random Quotes';
    }
  }
});

new Vue({
  el: '#app',
  data: {
    searchTerm: '',
    searchOption: '',
    searchOptions: [
        { value: 'filter', label: 'Keyword', type: '' },
        { value: 'author', label: 'Author', type: 'author' },
        { value: 'tag', label: 'Tag', type: 'tag' }
    ],
    quotes: [],
    errored: false,
    // isSearch is a boolen that resolves to true only after a user has searched for a term
    // This boolen will determine whether the quote title is one string or another. 
    isSearch: false
  },
  mounted() {
    this.randQuotes()
  },
  methods: {
    randQuotes() {
      axios.get(`https://favqs.com/api/quotes`, {
        headers: {
          Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
        },
      }).then(response => {
        this.quotes = response.data.quotes
      }).catch(error => { //How make this work?
        console.log(error)
        this.errored = true
    })
    },
    searchQuote() {
      this.isSearch = true;
      axios.get(`https://favqs.com/api/quotes`, {
        headers: {
          Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
        },
        params: {
          // fetching the information retrieved from data that stores user input
          filter: this.searchTerm,
          type: this.searchOption
        },
      }).then(response => {
        this.quotes = response.data.quotes
      })
    }
  }
})
