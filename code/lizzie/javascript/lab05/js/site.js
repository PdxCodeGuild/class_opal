new Vue({
    el: '#app',
    data: {
        cohortName: 'Class Opal',
        startDate: 'October 31',
        message: 'Hello world!',
        newTodoText: '',
        todos: [
        {item: 'Do the dishes'},
        ],
        completeTodo: [''],
        inputField: 'starter value',
    },
    methods: {
        addNewTodo: function () {
            this.todos.push({
              item: this.newTodoText
            })
            this.newTodoText = ''
          }
    }
})