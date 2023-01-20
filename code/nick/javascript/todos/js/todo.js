Vue.component('TodoItem', {
    template: `
    <div class="col s12">
    <div class="card blue-grey darken-2 center">
      <div class="card-content white-text">
        <p>{{ todo.todoText }}</p>
        <div class="card-action">
          <label class="left">
            <input type="checkbox" class="filled-in  red lighten-2" @click="$emit('complete-todo', todo)" :checked="todo.complete"/>
            <span class=" red-text text-lighten-2">Complete</span>
          </label>
          <a class="waves-effect waves-light btn-small red lighten-2 right" @click="$emit('delete-todo', todo)"><i class="material-icons right">delete</i>Delete</a>
        </div>
      </div>
    </div>
  </div>`,
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
        completeTodo(todo) {
            todo.complete = !todo.complete
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
            return this.todoItems.filter( (td) => !td.complete )
        },
        complete() {
            return this.todoItems.filter( (td) => td.complete )
        },
    }
})
     