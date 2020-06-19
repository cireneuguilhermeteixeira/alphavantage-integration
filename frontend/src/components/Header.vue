<template>
    <header>
        <nav>
            <div class="int-alpha">
                Integração Alphavantage
            </div>

            <div  class="logo">
                <img src="https://s3.amazonaws.com/sample-login/companies/avatars/000/002/030/original/logo.png?1483985205" alt="PontoTel" srcset="">
            </div>
        </nav>
    </header>
</template>

<script>
export default {
    name: "Header",

}
</script>

<style scoped>

    *{
        background: #ffffff;;

    }

    nav{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 15px 20px;
        box-shadow: 0 2px 4px rgba(30, 60, 90, 0.1);

    }

    .logo{
        padding: 0px 0;
    }

    .logo img{
        width: 120px;
    }

    .int-alpha{
        font-size: 20px;
    }
</style>