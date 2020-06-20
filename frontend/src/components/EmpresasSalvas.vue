<template>
  <div>
    <div class="md-layout">
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
          <span>{{empresa.name}} ({{empresa.symbol}})</span>
          <span>{{empresa.region}}</span>
          <p>MatchScore: {{empresa.matchScore}}</p>
        </div>

        <div class="md-list-action">
          <md-button
            @click="getCotacaoEmpresa(empresa)"
            class="md-icon-button"
            title="Visualizar cotação da empresa"
          >
            <md-icon class="md-primary">remove_red_eye</md-icon>
          </md-button>

          <md-button
            @click="modalEdicaoEmpresa(empresa)"
            class="md-icon-button"
            title="Editar empresa"
          >
            <md-icon class="md-primary">edit</md-icon>
          </md-button>

          <md-button
            @click="deletarEmpresa(empresa)"
            class="md-icon-button"
            title="Deletar empresa"
          >
            <md-icon class="md-primary">delete_forever</md-icon>
          </md-button>
        </div>
        <hr />
      </md-list-item>
    </md-list>

    <md-dialog :md-active.sync="showDialog">
      <md-dialog-title>Salvar novo usuário</md-dialog-title>
      <div class="modal-body">
        <div class="md-layout">
          <div class="md-layout-item">
            <md-field>
              <label>Symbol</label>
              <md-input v-model="currentEmpresa.symbol"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <label>Name</label>
              <md-input v-model="currentEmpresa.name" number></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <label>Type</label>
              <md-input v-model="currentEmpresa.type"></md-input>
            </md-field>
          </div>
        </div>

        <div class="md-layout">
          <div class="md-layout-item">
            <md-field>
              <label>Region</label>
              <md-input v-model="currentEmpresa.region"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <label>Market Open</label>
              <md-input v-model="currentEmpresa.marketOpen" number></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <label>Market Close</label>
              <md-input v-model="currentEmpresa.marketClose"></md-input>
            </md-field>
          </div>
        </div>

        <div class="md-layout">
          <div class="md-layout-item">
            <md-field>
              <label>Timezone</label>
              <md-input v-model="currentEmpresa.timezone"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <label>Currency</label>
              <md-input v-model="currentEmpresa.currency" number></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <label>Match Score</label>
              <md-input v-model="currentEmpresa.matchScore"></md-input>
            </md-field>
          </div>
        </div>
      </div>
      <md-dialog-actions>
        <md-button class="md-primary" @click="showDialog = false">Fechar</md-button>
        <md-button
          class="md-primary"
          :disabled="isInvalidForm"
          @click="editarDadosEmpresa(currentEmpresa)"
        >Salvar</md-button>
      </md-dialog-actions>
    </md-dialog>
  </div>
</template>



<script>
import api from "../enviroment.js";

export default {
  data() {
    return {
      showDialog: false,
      currentEmpresa: {},
      chave: "",
      currentSymbol: "",
      simbols: ["", "", "", ""],
      empresas: null,
      cotacao: null,
      chartOptions: null,
      component: null
    };
  },
  methods: {
    getEmpresasSalvas() {
      this.axios
        .get(`${api.apiUrl}/empresa/mostrar/`)
        .then(response => (this.empresas = response.data))
        .then(()=> this.showDialog = false)
        .catch(() =>
          this.$toast.error("Erro ao tentar listar empresas salvas.")
        );
    },
    editarDadosEmpresa(empresa) {
      this.axios
        .put(`${api.apiUrl}/empresa/editar/`, empresa)
        .then(() => this.$toast.success("Empresa editada com sucesso."))
        .then(() => this.getEmpresasSalvas())
        .catch(() => this.$toast.error("Erro ao tentar editar empresa."));
    },

    modalEdicaoEmpresa(empresa) {
      this.showDialog = true;
      delete empresa.cotacoes;
      this.currentEmpresa = empresa;
    },

    deletarEmpresa(empresa) {
      this.axios
        .delete(`${api.apiUrl}/empresa/deletar/${empresa.id}`)
        .then(() => this.$toast.success("Empresa deletada com sucesso."))
        .then(() => this.getEmpresasSalvas())
        .catch(() => this.$toast.error("Erro ao tentar deletar empresa."));
    },

    getCotacaoEmpresa(empresa) {
      this.axios
        .get(`${api.apiUrl}/cotacao/mostrar/${empresa.id}`)
        .then(response => (this.cotacao = response.data))
        .catch(() =>
          this.$$toast.error(
            "Erro ao tentar obter cotações da empresa " + empresa.name
          )
        );
    },

    editarCotacao(cotacao) {
      this.axios
        .put(`${api.apiUrl}/cotacao/editar/`, cotacao)
        .then(() => this.$toast.success("Cotação editada com sucesso."))
        .then(() => this.getEmpresasSalvas())
        .catch(() => this.$toast.error("Erro ao tentar editar cotação."));
    },

    deletarCotacao(cotacao) {
      this.axios
        .delete(`${api.apiUrl}/cotacao/deletar/${cotacao.id}`)
        .then(() => this.$toast.success("Cotação deletada com sucesso."))
        .then(() => this.getEmpresasSalvas())
        .catch(() => this.$toast.error("Erro ao tentar deletar cotação."));
    }
  },
  created() {
    this.getEmpresasSalvas();
  },
  computed: {
    isInvalidForm() {
      let temCampoVazio = false;
      Object.keys(this.currentEmpresa).forEach(key=>{
         if(!this.currentEmpresa[key]){
           temCampoVazio = true;
         }
      })
      return temCampoVazio;
    }
  }
};
</script>

<style>
.modal-body {
  overflow: scroll;
}
</style>