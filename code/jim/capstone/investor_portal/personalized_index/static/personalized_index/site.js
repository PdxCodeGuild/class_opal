const { createApp } = Vue

createApp({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: function () {
        return {
            user: '',
            indexes: [],
            index_name: '',
            index_allocation: '',
            market_cap_min: '',
            dividend_yield_min: '',
            pe_ratio_max: '',
            sector_exclude_1: '',
            sector_exclude_2: '',
            edit_index_id: '',
            edit_index_name: '',
            edit_index_allocation: '',
            edit_market_cap_min: '',
            edit_dividend_yield_min: '',
            edit_pe_ratio_max: '',
            edit_sector_exclude_1: '',
            edit_sector_exclude_2: '',
            csrfToken: '',
        }
    },
    mounted() {
        // fetch the CSRF token from a meta tag when the component is created
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value;
        console.log(`the component is now mounted.`);
    },
    methods: {
        fetchPersonalizedIndex: function () {
            axios.get('/apis/v1/')
                .then(response => {
                    this.indexes = response.data;
                })
                .catch(error => {
                    console.error(error);
                });
        },
        createPersonalizedIndex: function (event) {
            event.preventDefault();
            axios.post('/apis/v1/', {
                index_name: this.index_name,
                index_allocation: this.index_allocation,
                market_cap_min: this.market_cap_min,
                dividend_yield_min: this.dividend_yield_min,
                pe_ratio_max: this.pe_ratio_max,
                sector_exclude_1: this.sector_exclude_1,
                sector_exclude_2: this.sector_exclude_2,
                user: this.user_id,
            }, {
                headers: {
                    'X-CSRFToken': this.csrfToken,
                },
            })
                .then(response => {
                    // Assume that the response data is a list of items
                    let items = response.data;
                    // Loop through the list of items
                    for (let i = 0; i < items.length; i++) {
                        let item = items[i];
                        // Append the item to the list
                        this.itemList.push(item);
                    }
                });
        },
        deletePersonalizedIndex: function (indexId) {
            axios.delete(`/apis/v1/${indexId}/`, {
                headers: {
                    'X-CSRFToken': this.csrfToken,
                },
            })
                .then(response => {
                    console.log(response.data);
                    this.indexes = this.indexes.filter(p => p.number !== indexId);
                })
                .catch(error => {
                    console.error(error);
                });
        },
        editPersonalizedIndex: function (indexId) {
            axios.put(`/apis/v1/${indexId}/`, {
                index_name: this.edit_index_name,
                index_allocation: this.edit_index_allocation,
                market_cap_min: this.edit_market_cap_min,
                dividend_yield_min: this.edit_dividend_yield_min,
                pe_ratio_max: this.edit_pe_ratio_max,
                sector_exclude_1: this.edit_sector_exclude_1,
                sector_exclude_2: this.edit_sector_exclude_2,
            }, {
                headers: {
                    'X-CSRFToken': this.csrfToken,
                },
            })
                .then(response => {
                    console.log(response.data);
                    this.fetchPersonalizedIndex();
                })
                .catch(error => {
                    console.error(error);
                });
        },
        async getOrders(index_id) {
            try {
                const { data } = await axios.get('/apis/v1/download/orders/' + index_id + '/');

                console.log(index_name)
                const response = await axios({
                    url: '/apis/v1/download/orders/' + index_id + '/',
                    method: 'GET',
                    responseType: 'blob',
                });
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'orders_' + index_id + '.csv'); //, `orders_${index_name}.csv`); //.replace('${index_name}', index_name));
                document.body.appendChild(link);
                link.click();
            } catch (error) {
                console.log(error);
            }
        },
        async getIndex(index_id) {
            try {
                const { data } = await axios.get('/apis/v1/download/index/' + index_id + '/');

                console.log(index_name)
                const response = await axios({
                    url: '/apis/v1/download/index/' + index_id + '/',
                    method: 'GET',
                    responseType: 'blob',
                });
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'personalized_index_' + index_id + '.csv');
                document.body.appendChild(link);
                link.click();
            } catch (error) {
                console.log(error);
            }
        },
    },
    created: function () {
        this.fetchPersonalizedIndex();
    },
}).mount('#app')