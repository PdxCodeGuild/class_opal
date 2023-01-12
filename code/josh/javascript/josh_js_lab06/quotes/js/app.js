// const axios = require('axios');

new Vue ({
    el: '#app',
    data: {
        output: {}
        },
    methods: {
        getQuote() {
            console.log('GET request');
            axios.get('https://favqs.com/api/quotes/', {
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                    'Content-Type': 'application/json'},
                params: {
                    'filter': 'keyword',
                    // 'type': 
                }
    }).then(response => this.output = response)
    .then(data => console.log(data))
    .catch(error => console.error(error))
    },
}})


// Let the user enter a search term and select whether to search by keyword, author, or tag.
// When the page first loads, show the user a set of completely random quotes.
// You must have at least one Vue component in your app. Review components here
// 
// Read the API documentation!
// Remember to use your Vue app data as your single source of truth.
// You'll need to set the Authorization header for the FavQs API to work.

            // header: {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
            // parameters: {'filter': keyword, 'page': page}, //stores user input and page number to allow search terms and next page functionality in URL
            // searchResponse: requests.get('https://favqs.com/api/quotes', params=parameters, headers=header),
        //     searchResponseText: search_response.json(),
        //     quotesList: searchResponseText['quotes'], //sorts returned list index 'quotes'
        //     response: requests.get('https://favqs.com/api/qotd'),
        //     responseText: response.json(),
        //     author: response_text['quote']['author'],
        //     quote: response_text['quote']['body'],
        //     qotd: 'https://favqs.com/api/qotd'
        // },