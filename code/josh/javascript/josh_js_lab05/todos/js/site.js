new Vue({
    el: '#app',
    data: {
        listItems: [],
        completed: '',
        delete: '',
        userItem: ''
    },
    methods: {
        // Appends user input to 'listItems' array and clears input field
        addItem () {
            this.listItems.push(this.userItem)
            this.userItem = ''
        },
        completed () {
            // toggle completed/incomplete checkbox and strikethrough
        },
        delete () {
        //     delete this.userItem
        }
    }})


/* 
Allow the user to remove todos
Allow a user to toggle if a task is complete or not
*/