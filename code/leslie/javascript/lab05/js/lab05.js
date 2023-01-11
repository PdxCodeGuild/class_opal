new Vue({
    el: '#app',
    data: {
        newItem: '', // Add Todo input goes here
        items: [
            {
                id: 1,
                name: 'learn Vue',
                completed: false,

            },
            {
                id: 2,
                name: "walk dogs",
                completed: false,
            },

        ],
    },
    computed: {
        reversedItems() {
            return this.items.slice(0).reverse();
        },
    },
    methods: {
        addItem: function () {
            this.items.push({
                id: this.items.length + 1,
                name: this.newItem,
                completed: false,
            });
            this.newItem = '';
        },
        toggleCompleted: function (item) {
            item.completed = !item.completed;
        },
        removeItem: function (item) {
            this.items = this.items.filter((newItem) => newItem.name !== item.name);
        },
    }
})