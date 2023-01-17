new Vue({
    el: '#app',
    data: {
      foxImage: null,
      foxInfo: null,
      spaceImage: null,
      // Work on this loding thing
      loading: true,
      errored: false,
      jokes: null,
      totalJokes: null,
      definition: null,
      userResponse: '',
      index: 1,
      jokesLeft: null,
      spaceCopyright: null,
      spaceDescription: null
    },
    mounted() {
      this.getSpaceImage(),
      this.getFoxImage()
    },
    methods: {
      addList() {
        this.index = Math.min(this.index + 1, this.jokes.length),
        this.jokesLeft = Math.min(this.totalJokes - this.index)
      },
      clearList() {
        this.index = 1
      },
      getFoxImage() {
        axios
        .get('https://randomfox.ca/floof/?ref=apilist.fun/', {
          params: {},
        headers: {},
        }).then(response => 
          (this.foxImage = response.data.image,
            this.foxInfo = response.data
        ))
        .catch(error => {
            console.log(error)
            this.errored = true
        })
        .finally(() => this.loading = false)
      },
      getSpaceImage() {
        axios.get('https://api.nasa.gov/planetary/apod?api_key=EUgrtpQMpfvvYbZp6zqMmJiWNGtGENsuoY1D00TL', {
          params: {},
          headers: {},
        }).then(response =>
          (this.spaceImage = response.data.hdurl,
            this.spaceCopyright = response.data.copyright,
            this.spaceDescription = response.data.explanation
        ))
        .catch(error => {
          console.log(error)
          this.errored = true
      })
      .finally(() => this.loading = false)
      },
      getPun() {
        axios.get('https://icanhazdadjoke.com/search', {
          // the term is whatever was determined by user in the text input
          params: {term: this.userResponse},
          headers: {accept: 'application/json'},
        }).then(response =>
          // Hard-coded but might just have to go 
          // v-for pun in puns, pun at indexof .joke or something like that
          (this.jokes = response.data.results,
          this.totalJokes = response.data.total_jokes
        ))
        .catch(error => {
          console.log(error)
          this.errored = true
      })
      .finally(() => this.loading = false)
      },
      // Un-comment out later once done messign with user input. It is hardcoded into the url.
      getDefinition() {
        axios.get(`https://wordsapiv1.p.rapidapi.com/words/${this.userResponse}/definitions`, {
          params: {},
          headers: {
            'X-Mashape-Key': "baa65c740dmsh7c4edd371ac192ap10438bjsn187c5c8263c4",
            // 'X-RapidAPI-Key': 'EUgrtpQMpfvvYbZp6zqMmJiWNGtGENsuoY1D00TL',
            // 'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com',
            'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com',
            accept: "application/json",
          }
        }).then(response =>
          // Returns an array with dicts storing defintion and partOfSpeech:
          //  [ {"definition": "blah", "partOfSpeech": "blah"}... ] accessed by index
          (this.definition = response.data.definitions))
          .catch(error => {
            console.log(error)
            this.errored = true
        })
        .finally(() => this.loading = false)
      }
    },
    computed: {
      list: ({ jokes, index }) => jokes.slice(0, index)
    },
})