new Vue({
    el: '#app',
    data: {
      todos: [ 
        { text: 'Learn JavaScript' },
        { text: 'Learn Vue' },
        { text: 'Build something awesome' },
        // { text: '' },
      ],
      completedItems: [
        { text: 'walk the dog' },
        { text: 'buy groceries' },
      ]
    },
    methods: {
        addNewItem () {
            let newItem = {
                text: this.newItem
            }
            this.todos.push(newItem)
        },
        complete () {
            this.todos.remove(this.todo)
            this.completedItems.push(this.todo)
        }
    }
  })
