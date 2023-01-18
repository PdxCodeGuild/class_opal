new Vue({
    el: '#app',
    data: () => {
        return {
            test: 'hello',
            insultText: '',
            translation: '',
        }
    },
    // Note: to take output from getInsult and/or haveInsult text input and use as parameter for the language translations, just include response (here: insultText) as an argument for the @click method both in html and app.js
    
    methods: {
        getInsult() {
            //console.log('GET Request'),
            axios({
                method: 'get',
                url: 'https://insult.mattbas.org/api/insult/type=json',
            }).then(res => this.insultText = res.data)
            .catch(err => console.error(err))
            // }).then(function (response) {
            //     console.log(response.data);
            // })
        },
        resize() {
            this.style.width = this.value.length + "ch"
        },
        shakespeare(insultText) {
            console.log(insultText),
            axios({
                method: 'get',
                url: 'https://api.funtranslations.com/translate/shakespeare.json',
                //params: {'text': 'hey girl'} //this works
                params: {'text':insultText.trimEnd()} // insultText returns a string w/ an extra space on the end which returns a 404 error, so using trimEnd to remove that space 
            }).then(response => this.translation = response.data.contents.translated) // this works
            .catch(err => console.error(err))
            // }).then(function (response) {
            //     console.log(response.data);
            // })
        }, 
        klingon(insultText) {
            console.log(insultText),
            axios({
                method: 'get',
                url: 'https://api.funtranslations.com/translate/klingon.json',
                //params: {'text': 'hey girl'} //
                params: {'text':insultText.trimEnd()} 
            }).then(response => this.translation = response.data.contents.translated) 
            .catch(err => console.error(err))
            // }).then(function (response) {
            //     console.log(response.data);
            // })
        },
        vulcan(insultText) {
            console.log(insultText),
            axios({
                method: 'get',
                url: 'https://api.funtranslations.com/translate/vulcan.json',
                //params: {'text': 'hey girl'} 
                params: {'text':insultText.trimEnd()} 
            }).then(response => this.translation = response.data.contents.translated)
            .catch(err => console.error(err))
            // }).then(function (response) {
            //     console.log(response.data);
            // })
        },
        pirate(insultText) {
            console.log(insultText),
            axios({
                method: 'get',
                url: 'https://api.funtranslations.com/translate/pirate.json',
                //params: {'text': 'hey girl'}
                params: {'text':insultText.trimEnd()} 
            }).then(response => this.translation = response.data.contents.translated)
            .catch(err => console.error(err))
            // }).then(function (response) {
            //     console.log(response.data);
            // })
        },
        redneck(insultText) {
            console.log(insultText),
            axios({
                method: 'get',
                url: 'https://api.funtranslations.com/translate/redneck.json',
                //params: {'text': 'hey girl'} 
                params: {'text':insultText.trimEnd()} 
            }).then(response => this.translation = response.data.contents.translated)
            .catch(err => console.error(err))
            // }).then(function (response) {
            //     console.log(response.data);
            // })
        },
        yoda(insultText) {
            console.log(insultText),
            axios({
                method: 'get',
                url: 'https://api.funtranslations.com/translate/yoda.json',
                //params: {'text': 'hey girl'} 
                params: {'text':insultText.trimEnd()} 
            }).then(response => this.translation = response.data.contents.translated)
            .catch(err => console.error(err))
            // }).then(function (response) {
            //     console.log(response.data);
            // })
        },
    }
})
//Problems:
// API calls limited to 5 per hour / 60 per day which is not great for testing

//Additional options:
// 1) Instead of having a seperate method for each language: substitute in keyword in the URL.
// 2) Return/render error message (429) if user goes over the allotted 5 requests to a specific API (per hour)