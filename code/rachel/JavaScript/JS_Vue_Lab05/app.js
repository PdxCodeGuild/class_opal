new Vue({
    el: '#app',
    data: {
      todos: [ 
        { text: 'make a list!'},
      ],
      completedItems: [
        { text: 'walk the dog' },
        { text: 'buy groceries' },
      ],
    },
    methods: {
        addNewItem () {
            let newItem = {
                text: this.newItem
            }
            this.todos.push(newItem)
        },
        // clear(i){
        //   for (let key in this.todos[index]) {
        //     this.$set(this.todos[index], key, null);
        //   }
        // }, 
        add(todo) {
            let newItem = {
              text: this.newItem
            }
          this.completedItems.push(newItem),
          this.todos.splice(this.todos.indexOf(todo), 1)
        
        }
    }
  })
