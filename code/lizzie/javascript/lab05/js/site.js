new Vue({
    el: '#app',
    data: {
        cohortName: 'Class Opal',
        startDate: 'October 31',
        message: 'Hello world!',
        newTodoText: '',
        todos: [
        {item: 'Create 5 more todo lists'},
        ],
        completeTodo: [''],
    },
    methods: {
        addNewTodo: function () {
            this.todos.push({
              item: this.newTodoText
            })
            this.newTodoText = ''
          },
        removeTodo(todoItem) {
            // Remove item at its index in the array
            this.todos.splice(this.todos.indexOf(todoItem), 1);
          },
    },
})