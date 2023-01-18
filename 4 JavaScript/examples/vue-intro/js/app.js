new Vue({
    el: '#app',
    data: {
        cohortName: 'Class Opal',
        startDate: 'October 31',
        gradDate: 'February 15',
        repo: 'https://github.com/PdxCodeGuild/class_opal/',
        clicks: 0,
        inputField: 'starter value',
        inputField2: '',
        a: 0,
        b: 0,
        students: [
            'Nick',
            'Josh',
            'Rachel',
            'Leslie',
            'Lizzie',
            'Jim'
        ],
        staff: [
            {
                name: 'Danny',
                title: 'instructor',
                isReal: true
            },
            {
                name: 'Gage',
                title: 'TA',
                isReal: true
            },
            {
                name: 'Puff the Magic Dragon',
                title: 'mascot',
                isReal: false
            }
        ],
        seasons: {
            spring: ['March', 'April', 'May'],
            summer: ['June', 'July', 'August'],
            fall: ['September', 'October', 'November'],
            winter: ['December', 'January', 'February']
        },
        isRed: false,
        isTransparent: false
    },
    methods: {
        clicker(count) {
            this.clicks += count
        },
        logInput(e) {
            this.inputField = e.target.value
        }
    },
    computed: {
        scoreA() {
            return this.a + 4
        },
        scoreB() {
            if (this.scoreA > this.b) {
                return this.scoreA + 3
            }
            return this.b
        },
        realStaff() {
            return this.staff.filter(s => s.isReal)
        },
        boxClasses() {
            return {
                boxRed: this.isRed,
                transparent: this.isTransparent
            }
        }
    }
})