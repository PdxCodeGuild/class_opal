Vue.component('incompleteItem', {
    template: '...'
    ,
    data: () => {
        return {
            
        }
    },
    props: {
        todo: {
            type: Object,
        },
    },
    methods: {

    },
})





new Vue({
    el: '#app',
    methods: {
        addTodo() {
            console.log(this.newTodoText)
            if ( this.newTodoText.length > 0 ) {
                this.currentId++
                this.todoItems.unshift({ id: this.currentId, todoText: this.newTodoText, complete: false })
                console.log(this.todoItems[0])
                this.newTodoText = ''
            }
        },
        removeTodo(todo) {
            const index = this.todoItems.indexOf(todo)
            if (index !== -1) {
                this.todoItems.splice(index, 1)
            }
        },
        completeTodo() {

        },
    },
    data: {
        currentId: 0,
        newTodoText: '',
        todoItems: [
            // {
                // id: this.currentId,
                // todoText: '',
                // complete: false
            // },
        ],
    },
    computed: {
        incomplete() {
            return this.todoItems.filter( (td) => td.complete )
        },
        complete() {
            return this.todoItems.filter( (td) => !td.complete )
        },
    }
})
     