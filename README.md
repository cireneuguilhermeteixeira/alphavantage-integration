# Desafio PontoTel


Este Projeto corresponde à um desafio proposto pela empresa [PontoTel](https://www.pontotel.com.br/) para vaga de desenvolvedor VueJs e Python. O projeto consiste numa aplicação cliente(VueJs) servidor(Python com Flask) com integração à API da [Alpha Vantage](https://www.alphavantage.co/). Na aplicação é possível consultar os dados da Bovespa do dia, informando por parâmetro alguns parâmetros na url tais como o tamanho da saída dos dados, intervalo entre cotações. Na mesma url é possível informar outros símbolos, obtendo dados das empresas monitoradas pelo Alpha Vantage e com isso o seu valor também. 
Além disso, no sistema é possível fazer um CRUD de usuários, empresas e cotações, de maneira bem intuitiva e dinâmica, obtendo os os valores da API e salvando em um banco de dados relacional. 

---

# Documentação API Python FLASK

Para ter acesso à documentação da API e saber quais os endpoints existentes e como é o comportamento de cada um deles acesse o [Link do POSTMAN aqui](https://documenter.getpostman.com/view/11802905/SzzoZFJf).

---

# Estrutura do projeto

O projeto está dividido em uma arquitetura cliente-servidor. O lado do servidor foi feito em Python 3.7 e consome, assíncronamente, as API's fornecidas pela [Alpha Vantage](https://www.alphavantage.co/) para fornecer os dados da aplicação.
O lado do cliente foi desenvolvido com Angular 7 e componentes do Material Design. Existe também uma camada de banco de dados desenvolvida com PostgreSQL para persistência de dados sobre empresas e suas cotações recebidas durante a execução da aplicação.


---

## Tecnologias utilizadas

Para a aplicação em Python foram usadas, principalmente, as dependências:

+ [Python 3.6](https://www.python.org/)
  - Uma das versões mais recentes desta linguagem.

+ [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - Um framework web para Python baseado na biblioteca WSGI Werkzeug e na biblioteca de Jinja2.

+ [SQLAlchemy](https://www.sqlalchemy.org/)
  - SQLAlchemy é uma biblioteca de mapeamento objeto-relacional SQL em código aberto desenvolvido para a linguagem de programação Python.

+ [Marshmallow](https://marshmallow.readthedocs.io/en/3.0/api_reference.html)
  - Biblioteca utilizada para validação de inputs e desserialização de dados.

+ [Pytest](https://docs.pytest.org/en/latest/)
  - Framework para escrever testes em Python com o auxílio da biblioteca [Flask Testing](https://pythonhosted.org/Flask-Testing/).

+ [Requests](https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html)
  - Biblioteca para fazer requisições HTTP para Python nos testes e na integração com Alphavantage.

---

Para a aplicação em Vue foram usadas, principalmente, as seguintes ferramentas:
+ [Vue.js ](https://vuejs.org/v2/guide/)
  - Vue.js é um framework JavaScript de código-aberto, focado no desenvolvimento de interfaces de usuário e aplicativos de página única.

+ [Vue-CLI](https://cli.vuejs.org/)
  - Ferramenta de linha de comando para gerenciamento de projetos Vue.

+ [NPM](https://www.npmjs.com/)
  - Gerenciador de pacotes NodeJs

+ [Vue Material](https://vuematerial.io/) e [BootstrapVue](https://bootstrap-vue.org/)
  - Biblioteca com implementações estilos e componentes já prontos.

+ [VueX](https://vuex.vuejs.org/)
  - Vuex é um padrão de gerenciamento de estado + biblioteca para aplicativos Vue.js. Também é útil como um armazenamento centralizado para todos os componentes em um aplicativo, com regras que garantem que o estado possa ser alterado apenas de maneira previsível.


+ [HighchartsVue](https://www.highcharts.com/blog/tutorials/highcharts-vue-wrapper/)
  - Componente para exibição de dados em formato gráfico.

---

Para a camada de banco de dados foi utilizada a seguinte dependência:
+ [PostgreSQL 12](https://www.postgresql.org/)
  - SGBD relacional em uma de suas versões mais atuais.
---

## Configuração do ambiente

O projeto foi configurado para execução com Docker Compose. Contudo, é possível fazer a execução manualmente.

###  Configuração da parte FrontEnd

+ Intalar o node e npm 
  - Acesse o [link](https://dicasdejavascript.com.br/instalacao-do-nodejs-e-npm-no-windows-passo-a-passo/#:~:text=Instala%C3%A7%C3%A3o%20do%20NodeJS%20e%20npm%20no%20Windows%20(Passo%20a%20passo!),-Por%20Gustavo%20Furtado&text=Para%20instalar%20o%20nodejs%20e,que%20%C3%A9%20a%20%C3%BAltima%20vers%C3%A3o.) e certifique-se de está instalando as versões mais recentes. 
   
+ Instalar o Vue-CLI na sua máquina e rodar o frontend.

    ```
      npm install -g @vue/cli

      npm install -g @vue/cli/service-global

    ```
    Após clonar o projeto entre no diretório do frontend e execute o comando:
    
    ```
      npm install

      npm run serve

    ```
    Se tudo ocorrer bem o projeto estará rodando localmente na porta 8080.

---
###  Configuração da parte Backend

 + Certifique de ter instalado no seu ambiente as seguintes dependências:
 
  - [Python 3.6 ou superior](https://www.python.org/downloads/)
  - [Postgres 12](https://www.postgresql.org/about/news/1976/)
  - [pip3](https://www.educative.io/edpresso/installing-pip3-in-ubuntu)

+ Após instaladas, entre no diretório do backend e prossiga com os passos:
  - Instale as biliotecas utilizadas pelo projeto.
    ```
      pip3 install -r requirements.txt

    ```
  - Crie um banco de dados com um usuário e configure o ambiente para ter acesso ao banco.
    ```
      sudo -i -u postgres
      psql
      
    ```
    Agora crie o banco com o usuário e suas permissões.

    ```
      create database ptl;
      create user ponto_tel_user with encrypted password 'pontotel';
      grant all privileges on database ptl to ponto_tel_user;
      \q
      exit
    
    ```
    Logo depois, exporte as configurações de banco para se torarem acessíveis pelo Python.

    ```
      export POSTGRES_USER="ponto_tel_user"
      export POSTGRES_PW="pontotel"
      export POSTGRES_URL="127.0.0.1:5432"
      export POSTGRES_DB="ptl"

    ```
    Agora exporte as configurações de aplicação do ambiente e migration.

    ```
      export FLASK_APP=app
      export FLASK_ENV=Development
      export FLASK_DEBUG=True
    ```

      Logo depois, execute os seguintes comandos para efetuar as migrations.

    ```
      flask db init
      flask db migrate
      flask db upgrade

    ```
    Logo depois pode executar a aplicação:

    ```
      python3 app.py

    ```
---

## Execução de Testes

Execute o comando pelo terminal na raiz do projeto:
```
  py.test backend/tests_api_routes.py

```

---

#### Alguns Screenshots da aplicação

![Tela de exibição do Ibovespa](https://i.imgur.com/ou0KwtF.png)
  *Exibição do Ibovespa do dia*

---  
  
![Tela de exibição de empresas](https://i.imgur.com/EaPjCYb.png)
  *Lista de empresas buscadas por chaves.*
  


---  
  
![Tela de exibição dos usuários](https://i.imgur.com/gWja6go.png)
  *Lista de empresas buscadas por chaves.*
  

---  
  
![Tela de exibição de cotações](https://i.imgur.com/hulc6Xp.png)
  *Lista cotações de respectiva empresa.*
  



---

## Melhorias

* Melhorar as respostas do backend para serem reproduzidas de maneira mais clara para usuário caso ocorra algum erro.

* Configurar ambiente para rodar com Docker.

* Melhorar a interface do usuário, tais como animações de loads para dá um melhor feedback ao usuário em requisições que demandarem mais tempo.
