Vue.component('Counter', {
    // send information up into a parent component using emitted events
    // define the event name here with $emit() and then listen for that event in the app
    template: `<button @dblclick="$emit('my-event')" @click="count++">{{ count }}</button>`,
    data: () => {
        return {
            count: 0
        }
    }
})


Vue.component('BookItem', {
    template: `
        <p class="book" v-on="checkedOut ? {click: checkIn} : {click: checkOut}" :class="{out: checkedOut}">
            <strong>{{ book.title }}</strong><br>
            {{ book.author }}<br>
            checked out {{ timesCheckedOut }} times
            <button @click="$emit('delete-book', book)">❌</button>
        </p>`,
    data: () => {
        return {
            checkInDate: Date.now(),
            checkOutDate: null,
            timesCheckedOut: 0
        }
    },
    props: {
        book: {
            // if you don't need this level of detail, you can just list the prop names in an array
            type: Object,
            required: true, // true is default
            validator: (book) => {
                return book.title && book.author && book.id
            }
        }
    },
    methods: {
        checkOut() {
            this.timesCheckedOut++
            this.checkOutDate = Date.now()
        },
        checkIn() {
            this.checkInDate = Date.now()
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
    methods: {
        removeBook(book) {
            const index = this.books.indexOf(book)
            if (index !== -1) {
                this.books.splice(index, 1)
            }
        }
    },
    data: {
        libraryName: 'Class Opal Library',
        emittedCount: 0,
        books: [
            {
                id: 1,
                title: "Future Home of the Living God",
                author: "Louise Erdritch"
            },
            {
                id: 2,
                title: "Last Night at the Telegraph Club",
                author: "Malinda Lo"
            },
            {
                id: 3,
                title: "Braiding Sweetgrass",
                author: "Robin Wall Kimmerer"
            },
            {
                id: 4,
                title: "The Bluest Eye",
                author: "Toni Morrison"
            },
            {
                id: 5,
                title: "A Long Petal of the Sea",
                author: "Isabel Allende",
            },
            {
                id: 6,
                title: "A Tale for the Time Being",
                author: "Ruth Ozeki"
            },
            {
                id: 7,
                title: "Disorientation",
                author: "Elaine Hsieh Chou"
            },
            {
                id: 8,
                title: "The Fifth Season",
                author: "N. K. Jemisin"
            },
            {
                id: 9,
                title: "Americanah",
                author: "Chimamanda Ngozi Adichie"
            },
            {
                id: 10,
                title: "Woman at Point Zero",
                author: "Nawal El-Saadawi"
            },
            {
                id: 11,
                title: "Persepolis",
                author: "Marjane Satrapi"
            },
            {
                id: 12,
                title: "In the Dream House",
                author: "Carmen Maria Machado"
            },
            {
                id: 13,
                title: "Gold Diggers",
                author: "Sanjeetha Sathian"
            },
            {
                id: 14,
                title: "Kindred",
                author: "Octavia Butler"
            },
            {
                id: 15,
                title: "Akata Witch",
                author: "Nnedi Okorafor"
            },
            {
                id: 16,
                title: "Passing",
                author: "Nella Larsen"
            },
            {
                id: 17,
                title: "Black Water Sister",
                author: "Zen Cho"
            },
            {
                id: 18,
                title: "Their Eyes Were Watching God",
                author: "Zora Neal Hurston"
            },
            {
                id: 19,
                title: "Iron Widow",
                author: "Xiran Jay Zhao"
            },
            {
                id: 20,
                title: "Jasmine",
                author: "Bharati Mukherjee"
            },
            {
                id: 21,
                title: "The Farming of Bones",
                author: "Edwidge Danticat"
            },
            {
                // this one is going to throw a warning from the validator
                id: 22
            }
        ]
    }
})
