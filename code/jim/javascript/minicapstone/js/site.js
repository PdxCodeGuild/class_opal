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
            return axios.get('https://mboum-finance.p.rapidapi.com/mo/module/', {
                params: { symbol: this.symbol, module: 'asset-profile' },
                headers: {
                    'X-RapidAPI-Key': '0zotPkYey9mshuMn8ZAGIEMstMSyp1fQFA3jsnnIVcgEtc7lxi',
                    'X-RapidAPI-Host': 'mboum-finance.p.rapidapi.com'
                }
            })
                .then(response => {
                    const data = response.data;
                    this.assetProfile = data;
                    console.log(this.assetProfile)
                    console.log(this.assetProfile['longBusinessSummary'])
                }).catch(function (error) {
                    console.error(error);
                })
        },
        stockInfo() {
            return axios.get('https://mboum-finance.p.rapidapi.com/qu/quote', {
                params: { symbol: this.symbol },
                headers: {
                    'X-RapidAPI-Key': '0zotPkYey9mshuMn8ZAGIEMstMSyp1fQFA3jsnnIVcgEtc7lxi',
                    'X-RapidAPI-Host': 'mboum-finance.p.rapidapi.com'
                }
            })
                .then(response => {
                    const data = response.data;
                    this.companyInfo = data;
                }).catch(function (error) {
                    console.error(error);
                })
        },
        stockQuote() {
            return axios.get('https://mboum-finance.p.rapidapi.com/hi/history', {
                params: { symbol: this.symbol, interval: '1mo', diffandsplits: 'false' },
                headers: {
                    'X-RapidAPI-Key': '0zotPkYey9mshuMn8ZAGIEMstMSyp1fQFA3jsnnIVcgEtc7lxi',
                    'X-RapidAPI-Host': 'mboum-finance.p.rapidapi.com'
                }
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