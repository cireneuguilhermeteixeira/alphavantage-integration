<template>
  <div class="page-container">
    <md-app>
      <md-app-toolbar class="md-primary">
        <span class="md-title">{{currentPage}}</span>
      </md-app-toolbar>

      <md-app-drawer md-permanent="full">
        
        <md-list>
          <md-list-item v-for="pagina in paginas" :key="pagina.id" @click="changePage(pagina)">
            <md-icon>{{pagina.icon}}</md-icon>
            <span class="md-list-item-text">{{pagina.title}}</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <component :is="currentComponent"></component>
      </md-app-content>
    </md-app>
  </div>
</template>

<script>

import Bovespa from './Bovespa.vue';
import Empresas from './Empresas.vue';
import Usuarios from './Usuarios.vue';


export default {
    name:"Body",
    components:{
        Bovespa,
        Empresas,
        Usuarios
    },
    data(){
        return {
            paginas: [
                {
                    id:1,
                    icon: 'attach_money',
                    title: 'Bovespa do dia',
                    componentName: 'Bovespa'
                },
                {
                    id:2,
                    icon: 'send',
                    title: 'Buscar empresa',
                    componentName: 'Empresas'
                },
                {
                    id:3,
                    icon: 'save_alt',
                    title: 'Empresas Salvas',
                    componentName: 'Empresas'
                },
                {
                    id:4,
                    icon: 'supervisor_account',
                    title: 'Usuarios',
                    componentName: 'Usuarios'
                }
            ],
            currentPage: 'Bovespa do dia',
            currentComponent: 'Bovespa',

        }
    },
    methods: {
        changePage(page){
            this.currentPage = page.title;
            this.currentComponent = page.componentName;
        }
    },

}
</script>

<style scoped>
   
   .md-app .md-content.md-theme-default{
       min-height: 500px;
   }

    .md-drawer.md-theme-default {
        width: 250px;
        background: rgb(56, 56, 58);
        
    }

    .md-list.md-theme-default{
        background: rgb(56, 56, 58);
    }

    .md-transparent{
        color: #ffffff;
    }

    .md-list-item-text{
        color: #ffffff;
    }

    .md-list-item-text:hover{
        transform: scale(1.1);
    }


    .md-icon.md-theme-default.md-icon-font {
        color: #ffffff;

    }


    .md-list-item-text{
        cursor: pointer;
    }

</style>