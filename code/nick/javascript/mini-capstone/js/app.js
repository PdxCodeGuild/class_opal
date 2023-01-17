new Vue({
    el: '#app',
    data: () => {
        return {
            voiceTokens: {
                'Obama': 'TM:58vtv7x9f32c',
                'Gandhi': 'TM:cvw5qkye9y22',
                'Churchill': 'TM:3na2hzvbfqn7',
                'Kennedy': 'TM:a9pmkvtg2p6b',
                'FDR': 'TM:jh0bts33pn7x',
                'Teddy': 'TM:pn9edma33t2j',
            },
            kanyeQuote: null,
            audioPath: null,

        }
    },
    methods: {
        getKanyeQuote() {
            axios.get('https://api.kanye.rest')
            .then(res => this.kanyeQuote = res)
        }
    },
    computed: {
        uuidToken() {
            let tokenArray = []
            const range = 20
            for (let i = 0; i < range; i++) {
                tokenArray.push(Math.floor(Math.random() * 10))
            }
            return tokenArray.join()
        }
    },
})