new Vue({
    el: '#app',
    data () {
      return {
        image: null,
        loading: true,
        errored: false
      }
    },
    mounted () {
      axios
        .get('https://randomfox.ca/floof/?ref=apilist.fun/', {
          params: {},
        headers: {},
        }).then(response => 
            (this.image = response.data.image
        ))
        .catch(error => {
            console.log(error)
            this.errored = true
        })
        .finally(() => this.loading = false)
    },
})