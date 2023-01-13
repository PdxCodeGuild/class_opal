new Vue({
    el: '#app',
    data: {
        newTodoText: '',
        todos: [
            {item: 'Step 1: Learn how to make a todo list',
            completed: true,
            isActive: true,
            id: 0,},
            {item: 'Step 2: Finish drafting first ver',
            completed: true,
            isActive: false,
            id: 1,},
            {item: 'Step 3: Make important toggle',
            completed: false,
            isActive: false,
            id: 2,},
        ],
        itemIncrement: 3,
    },
    methods: {
        addNewTodo: function () {
            this.todos.push({
                // builds the new todo item then clears the string afterward to be reused
              item: this.newTodoText,
              completed: false,
              isActive: true,
              id: this.itemIncrement,
            },)
            this.itemIncrement++
            this.newTodoText = ''
        },
        removeTodo(todoItem) {
            // Accessing relevant index of the todo and removing the item in the array
            const myIndex = this.todos.indexOf(todoItem)
            this.todos.splice(myIndex, 1);
        },
        markComplete(task) {
            task.completed = true;
        },
        markIncomplete(task) {
            task.completed = false;
        },
        toggleClass: function(todo){
            const myIndex = this.todos.indexOf(todo)
            this.todos[myIndex].isActive =!this.todos[myIndex].isActive;
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