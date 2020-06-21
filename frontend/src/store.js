
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        cotacoes: null
    },
    mutations:{
        changeCotacoes(state, payload){
            state.cotacoes = payload
        }
    }
});