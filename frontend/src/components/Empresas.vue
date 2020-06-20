<template>
  <div>
    <div v-if="!currentSymbol || !chartOptions">
      <md-checkbox v-model="buscaManual" class="md-primary">Busca manual</md-checkbox>

      <div class="md-layout" v-if="!buscaManual">
        <div class="md-layout-item">
          <md-field>
            <label for="currentInterval">Intervalo</label>
            <md-select v-model="currentSymbol" name="currentSymbol" id="currentSymbol">
              <md-option :value="simbol" v-for="simbol in simbols" :key="simbol">{{simbol}}</md-option>
            </md-select>
          </md-field>
        </div>

        <div class="md-layout-item md-size-15">
          <md-button
            @click="getDadosEmpresa( currentSymbol, currentSymbol)"
            class="md-raised md-primary"
          >
            <md-icon class="md-primary">remove_red_eye</md-icon>
          </md-button>
        </div>
      </div>

      <div class="md-layout" v-if="buscaManual">
        <div class="md-layout-item">
          <md-field>
            <label>Buscar Empresa</label>
            <md-input v-model="chave"></md-input>
          </md-field>
        </div>
        <div class="md-layout-item md-size-15">
          <md-button @click="getSimbolosPorChave()" class="md-raised md-primary">
            <md-icon class="md-primary">search</md-icon>
          </md-button>
        </div>
      </div>

      <p v-if="empresas && empresas.length == 0">Nenhuma empresa encontrada</p>
      <md-list class="md-triple-line">
        <md-list-item v-for="empresa in empresas" :key="empresa.symbol" style="cursor: pointer">
          <md-avatar>
            <img
              src="https://pbs.twimg.com/profile_images/1230031751659114496/UJtP9hb5_400x400.jpg"
              alt="Business"
            />
          </md-avatar>

          <div class="md-list-item-text">
            <span>{{empresa['2. name']}} ({{empresa['1. symbol']}})</span>
            <span>{{empresa['4. region']}}</span>
            <p>MatchScore: {{empresa['9. matchScore']}}</p>
          </div>
          <div class="md-list-action">
            <md-button
              @click="getDadosEmpresa(empresa['2. name'], empresa['1. symbol'])"
              class="md-icon-button"
              title="Visualizar cotação da empresa"
            >
              <md-icon class="md-primary">remove_red_eye</md-icon>
            </md-button>

            <md-button
              @click="salvarEmpresa(empresa)"
              class="md-icon-button"
              title="Salvar empresa"
            >
              <md-icon class="md-primary">save</md-icon>
            </md-button>
          </div>
          <hr />
        </md-list-item>
      </md-list>
    </div>
    <div v-if="currentSymbol && chartOptions">
      <div class="md-layout">
        <div class="md-layout-item">
          <md-button @click="salvarCotacoes" class="md-raised md-primary">
            <md-icon class="md-primary">sync</md-icon>
            Sincronizar cotações
          </md-button>
        </div>
        <div class="md-layout-item md-size-15">
          <md-button @click="clearField" class="md-raised md-primary">
            <md-icon class="md-primary">keyboard_backspace</md-icon>Voltar
          </md-button>
        </div>
      </div>

      <Simbolo :confChart="chartOptions" :symbol="currentSymbol" />
    </div>
  </div>
</template>



<script>
import api from "../enviroment.js";
import Simbolo from "@/components/Simbolo.vue";

export default {
  components: {
    Simbolo
  },
  data() {
    return {
      buscaManual: false,
      chave: "",
      currentSymbol: "",
      simbols: ["PETR4.SAO", "ITUB4.SAO", "VALE3.SAO"],
      empresas: null,
      chartOptions: null,
      component: null
    };
  },
  methods: {
    getSimbolosPorChave() {
      this.axios
        .get(`${api.apiUrl}/alphavantage/buscar-por-chave/${this.chave}`)
        .then(response => (this.empresas = response.data["bestMatches"]))
        .catch(() => this.$toast.error("Erro ao tentar buscar informação."));
    },

    clearField() {
      this.currentSymbol = "";
      this.chartOptions = null;
    },

    salvarCotacoes(){

    },

    salvarEmpresa(empresa) {
      let empresaFormatada = {};
      Object.keys(empresa).forEach(key => {
        let keyFormatada = key.replace(key.substring(0, 3), "");
        empresaFormatada[keyFormatada] = empresa[key];
      });
      
      this.axios
        .post(`${api.apiUrl}/empresa/cadastrar/`, empresaFormatada)
        .then(() => this.$toast.success("Empresa salva com sucesso."))
        .catch(() => this.$toast.error("Erro ao tentar salvar empresa."));
    },

    getDadosEmpresa(nome, simbolo) {
      this.chartOptions = {
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
          text: nome
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
            data: [1, 2]
          }
        ]
      };
      this.currentSymbol = simbolo;
    }
  }
};
</script>

<style>
</style>