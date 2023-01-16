new Vue({
    el: '#app',
    data: {
      foximage: null,
      spaceimage: null,
      loading: true,
      errored: false,
      pun: null,
      definition: null,
    },
    mounted() {
      this.getSpaceImage(),
      this.getFoxImage()
    },
    methods: {
      getFoxImage() {
        axios
        .get('https://randomfox.ca/floof/?ref=apilist.fun/', {
          params: {},
        headers: {},
        }).then(response => 
            (this.foximage = response.data.image
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
          (this.spaceimage = response.data.hdurl
        ))
      },
      getPun() {
        axios.get('https://icanhazdadjoke.com/search', {
          params: {term: 'cat'},
          headers: {accept: 'application/json'},
        }).then(response =>
          // Hard-coded but might just have to go 
          // v-for pun in puns, pun at indexof .joke or something like that
          (this.pun = response.data.results[0].joke
        ))
      },
      getDefinition() {
        axios.get('https://wordsapiv1.p.rapidapi.com/words/cat/definitions', {
          params: {word: 'word'},
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
      }
    }
})