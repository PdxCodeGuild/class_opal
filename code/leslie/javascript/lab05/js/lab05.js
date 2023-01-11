new Vue({
    el: '#app',
    data: {
        newItem: '', // input from "add Todo" goes in here, added "v-model='newItem'" to input tag
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
            return this.items.slice(0).reverse(); // renders items list backwards
        },
    },
    methods: {
        addItem: function () { //pushes newItem to items array
            this.items.push({
                id: this.items.length + 1,
                name: this.newItem,
                completed: false,
            });
            this.newItem = ''; //clears out newItem value from input
        },
        toggleCompleted: function (item) { //can toggle item from comeplete to incomplete
            item.completed = !item.completed;
        },
        removeItem: function (item) {
            this.items = this.items.filter((newItem) => newItem.name !== item.name);
        },
    }
})