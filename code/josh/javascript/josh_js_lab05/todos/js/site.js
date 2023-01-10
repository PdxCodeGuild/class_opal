new Vue({
    el: '#app',
    data: {
        listItems: [],
        completed: false,
        delete: '',
        userItem: ''
    },
    methods: {
        // Appends user input to 'listItems' array and clears input field
        addItem () {
            this.listItems.push({
                name: this.userItem,
                completed: false,
              }),
            this.userItem = ''
        }
            // this.listItems.push(this.userItem)
            // this.userItem = ''
    },
    computed: {
        itemComplete () {
            return {
                completedItem: this.completed
            }},

            
        // itemDelete () {
        //     return {
        //         deletedItem: this.delete
        //     }
        // }
}})


/* 
Allow the user to remove todos
Allow a user to toggle if a task is complete or not
*/