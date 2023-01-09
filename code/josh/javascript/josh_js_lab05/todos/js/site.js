new Vue({
    el: '#app',
    data: {
        listItems: ['Laundry'],
        completed: '',
        delete: '',
        userItem: ''
    },
    methods: {
        addItem () {
            this.listItems.push(this.userItem)
        },
        completed () {

        },
        delete () {
            
        }
    }})


/* 
Store an array of objects (the todos themselves)
List each todo
Allow the user to add and remove todos
Allow a user to toggle if a task is complete or not
*/