new Vue({
    el: '#app',
    data: () => {
        return {
            output: 'hello',
            insultText: '',
        }
    },
    // Question 1: how to take output from getInsult and/or haveInsult text input and use as parameter for the language translations - work on post response
    // Question 2: Instead of having a seperate method for each language, can I just substitute in a keyword in the URL? and what would the button input in HTML need to look like?
    methods: {
        getInsult() {
            console.log('GET Request'),
            axios({
                method: 'get',
                url: 'https://insult.mattbas.org/api/insult/type=json',
            }).then(res => this.insultText = res.data)
            .catch(err => console.error(err))
            // }).then(function (response) {
            //     console.log(response.data);
            // })
        }, 
        // sendInsult() {
        //     axios({
        //         method: 'post',
        //         url: 'https://evilinsult.com/generate_insult.php?lang=en&type=json',


        //     })
        // },
        // shakespeare () {
        //     console.log('GET Request');
        //     axios({
        //         method: 'get',
        //         url: 'https://api.funtranslations.com/translate/shakespeare.json',
        //         //is this how you add header info?
        //         params: {'contents': {'text': insultText}}
        //     }).then(res => this.output = contents.translated)
        //     .catch(err => console.error(err))
        // },
        // klingon() {
        //     console.log('GET Request');
        //     axios({
        //         method: 'get',
        //         url: 'https://api.funtranslations.com/translate/klingon.json',
        //         //is this how you add header info?
        //         params: {'contents': {'text': insult}}
        //     }).then(res => this.output = contents.translated)
        //     .catch(err => console.error(err))
        // },
        // vulcan() {
        //     console.log('GET Request');
        //     axios({
        //         method: 'get',
        //         url: 'https://api.funtranslations.com/translate/vulcan.json',
        //         //is this how you add header info?
        //         params: {'contents': {'text': insult}}
        //     }).then(res => this.output = contents.translated)
        //     .catch(err => console.error(err))
        // },
        // pirate() {
        //     console.log('GET Request');
        //     axios({
        //         method: 'get',
        //         url: 'https://api.funtranslations.com/translate/pirate.json',
        //         //is this how you add header info?
        //         params: {'contents': {'text': insult}}
        //     }).then(res => this.output = contents.translated)
        //     .catch(err => console.error(err))
        // },
        // redneck() {
        //     console.log('GET Request');
        //     axios({
        //         method: 'get',
        //         url: 'https://api.funtranslations.com/translate/redneck.json',
        //         //is this how you add header info?
        //         params: {'contents': {'text': insult}}
        //     }).then(res => this.output = contents.translated)
        //     .catch(err => console.error(err))
    }
})
