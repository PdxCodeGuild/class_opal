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

            // url = 'https://favqs.com/api/quotes?'
            // params = {
            //     'page' : str(page),
            //     'filter' : user_keyword
            // }
            // headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
            // built_url = requests.get(url, params=params, headers=headers)
            // quotes_info = built_url.json()
            
            
            axios.get('https://favqs.com/api/quotes?', {
                params: { 
                    'page' : 1,
                    'filter' : 'flower',
                },
                headers: {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
            }).then(res => this.output = res)
                .catch(err => console.error(err))

            // axios.get('https://jsonplaceholder.typicode.com/users', {
            //     params: { id: 5 }
            // }).then(res => this.output = res)
            //     .catch(err => console.error(err))
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