<template>
  <div>
    <div class="md-layout">
      <div class="md-layout-item">
        <md-field>
          <label for="currentInterval">Intervalo</label>
          <md-select v-model="currentInterval" name="currentInterval" id="currentInterval">
            <md-option
              :value="intervalo"
              v-for="intervalo in intervalos"
              :key="intervalo"
            >{{intervalo}} minutos</md-option>
          </md-select>
        </md-field>
      </div>
      <div class="md-layout-item">
        <md-field>
          <label for="movie">Tamanho da resposta</label>
          <md-select v-model="outputsize" name="outputsize" id="outputsize">
            <md-option value="full">Completo</md-option>
            <md-option value="compact">Compacto</md-option>
          </md-select>
        </md-field>
      </div>
    </div>

    <highcharts class="hc" :options="confChart" ref="chart"></highcharts>
    <div class v-if="jsonUltimaCotacao">
      <p class="info-cotacao">Informações abaixo referente a última medição no horário: {{ formatData }}</p>
    </div>
    <div class="md-layout" v-if="jsonUltimaCotacao">
      <div class="md-layout-item">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Abertura</div>
              <div class="md-subhead">{{jsonUltimaCotacao.value['1. open']}}</div>
            </md-card-header>
            <!-- <md-card-content></md-card-content> -->
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Alta</div>
              <div class="md-subhead">{{jsonUltimaCotacao.value['2. high']}}</div>
            </md-card-header>
            <!-- <md-card-content></md-card-content> -->
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Baixa</div>
              <div class="md-subhead">{{jsonUltimaCotacao.value['3. low']}}</div>
            </md-card-header>

            <!-- <md-card-content></md-card-content> -->
          </md-ripple>
        </md-card>
      </div>
      <div class="md-layout-item">
        <md-card md-with-hover>
          <md-ripple>
            <md-card-header>
              <div class="md-title">Fechamento</div>
              <div class="md-subhead">{{jsonUltimaCotacao.value['4. close']}}</div>
            </md-card-header>
            <!-- <md-card-content></md-card-content> -->
          </md-ripple>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../enviroment.js";

export default {
  props:[
      "confChart",
      "symbol"
  ],
  data() {
    return {
     
      metadados: {},
      jsonCotacoes: [],
      jsonUltimaCotacao: null,
      currentInterval: 1,
      outputsize: "compact",
      intervalos: [1, 5, 15, 30, 60]
    };
  },
  methods: {
    getDadosPorSimbolo(interval, symbol, outputsize) {
      this.axios
        .get(
          `${api.apiUrl}/alphavantage/buscar-por-simbolo/?interval=${interval}&outputsize=${outputsize}&symbol=${symbol}`
        )
        .then(response => {
          console.log(response);
          this.jsonCotacoes = this.managerValue(
            response.data[`Time Series (${interval}min)`]
          );
          this.metadados = response.data["Meta Data"];
          this.confChart.series = [
            {
              data: this.jsonCotacoes.map(json => {
                return {
                  name: json.key + ": " + json.value["4. close"],
                  y: Number(json.value["4. close"]),
                  x: new Date(json.key).getTime()
                };
              })
            }
          ];
          this.jsonUltimaCotacao = this.jsonCotacoes[this.jsonCotacoes.length - 1];
        }).catch(()=>{
            this.$toast.error('Erro ao tentar buscar informação.');
        });
    },
    managerValue(data) {
      let jsonCotacoes = [];
      Object.keys(data).forEach(key => {
        jsonCotacoes.push({
          key: key,
          value: data[key]
        });
      });
      return jsonCotacoes;
    }
  },
  computed: {
    formatData() {
      let horario = new Date(this.jsonUltimaCotacao.key);
      return horario.toLocaleString();
    }
  },
  watch: {
      outputsize(){
        this.getDadosPorSimbolo(this.currentInterval, this.symbol, this.outputsize);
      },
      currentInterval(){
        this.getDadosPorSimbolo(this.currentInterval, this.symbol, this.outputsize);
      },
      symbol(){
        this.getDadosPorSimbolo(this.currentInterval, this.symbol, this.outputsize);
      }
  },
  created() {
    this.getDadosPorSimbolo(this.currentInterval, this.symbol, this.outputsize);
  }
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