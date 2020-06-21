<template>
  <div>
    <Simbolo :confChart= "chartOptions" :symbol="'^BVSP'" />
  </div>
</template>

<script>
import Simbolo from "@/components/Simbolo.vue";


export default {
  components:{
    Simbolo
  },
  data() {
    return {
      chartOptions: {
        plotOptions: {
          line: {
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
          text: "IBOVESPA"
        },
        xAxis: {
          type: "datetime"
        },
        tooltip: {
          xDateFormat: "%d/%m/%Y %H:%M:%S"
        },

        series: [
          {
            name: "",
            data: []
          }
        ]
      },
      metadados: {},
      jsonCotacoes: [],
      jsonUltimaCotacao: null,
      currentInterval: 1,
      outputsize: "compact",
      intervalos: [1, 5, 15, 30, 60]
    };
  },
 
};
</script>

<style>
.info-cotacao {
  text-align: center;
  font-style: italic;
  font-weight: 200;
}

.md-layout-item {
    padding: 10px;
}


</style>