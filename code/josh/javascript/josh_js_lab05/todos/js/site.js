new Vue({
    el: '#app',
    data: {
        listItems: [],
        completed: '',
        delete: '',
        userItem: ''
    },
    methods: {
        addItem () {
            this.listItems.push(this.userItem)
        },
        clearInput () {
            this.userItem.value = ''
        },
        // completed () {

        // },
        // delete () {
        //     delete this.userItem?
        // }
    }})


/* 
Allow the user to remove todos
Allow a user to toggle if a task is complete or not
*/