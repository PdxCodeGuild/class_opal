new Vue ({
    el: '#app',
    data: {
        header: {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
        parameters: {'filter': keyword, 'page': page}, //stores user input and page number to allow search terms and next page functionality in URL
        searchResponse: requests.get('https://favqs.com/api/quotes', params=parameters, headers=header),
        searchResponseText: search_response.json(),
        quotesList: searchResponseText['quotes'], //sorts returned list index 'quotes'
        response: requests.get('https://favqs.com/api/qotd'),
        responseText: response.json(),
        author: response_text['quote']['author'],
        quote: response_text['quote']['body'],
    },
    methods: {

    },
})