// https://jsonplaceholder.typicode.com/
// response headers: [ "data", "status", "statusText", "headers", "config", "request" ]



const App = {
    el: '#app',
    data() {
        return {
            output: {}
        }
    },
    mounted() {
        console.log('this happens when the page mounts')
        this.getUsers()
    },
    updated() {
        console.log('this happens every time the page updates')
        // if (newVersion !== oldVersion) {
        //     // do thing
        // }
    },
    methods: {
        getUsers() {
            // GET REQUEST
            console.log('GET Request');
            // axios({
            //     method: 'get',
            //     url: 'https://jsonplaceholder.typicode.com/users',
            //     params: { id: 4 }
            // })
            axios.get('https://jsonplaceholder.typicode.com/users', {
                params: { id: 5 }
            }).then(res => this.output = res)
                .catch(err => console.error(err))
        },
        addUser() {
            // POST REQUEST
            console.log('POST Request');
            axios.post('https://jsonplaceholder.typicode.com/users', {
                name: 'Fake Person',
                email: 'fake@person.com',
                id: 200,
                garbage: ':)'
            }).then(response => this.output = response)
                .catch(error => console.error(error))
        },
        updateUser() {
            // PUT/PATCH REQUEST
            // PUT replaced the entire record
            // PATCH only changes the specified keys on the record
            console.log('PUT Request');
            axios.patch('https://jsonplaceholder.typicode.com/users/3', {
                name: 'Fake Person',
                email: 'fake@person.com',
                id: 200,
                garbage: ':)'
            }).then(response => this.output = response)
                .catch(error => console.error(error))
        },
        removeUser() {
            // DELETE REQUEST
            console.log('DELETE Request');
            axios.delete('https://jsonplaceholder.typicode.com/users/3')
                .then(response => this.output = response)
                .catch(error => console.error(error))
        }
    }
}
const app = Vue.createApp(App)
app.mount('#app')