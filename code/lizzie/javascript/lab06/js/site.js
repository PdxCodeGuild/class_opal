// Vue.component({
// We will get back to this...
//  template: ``,
//  data: () => {},
// props: {},
// methods: {},
// computed: {}
//})


new Vue({
  el: '#app',
  data: {
    quotes: [],
  },
  // mounted() {
  //   this.fetchQuotes()
  // },
  methods: {
    fetchQuotes() {
      axios.get(`https://favqs.com/api/quotes`, {
        params: {
          page: '1',
          // Take this out if you want to mount random results (apparently)
          filter: 'flower',
          type: '',
        },
        headers: {
          Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
        },
      }).then(response => this.quotes = response.data.quotes)
    },
  }
})
