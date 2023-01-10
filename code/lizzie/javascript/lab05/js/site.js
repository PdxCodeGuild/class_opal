new Vue({
    el: '#app',
    data: {
        cohortName: 'Class Opal',
        startDate: 'October 31',
        message: 'Hello world!',
        newTodoText: '',
        todos: [
        {item: 'This inst done', completed: false},
        {item: 'I am not done either', completed: false},
        {item: 'i am super done', completed: true},
        {item: 'i am done too', completed: true},
        ],
    },
    methods: {
        addNewTodo: function () {
            this.todos.push({
              item: this.newTodoText,
              completed: false,
            })
            this.newTodoText = ''
        },
        removeTodo(todoItem) {
            // Remove item at its index in the array
            this.todos.splice(this.todos.indexOf(todoItem), 1);
        },
        markComplete(index) {
            this.todos[index].completed = true;
        },
        markIncomplete(index) {
            this.todos[index].completed = false;
        },
    },
    computed: {
        incompleteTodos() {
            return this.todos.filter(todo => !todo.completed);
        },
        completeTodos() {
            return this.todos.filter(todo => todo.completed);
        }
    }
})