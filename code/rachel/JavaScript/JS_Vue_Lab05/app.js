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
        // complete: function(todo) {
        //     let todoItem = {
        //       text: this.todoItem
        //     }
        complete: function (todo) {
            this.completedItems.push(todo)
            this.todos.splice(this.todos.indexOf(todo), 1)
           
        }
    }
  })
