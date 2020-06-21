<template>
  <div>
    
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
            @click="modalShowDialogCotacoes(empresa)"
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

    <md-dialog :md-active.sync="showDialogCotacoes">
      <md-dialog-title>Cotações</md-dialog-title>
      <div class="modal-body">
        <b-table
          id="my-table"
          :items="cotacoes"
          :per-page="perPage"
          :current-page="currentPage"
          small
        >
          <template v-slot:cell(opcoes)="data">
            <md-button
              class="md-secondary md-raised"
              title="editar"
              @click="modalEdicaoCotacao(data.item)"
            >
              <md-icon class="md-primary">edit</md-icon>
            </md-button>
            <md-button
              class="md-secondary md-raised"
              title="deletar"
              @click="deletarCotacao(data.item)"
            >
              <md-icon class="md-primary">delete_forever</md-icon>
            </md-button>
          </template>
        </b-table>

        <div class="overflow-auto">
          <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            aria-controls="my-table"
            size="sm"
          ></b-pagination>
        </div>
      </div>
      <md-dialog-actions>
        <md-button class="md-primary" @click="showDialogCotacoes = false">Fechar</md-button>
      </md-dialog-actions>
    </md-dialog>

    <md-dialog :md-active.sync="showDialogEditCotacao">
      <md-dialog-title>Editar Cotação</md-dialog-title>
      <div class="modal-body">
        <div class="md-layout">
          <div class="md-layout-item">
            <md-field>
              <label>Open</label>
              <md-input v-model="currentCotacao.open"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <label>Close</label>
              <md-input v-model="currentCotacao.close" number></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <label>High</label>
              <md-input v-model="currentCotacao.high"></md-input>
            </md-field>
          </div>
        </div>

        <div class="md-layout">
          <div class="md-layout-item">
            <md-field>
              <label>Low</label>
              <md-input v-model="currentCotacao.low"></md-input>
            </md-field>
          </div>
          <div class="md-layout-item">
            <md-field>
              <label>Volume</label>
              <md-input v-model="currentCotacao.volume" number></md-input>
            </md-field>
          </div>
           <div class="md-layout-item">
            <md-field>
              <label>Date</label>
              <md-input v-model="currentCotacao.date" number></md-input>
            </md-field>
          </div>
        </div>
      </div>
      <md-dialog-actions>
        <md-button class="md-primary" @click="showDialogEditCotacao = false">Fechar</md-button>
        <md-button
          class="md-primary"
          :disabled="isInvalidFormCotacao"
          @click="editarCotacao(currentCotacao)"
        >Salvar</md-button>
      </md-dialog-actions>
    </md-dialog>

    <md-dialog :md-active.sync="showDialog">
      <md-dialog-title>Editar empresa</md-dialog-title>
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
          :disabled="isInvalidFormEmpresa"
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
      cotacoes: [],
      currentPage: 1,
      perPage: 5,
      showDialog: false,
      showDialogCotacoes: false,
      showDialogEditCotacao: false,
      currentEmpresa: {},
      currentCotacao: {},
      chave: "",
      currentSymbol: "",
      simbols: ["", "", "", ""],
      empresas: null,
      chartOptions: null,
      component: null
    };
  },
  methods: {
    modalEdicaoCotacao(cotacao) {
      this.showDialogEditCotacao = true;
      this.currentCotacao = cotacao;
    },

    getEmpresasSalvas() {
      this.axios
        .get(`${api.apiUrl}/empresa/mostrar/`)
        .then(response => (this.empresas = response.data))
        .then(() => (this.showDialog = false))
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

    modalShowDialogCotacoes(empresa) {
      this.currentPage = 1;
      this.showDialogCotacoes = true;
      this.getCotacaoEmpresa(empresa.id);
    },

    deletarEmpresa(empresa) {
      this.axios
        .delete(`${api.apiUrl}/empresa/deletar/${empresa.id}`)
        .then(() => this.$toast.success("Empresa deletada com sucesso."))
        .then(() => this.getEmpresasSalvas())
        .catch(() => this.$toast.error("Erro ao tentar deletar empresa."));
    },

    getCotacaoEmpresa(empresaId) {
      this.axios
        .get(`${api.apiUrl}/cotacao/mostrar/${empresaId}`)
        .then(response => {
          this.cotacoes = response.data;
          this.cotacoes.forEach(element => {
            delete element.empresa;
            element["opcoes"] = "-";
          });
        })
        .catch(() =>
          this.$$toast.error("Erro ao tentar obter cotações da empresa ")
        );
    },

    editarCotacao(cotacao) {
      delete cotacao.opcoes;   
      console.log(cotacao);
         
      this.axios
        .put(`${api.apiUrl}/cotacao/editar/`, cotacao)
        .then(() => this.$toast.success("Cotação editada com sucesso."))
        .then(() => this.showDialogEditCotacao = false)
        .then(() => this.getCotacaoEmpresa(cotacao.empresa_id))
        .catch(() => this.$toast.error("Erro ao tentar editar cotação."));
    },

    deletarCotacao(cotacao) {
      this.axios
        .delete(`${api.apiUrl}/cotacao/deletar/${cotacao.id}`)
        .then(() => this.$toast.success("Cotação deletada com sucesso."))
        .then(() => this.getCotacaoEmpresa(cotacao.empresa_id))
        .catch(() => this.$toast.error("Erro ao tentar deletar cotação."));
    }
  },
  created() {
    this.getEmpresasSalvas();
  },

  computed: {
    rows() {
      return this.cotacoes.length;
    },

    isInvalidFormEmpresa() {
      let temCampoVazio = false;
      Object.keys(this.currentEmpresa).forEach(key => {
        if (!this.currentEmpresa[key]) {
          temCampoVazio = true;
        }
      });
      return temCampoVazio;
    },
     isInvalidFormCotacao() {
      let temCampoVazio = false;
      Object.keys(this.currentCotacao).forEach(key => {
        if (!this.currentCotacao[key]) {
          temCampoVazio = true;
        }
      });
      return temCampoVazio;
    }
  }
};
</script>

<style>
.modal-body {
  overflow: scroll;
}

.table-sm th,
.table-sm td {
  font-size: 10px;
}
</style>