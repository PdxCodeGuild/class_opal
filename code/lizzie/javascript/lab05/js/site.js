new Vue({
    el: '#app',
    data: {
        newTodoText: '',
        todos: [
            {item: 'Learn how to make a todo list',
            completed: false,
            id: 1,}
        ],
        itemIncrement: 1
    },
    methods: {
        addNewTodo: function () {
            this.todos.push({
                // builds the new todo item then clears the string afterward to be reused
              item: this.newTodoText,
              completed: false,
              id: this.itemIncrement,
            },)
            this.itemIncrement++
            this.newTodoText = ''
        },
        removeTodo(todoItem) {
            // Remove item at its index in the array
            const myIndex = this.todos.indexOf(todoItem)
            this.todos.splice(myIndex, 1);
        },
        markComplete(id) {
            this.id.completed = true;
        },
        markIncomplete(id) {
            this.todos[id].completed = false;
        },
    },
    computed: {
        completeTodos() {
            return this.todos.filter(todo => todo.completed);
        },
        incompleteTodos() {
            return this.todos.filter(todo => !todo.completed);
        },
    },
},
)