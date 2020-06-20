<template>
  <div>
    <h2>Usuários</h2>
    <div class="md-layout">
      <md-button class="md-primary md-raised" @click="initModal(null)">
        <md-icon class="md-primary">add</md-icon>Novo usuário
      </md-button>
    </div>

    <p class="mt-3">Página atual: {{ currentPage }}</p>

    <b-table id="my-table" :items="usuarios" :per-page="perPage" :current-page="currentPage" small>
      <template v-slot:cell(opcoes)="data">
        <md-button class="md-secondary md-raised" title="editar" @click="initModal(data.item)">
          <md-icon class="md-primary">edit</md-icon>
        </md-button>
        <md-button
          class="md-secondary md-raised"
          title="deletar"
          @click="deletarUsuario(data.item)"
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

    <md-dialog :md-active.sync="showDialog">
      <md-dialog-title>Salvar novo usuário</md-dialog-title>
      <div class="md-layout">
        <div class="md-layout-item">
          <md-field>
            <label>Nome</label>
            <md-input v-model="nome"></md-input>
          </md-field>
        </div>
        <div class="md-layout-item">
          <md-field>
            <label>Idade</label>
            <md-input v-model="idade" number></md-input>
          </md-field>
        </div>
        <div class="md-layout-item">
          <md-field>
            <label>Profissão</label>
            <md-input v-model="profissao"></md-input>
          </md-field>
        </div>
      </div>

      <md-dialog-actions>
        <md-button class="md-primary" @click="showDialog = false">Fechar</md-button>
        <md-button class="md-primary" :disabled="isInvalidForm" @click="salvarOuAtualizar()">Salvar</md-button>
      </md-dialog-actions>
    </md-dialog>
  </div>
</template>

<script>
import api from "../enviroment.js";

export default {
  components: {},
  data() {
    return {
      showDialog: false,
      id: null,
      nome: "",
      idade: null,
      profissao: "",
      usuarios: [],
      perPage: 5,
      currentPage: 1
    };
  },
  methods: {
    initModal(usuario) {
      console.log(usuario);

      if (usuario) {
        this.id = usuario.id;
        this.nome = usuario.nome;
        this.idade = usuario.idade;
        this.profissao = usuario.profissao;
      } else {
        this.id = null;
        this.nome = "";
        this.idade = null;
        this.profissao = "";
      }
      this.showDialog = true;
    },
    salvarOuAtualizar() {
      if (!this.id) {
        let usuario = {
          nome: this.nome,
          idade: this.idade,
          profissao: this.profissao
        };
        this.axios
          .post(`${api.apiUrl}/usuario/cadastrar/`, usuario)
          .then(() => {
            this.getUsuarios();
            this.showDialog = false;
          })
          .then(()=> this.$toast.success("Usuário criado com sucesso."))
          .catch(() => this.$toast.error("Erro ao tentar criar usuário."));

      } else {

        let usuario = {
          id: this.id,
          nome: this.nome,
          idade: this.idade,
          profissao: this.profissao
        };
        this.axios
          .put(`${api.apiUrl}/usuario/editar/`, usuario)
          .then(() => {
            this.getUsuarios();
            this.showDialog = false;
          })
          .then(()=> this.$toast.success("Usuário Alterado com sucesso."))
          .catch(() => {
            this.$toast.error("Erro ao tentar alterar usuário");
          });
      }
    },

    deletarUsuario(usuario) {
      this.axios
        .delete(`${api.apiUrl}/usuario/deletar/${usuario.id}`)
        .then(() => {
          this.getUsuarios();
        })
        .then(() => this.$toast.success("Usuário deletado com sucesso."))
        .catch(() => {
          this.$toast.error("Erro ao tentar deletar usuário");
        });
    },

    getUsuarios() {
      this.axios
        .get(`${api.apiUrl}/usuario/mostrar/`)
        .then(response => {
          this.usuarios = response.data.sort((obj1, obj2) => {
            return obj1.id - obj2.id;
          });
          this.usuarios.forEach(element => {
            element.opcoes = "-";
          });
        })
        .catch(() => {
          this.$toast.error("Erro ao tentar listar usuários.");
        });
    }
  },

  created() {
    this.getUsuarios();
  },
  computed: {
    isInvalidForm() {
      return !this.nome || !Number(this.idade) || !this.profissao;
    },
    rows() {
      return this.usuarios.length;
    }
  }
};
</script>
  
<style scoped>
*,
*::before,
*::after {
  box-sizing: border-box;
  text-align: center;
}
.table th, .table td {
  font-size: 12px;
}
</style>