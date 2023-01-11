new Vue({
    el: '#app',
    data: {
        newTodoText: '',
        todos: [
            {item: 'Step 1: Learn how to make a todo list',
            completed: false,
            isActive: true,
            id: 0,},
        ],
        itemIncrement: 1,
    },
    methods: {
        addNewTodo: function () {
            this.todos.push({
                // builds the new todo item then clears the string afterward to be reused
              item: this.newTodoText,
              completed: false,
              isActive: true,
            },)
            this.itemIncrement++
            this.newTodoText = ''
        },
        removeTodo(todoItem) {
            // Remove item at its index in the array
            const myIndex = this.todos.indexOf(todoItem)
            this.todos.splice(myIndex, 1);
        },
        markComplete(task) {
            task.completed = true;
        },
        markIncomplete(task) {
            task.completed = false;
        },
        toggleClass: function(id){
            // this.isActive =!this.isActive;
            this.todos[id].isActive =!this.todos[id].isActive;
            // console.log(this.isActive)
        }
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