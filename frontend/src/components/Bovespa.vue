<template>
    <div>
        <p>Bovespa</p>         
        <highcharts class="hc" :options="chartOptions" ref="chart"></highcharts>
    </div>
</template>

<script>


export default {
    data(){
        return {
            chartOptions: {

                plotOptions: {
                    line:{
                    color: "#448aff"
                    }
                },
                time: {
                    useUTC: true,
                    timezoneOffset: 180
                },
                rangeSelector: {
                    enabled: true
                },
                title: {
                    text: 'IBOVESPA'
                },
                xAxis: {
                    type: 'datetime'
                },
                tooltip: {
                    xDateFormat: '%d/%m/%Y %H:%M:%S'
                },
    

                series: [
                    {   
                        name: 'BVSP BOVESPA IND',
                        data: [9,9,7,5,0,2,4,8,4]
                    }
                ]
            },
        }
    },
    methods: {
        getBovespa(){
            this.axios.get(api).then((response) => {
                console.log(response.data)
            })
        }
    },
}
</script>

<style>

</style>