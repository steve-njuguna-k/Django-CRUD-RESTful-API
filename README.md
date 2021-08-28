# Django-CRUD-RESTful-API
A Django RESTful API for performing CRUD operations on transaction details stored in a PostgreSQL DB

![](https://github.com/steve-njuguna-k/Django-CRUD-RESTful-API/blob/master/src/static/img/Screenshot-1.PNG)

# Functionalities

- You Can View All Transactions

![](https://github.com/steve-njuguna-k/Django-CRUD-RESTful-API/blob/master/src/static/img/Screenshot-2.PNG)

- You Can View Particular Transaction Details

![](https://github.com/steve-njuguna-k/Django-CRUD-RESTful-API/blob/master/src/static/img/Screenshot-3.PNG)

- You Can Add A New Transaction

![](https://github.com/steve-njuguna-k/Django-CRUD-RESTful-API/blob/master/src/static/img/Screenshot-4.PNG)

- You Can Delete A Particular Transaction

![](https://github.com/steve-njuguna-k/Django-CRUD-RESTful-API/blob/master/src/static/img/Screenshot-5.PNG)

# Project Setup Instructions
1) Git clone the repository 
```
https://github.com/steve-njuguna-k/Django-CRUD-RESTful-API.git
```
2. Go To Project Directory
```
cd Django-CRUD-RESTful-API
```
3. Create Virtual Environment
```
virtualenv env
```
4. Active Virtual Environment
```
env\scripts\activate
```
5. Install Requirements File
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate Database
```
py manage.py migrate
```
8. Run Project
```
py manage.py runserver
```
9. Head over to URL
```
http://127.0.0.1:8000/api/v1
```

© 2021 Steve Njuguna

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
