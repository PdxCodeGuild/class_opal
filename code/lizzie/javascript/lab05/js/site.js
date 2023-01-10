new Vue({
    el: '#app',
    data: {
        newTodoText: '',
        todos: [],
    },
    methods: {
        addNewTodo: function () {
            this.todos.push({
              item: this.newTodoText,
              completed: false,
            },)
            this.newTodoText = ''
        },
        removeTodo(todoItem) {
            // Remove item at its index in the array
            let myIndex = this.todos.indexOf(todoItem)
            this.todos.splice(myIndex, 1);
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
        },
    },
},
)