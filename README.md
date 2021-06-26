 ## MyWallet
 
Final project of a course made with Django. In this project, the challenge was to create something similar to a portfolio of operations. Where the user enters his trades and can view the summary of his stock portfolio and trade history.


## Technologies 
 
Technologies used in the project.  
 
* Python version  3.8.5
* Django version 3.1.4
* [Jinja Format](https://jinja.palletsprojects.com/en/2.11.x/templates/)
* Bootstrap 4
* Postgres Alpine (Imagem Docker) 13.2
* Docker 20.10.4
 
 
## Services Used
 
* Github
 
## Pip
 You will need some libs to run the project. Applications will be on file [requeriments.txt](https://github.com/Jackie098/django-example/blob/master/requeriments.txt).

 To install the requirements, just run in the terminal:
 > $ pip install -r requeriments.txt
  
  ATTENTION: Consider being in the same folder as 'requirements.txt'.

  If you use virtual environment (recommended):  
   1. Install the virtual environment:  
   > $python3 -m venv myvenv
   2. Start the environment. Be careful to put the correct path to the file:  
   > $ source ./myvenv/bin/activate
   3. After cloning the repository, install the dependencies with the file 'requirements.txt':  
   > $ pip install -r requirements.txt
 
## Starting
 
* Consider the previous steps in the **PIP** session.
* Your database must be synchronized. To do this, create a **Postgree** database called *homebroke*, make sure it is on port *5432* and configure the rest of the information according to your environment.
* Once the database is connected, enter the command in the terminal:  
> $ python manage.py migrate

  You must be at the same directory level as the *manage.py* file. If there is a problem, try running these two commands below in the terminal:  
**1º**
> $ python manage.py makemigrations  

**2º**
> $ python manage.py migrate

* Now with the database connected and all the tables created, start the server:
> $ python manage.py runserver

If you are using it, make sure you have the virtual environment running and in the same folder as the **manage.py** file.

## How to use
 
 Upon accessing the server link, you will see the *HOME* page for unlogged in users.  
 ![Home para usuários não logados](https://github.com/Jackie098/my-wallet/blob/master/images-readme/01.home_without_login.png)

 Create an account in the respective session. Enter user and investor data.  
 ![Criar conta](https://github.com/Jackie098/my-wallet/blob/master/images-readme/02.new_account_form.png)

 Then, *LOGIN* with the registered user data.  
 ![Login de usuário](https://github.com/Jackie098/my-wallet/blob/master/images-readme/03.login_view.png)

 Now we can view *HOME* for logged in users. Note the new options released in *nav-bar* as much as the summary of operations and investor information.  
 ![Home para usuários logados](https://github.com/Jackie098/my-wallet/blob/master/images-readme/04.home_logged.png)

 With the user logged in, register your operations and specify whether it is a purchase or sale.  
 ![Registro de Operações](https://github.com/Jackie098/my-wallet/blob/master/images-readme/05.new_operation.png)

 You can also view your operations (their history).  
 ![Histórico de Operações](https://github.com/Jackie098/my-wallet/blob/master/images-readme/06.history_operations.png)

 
## Updates
 
  - Suggestions:
     - in HOME: You can insert graphics as a dashoard.
     - HOME: Format *average price* data.
     - HOME: The calculations were made with an erroneous logic. For example: In *Summary of Operations*, all instances per action are added, but there is a contradiction here as some actions have *bought* and *sold* operations, there is no added value bought with the same sold.
     - Add more information for *investor* and/or *user*
     - Add functionality to change and delete operations.
     - Create a "public" page to rank investors by number of operations, higher amounts invested, etc.
 
 
## Links
 
  - Repository: https://github.com/Jackie098/my-wallet
    - In case of doubts or suggestions, feel free to get in touch and/or request **pull requests**. 
 
 
## Creator
 
* **Carlos Augusto M**: @Jackie098 (https://github.com/Jackie098)
