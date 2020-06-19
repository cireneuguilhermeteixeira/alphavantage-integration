<template>
  <div id="app">
    <Header/>
    <main>
      <Body/>
    </main>
    <Footer/>

  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import Body from '@/components/Body.vue';


export default {
  name: 'App',
  components: {
    Header,
    Footer,
    Body,
  }
}
</script>

<style>

  *{
    box-sizing: border-box;
    
  }

  body, ul, li, h1, h2, p{
    padding: 0;
    margin: 0;
  }

  ul{
    list-style: none;
  }
  
  body{
     font-family: Arial, Helvetica, sans-serif;
     color:#345;
  }

  a{
    color: #345;
    list-style: none;
    text-decoration: none;
  }

  img{
    max-width: 100%;
    display: block;
  }

  .btn{
    display: block;
    padding: 10px 30px;
    background: #448aff;
    border-radius: 4px;
    color: #ffff;
    text-align: center;
    font-size: 1rem;
    box-shadow: 0 4px 8px rgba(30, 60, 90, 0.2);
    transition: all 0.3s;
    border: none;
    font-family: Arial, Helvetica, sans-serif;
    cursor: pointer;
  }

  .btn:hover{
    background: #448aff;
    transform: scale(1.1);
  }

  #app{
    background: rgb(56, 56, 58);
    display: flex;
    min-height: 100vh;
    flex-direction: column;

  }

  main{
    flex: 1;
  }


</style>
