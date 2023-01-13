new Vue({
    el: '#app',
    data() {
        return {
            financialData: '',
            symbol: '',
            companyInfo: '',
            assetProfile: '',
        }
    },
    methods: {
        stockProfile() {
            // may need to request access at https://cors-anywhere.herokuapp.com/corsdemo
            // or https://thingproxy.freeboard.io/fetch/
            return axios.get('https://tiny-mountain-5aa6.jamesbrennan21.workers.dev/https://query1.finance.yahoo.com/v11/finance/quoteSummary/', {
                params: { symbol: this.symbol, modules: 'assetProfile' }
            })
                .then(response => {
                    const data = response.data;
                    this.assetProfile = data;
                }).catch(function (error) {
                    console.error(error);
                })
        },
        stockInfo() {
            return axios.get('https://tiny-mountain-5aa6.jamesbrennan21.workers.dev/https://query1.finance.yahoo.com/v7/finance/quote', {
                params: { symbols: this.symbol }
            })
                .then(response => {
                    const data = response.data;
                    this.companyInfo = data;
                    console.log(this.companyInfo['quoteResponse']['result'][0]['longName'])
                }).catch(function (error) {
                    console.error(error);
                })
        },
        stockQuote() {
            return axios.get('https://tiny-mountain-5aa6.jamesbrennan21.workers.dev/https://query1.finance.yahoo.com/v8/finance/chart/', {
                params: { symbol: this.symbol, interval: '1mo', diffandsplits: 'false' }
            })
                .then(response => {
                    const data = response.data;
                    const result = Object.entries(data.items).map(([timestamp, item]) => [item.date, item.close]);
                    result.unshift(['date', 'close']);
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
                title: this.symbol + ' Closing Price History',
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
            const infoArray = await this.stockInfo();
            const profileArray = await this.stockProfile();
            return this.drawChart(this.financialData);
        }
    },
})