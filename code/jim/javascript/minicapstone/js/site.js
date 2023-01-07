new Vue({
    el: '#app',
    data() {
        return {
            financialData: '',
            symbol: '',
        }
    },
    methods: {
        stockQuote() {
            return axios.get('https://mboum-finance.p.rapidapi.com/hi/history', {
                // params: { symbol: this.symbol, module: 'financial-data' },
                params: { symbol: this.symbol, interval: '1mo', diffandsplits: 'false' },
                headers: {
                    'X-RapidAPI-Key': '0zotPkYey9mshuMn8ZAGIEMstMSyp1fQFA3jsnnIVcgEtc7lxi',
                    'X-RapidAPI-Host': 'mboum-finance.p.rapidapi.com'
                }
            })
                .then(response => {
                    console.log(response.data);
                    const data = response.data;
                    const result = Object.entries(data.items).map(([timestamp, item]) => [item.date, item.close]);
                    result.unshift(['date', 'close']);
                    // console.log(result)
                    // console.log(typeof result)
                    this.financialData = result;
                }).catch(function (error) {
                    console.error(error);
                });
            return this.financialData
        },
        drawChart(dataArray) {
            // Convert data array to DataTable object
            var data = google.visualization.arrayToDataTable(dataArray);
            // Set Options
            var options = {
                title: 'Closing Price History',
                hAxis: { title: 'Date' },
                vAxis: { title: 'Closing Share Price' },
                legend: 'none'
            };
            // Draw Chart
            var chart = new google.visualization.LineChart(document.getElementById('myChart'));
            chart.draw(data, options);
        },
        async getChart() {
            google.charts.load('current', { packages: ['corechart'] });
            const dataArray = await this.stockQuote();
            console.log(typeof dataArray)
            console.log(dataArray)
            console.log(typeof this.financialData)
            console.log(this.financialData)
            return this.drawChart(this.financialData)
        }
    },
})