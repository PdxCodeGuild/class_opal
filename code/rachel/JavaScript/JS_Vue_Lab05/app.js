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
        complete: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
            this.completedItems.push(this.todos)
        }
    }
  })
