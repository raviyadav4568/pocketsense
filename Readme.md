# PocketSense

PocketSense is a set of web application api's to create and split expenses for college going students.

# Instructions for successfully running the application on local machine

1) Please navigate to the project directory and use the below command to install the project dependencies 

```bash
pipenv install
pipenv install --dev
```
2) Please configure the database the configuration in setting.py file

3) Run the migrations using the below command
   python manage.py migrate

4) Once the tables are visible in the db, we can start the server using below command
   python manage.py runserver

5) Now the project should be up and running for using the api's

# Api's

Below are the api's that are provided for creating and managing user, expenses, payments and concerns

1) For creating user

```bash
localhost:8000/api/auth/user
```

2) Creating token for using api's
```bash
localhost:8000/api/auth/jwt/create
```
3)For navigating the api's
```bash
   localhost:8000/api/pocketsense/expenses
   localhost:8000/api/pocketsense/payments
   localhost:8000/api/pocketsense/concerns
   localhost:8000/api/pocketsense/profiles
```
# Swagger documentation for the project can be found at
```bash
 localhost:8000/swagger/
```
Swagger documentation has all the api's and models mentioned, please refer the documentation before using the api's.

## License

[MIT](https://choosealicense.com/licenses/mit/)