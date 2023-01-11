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
            this.listItems[todoIndex].delete(todoItem)
        }
    },
    computed: {
}})


// Allow the user to remove todos