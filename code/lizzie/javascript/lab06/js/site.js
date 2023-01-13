Vue.component('SectionTitle', {
  props: ['isSearch'],
  template: '<h2>{{ title }}</h2>',
  computed: {
    title() {
      return this.isSearch ? 'Search Results' : 'Random Quotes';
    }
  }
});

// Vue.component('TextComp', {
//   // gonna need props to properly retrieve this info I think
//   template: `<ul v-for="quote in quotes" :key="quote.id">
//   <li>
//       {{ quote.body }}
//       — {{ quote.author }}
//   </li>
//   </ul>`
// })

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
    page: 0,
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
