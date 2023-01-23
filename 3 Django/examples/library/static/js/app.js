Vue.component('BookItem', {
    template: `
        <p class="book" v-on="checkedOut ? {click: checkIn} : {click: checkOut}" :class="{out: checkedOut}">
            <strong>{{ book.title }}</strong><br>
            {{ book.author }}<br>
            checked out {{ timesCheckedOut }} times
            <button @click="removeBook">❌</button>
        </p>`,
    data: () => {
        return {
            checkInDate: Date.now(),
            checkOutDate: null,
            timesCheckedOut: 0
        }
    },
    props: ['book', 'csrftoken'],
    methods: {
        checkOut() {
            this.timesCheckedOut++
            this.checkOutDate = Date.now()
        },
        checkIn() {
            this.checkInDate = Date.now()
        },
        removeBook() {
            axios.delete(`/api/v1/${this.book.id}`, {
                headers: { 'X-CSRFToken': this.csrftoken }
            }).then(res => this.$el.parentNode.removeChild(this.$el))
        }
    },
    computed: {
        checkedOut() {
            return this.checkOutDate > this.checkInDate
        }
    }
})

new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        libraryName: 'Class Opal Library',
        books: null,
        csrfToken: null,
        newTitle: '',
        newAuthor: ''
    },
    methods: {
        getBooks() {
            console.log(this)
            axios.get('/api/v1').then(res => this.books = res.data)
        },
        addBook() {
            // because the BookItem components can delete themselves
            // the Root vue instance doesn't always know where to insert new DOM elements
            // calling this.getBooks will refresh its knowledge and re-render
            this.getBooks()
            axios.post('/api/v1/new/', {
                'title': this.newTitle,
                'author': this.newAuthor
            }, {
                headers: { 'X-CSRFToken': this.csrfToken }
            }).then(res => this.getBooks())

            this.newAuthor = ''
            this.newTitle = ''
        },
        // removeBook(book) {
        //     axios.delete(`/api/v1/${book.id}`, {
        //         headers: { 'X-CSRFToken': this.csrfToken }
        //     }).then(res => this.getBooks())
        // }
    },
    mounted() {
        this.getBooks()
        this.csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value
    }
})
