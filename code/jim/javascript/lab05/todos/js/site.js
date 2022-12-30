new Vue({
    el: '#app',
    data: {
        newTodo: '',
        todos: [
            { text: 'Learn Vue.js', completed: false },
            { text: 'Build a todo app', completed: false },
            { text: 'Finish Lab05', completed: true }
        ]
    },
    computed: {
        completedTodos() {
            return this.todos.filter(todo => todo.completed);
        },
        incompleteTodos() {
            return this.todos.filter(todo => !todo.completed);
        }
    },
    methods: {
        addTodo() {
            this.todos.push({
                text: this.newTodo,
                completed: false
            });
            this.newTodo = '';
        },
        removeTodo(todoItem) {
            let myIndex = this.todos.indexOf(todoItem)
            this.todos.splice(myIndex, 1);
        },
        handleCompleteness(todoItem) {
            let myIndex = this.todos.indexOf(todoItem)
            todoItem.completed = !todoItem.completed
            this.todos[myIndex] = todoItem
            console.log(todoItem)
        }
    }
});
