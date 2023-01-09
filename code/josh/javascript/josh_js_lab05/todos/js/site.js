new Vue({
    el: '#app',
    data: {
        listItems: ['Laundry'],
        completed: '',
        delete: ''
    },
    userItem: () => {
        this.listItems.push()
    },
    methods: {
        logInput(e) {
            this.userItem = e.target.value
        }
    }})


/* 
Store an array of objects (the todos themselves)
List each todo
Allow the user to add and remove todos
Allow a user to toggle if a task is complete or not
*/