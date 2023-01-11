new Vue({
    el: '#app',
    data: {
        listItems: [],
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
        },
        // Item text is lined-through if complete
        itemComplete (todoItem) {
            return {
                completedItem: todoItem.completed
            }},
        // Item is marked complete/incomplete
        boxChecked (todoItem) {
            let todoIndex = this.listItems.indexOf(todoItem)
            this.listItems[todoIndex].completed = !this.listItems[todoIndex].completed
        },

        deleteItem (todoItem) {
            let todoDelete = this.listItems.indexOf(todoItem)
            this.listItems[todoDelete].delete
        }
    },
    computed: {
}})


// Allow the user to remove todos