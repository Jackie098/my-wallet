 ## MyWallet
 
Projeto final de uma disciplina feita com Django. Neste projeto o desafio foi criar algo parecido com uma carteira de operações. Onde o usuário insere suas operações e pode visualizar o resumo da sua carteira de ações e histórico de operações.


## Tecnologias 
 
Tecnologias utilizadas no projeto.
 
* Python version  3.8.5
* Django version 3.1.4
* [Jinja Format](https://jinja.palletsprojects.com/en/2.11.x/templates/)
* Bootstrap 4
* Postgres Alpine (Imagem Docker) 13.2
* Docker 20.10.4
 
 
## Services Used
 
* Github
 
## Pip
 Você vai precisar de algumas libs para rodar o projeto. Os requerimentos estarão no arquivo [requeriments.txt](https://github.com/Jackie098/django-example/blob/master/requeriments.txt).

 Para instalar os requerimentos, basta rodar no terminal:
 > $ pip install -r requeriments.txt
  
  ATENÇÃO: Considere estar na mesma pasta do 'requeriments.txt'.

  Se você usa ambiente virtual (o recomendado):
  1. Instale o ambiente virtual:
  > $ python3 -m venv myvenv
  2. Inicie o ambiente. Se atente em colocar o caminho correto do arquivo:
  > $ source ./myvenv/bin/activate
  3. Depois de clonar o repositório, instale as dependências com o arquivo 'requeriments.txt':
  > $ pip install -r requeriments.txt
 
## Começando
 
* Considere os passos anteriores na sessão **PIP**.
* O seu banco de dados deve estar sincronizado. Para isso, crie um banco de dados **Postgree** chamado *homebroke*, atente-se para estar na porta *5432* e configure o restante das informações de acordo com o seu ambiente.
* Assim que o banco de dados estiver conectado, insira o comando no terminal:
> $ python manage.py migrate

Você deve estar no mesmo nível do diretório do arquivo *manage.py*. Se houver algum problema, tente executar estes dois comandos a seguir no terminal:
**1º**
> $ python manage.py makemigrations

**2º**
> $ python manage.py migrate
* Agora com o banco conectado e todas as tabelas criadas, inicie o servidor:
> $ python manage.py runserver

Se estiver utilizando, certifique-se de estar com o ambiente virtual rodando e na mesma pasta do arquivo **manage.py**.

## Como usar
 
 Ao acessar o link do servidor, você verá a página *HOME* para usuários não logados.
 ![Home para usuários não logados](https://github.com/Jackie098/my-wallet/blob/master/images-readme/01.home_without_login.png)

 Crie uma conta na respectiva sessão. Insira dados relativos a usuário e investidor.
 ![Criar conta](https://github.com/Jackie098/my-wallet/blob/master/images-readme/02.new_account_form.png)

 Em seguida, faça *LOGIN* com os dados de usuário cadastrados.
 ![Login de usuário](https://github.com/Jackie098/my-wallet/blob/master/images-readme/03.login_view.png)

 Agora podemos visualizar a *HOME* para usuários logados. Observe as novas opções liberadas no *nav-bar* tanto quanto
 o resumo das operações e informação do investidor. ![Home para usuários logados](https://github.com/Jackie098/my-wallet/blob/master/images-readme/04.home_logged.png)

 Com o usuário logado, registre suas operações e especifique se é de compra ou venda. ![Registro de Operações](https://github.com/Jackie098/my-wallet/blob/master/images-readme/05.new_operation.png)

 Você também pode visualizar suas operações (o histórico delas). ![Histórico de Operações](https://github.com/Jackie098/my-wallet/blob/master/images-readme/06.history_operations.png)

 
## Atualizações
 
  - Sugestões: 
    - na HOME: Pode-se inserir gráficos como um dashoard.
    - HOME: Formatar os dados de *average price*.
    - HOME: Os calculos foram feito com uma lógica errônea. Por exemplo: No *Sumary of Operations*, soma-se todas as instâncias por ação, mas a uma contradição aqui pois algumas ações tem operação de *comprado* e *vendido*, não se soma um valor comprado com o mesmo vendido.
    - Agregar mais informações para o *investidor* e/ou *usuário*
    - Adicionar as funcionalidades para alterar e apagar operações.
    - Criar uma página "pública" para rankear investidores seja por quantidade de operações, maiores valores investidos, etc.
 
 
## Links
 
  - Repositório: https://github.com/Jackie098/my-wallet
    - Em caso de dúvidas ou sugestões, sinta-se livre para entrar em contato e/ou solicitar **pull requests**.
 
 
## Autor
 
* **Carlos Augusto M**: @Jackie098 (https://github.com/Jackie098)