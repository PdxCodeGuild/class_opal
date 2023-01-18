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
            voiceSelection: 'Obama',
            headsPost: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            headGet: {
                'Accept': 'application/json',
            },
            progress: ['pending', 'started'],
            kanyeQuote: null,
            jobToken: null,
            pollResult: null,
            ttsStatus: null,
            audioPath: null,

        }
    },
    methods: {
        async apiCycle() {
            await Promise.all([
                axios.get('https://api.kanye.rest')
                .then(res => this.kanyeQuote = res.data.quote),
                axios.post('https://api.fakeyou.com/tts/inference', {'uuid_idempotency_token': this.uuidToken(),
                'tts_model_token': this.voiceTokens.Obama,
                'inference_text': this.kanyeQuote}, { headers: this.headsPost })
                .then(res => this.jobToken = res.inference_job_token),
            ]);
                
            const statusPoll = async () => {
                await axios.get(`https://api.fakeyou.com/tts/job/${this.jobToken}`, { headers: this.headGet })
                    .then(res => this.pollResult = res);
                
                this.ttsStatus = this.pollResult.state.status
                const relPath = this.ttsStatus.state.maybe_public_bucket_wav_audio_path
                if (relPath) { this.audioPath = `https://storage.googleapis.com/vocodes-public${relPath}` }
                else if (this.progress.includes(this.ttsStatus)) { setTimeout(statusPoll(), 2000) }
            }
        },
        // fakeYou() {
        //     let payload = {
        //         'uuid_idempotency_token': this.uuidToken(),
        //         'tts_model_token': 'TM:58vtv7x9f32c',
        //         'inference_text': 'Testing'
        //     }
        //     axios.post('https://api.fakeyou.com/tts/inference', payload, { headers: this.headsPost })
        //             .then(res => console.log(res.inference_job_token))
        // },
        uuidToken() {
            let tokenArray = []
            const range = 20
            for (let i = 0; i < range; i++) {
                tokenArray.push(Math.floor(Math.random() * 10))
            }
            return tokenArray.join('')
        },
    },
})