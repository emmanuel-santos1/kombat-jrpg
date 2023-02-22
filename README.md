# Kombat-JRPG-Fastapi
App using fastapi

## Technology Stack:
* FastAPI
* Uvicorn (server)
* Pytest
* Sqlalchemy
* Postgres
* Docker


## I love to use virtualenvwrapper
If you want to use virtualenvwrapper follow the <a href="https://virtualenvwrapper.readthedocs.io/en/latest/install.html" target="_blank">installation guide</a>
Otherwise, modify the steps to make use of the virtual environment with the tool of your choice
You can also skip these steps if you just build the project with docker

## How to start the app ?
```
git clone git@github.com:emmanuel-santos1/kombat-jrpg.git
cd .\kombat-jrpg\
mkvirtualenv -p python3.10 -a kombat-jrpg kombat-jrpg  #create a virtual environment
pip install -r .\requirements.txt
cp .env-template .env
complete all environmet vars in .env file
docker build .
docker-compose build app
docker-compose run app loads_initial_data
docker-compose up app
visit  127.0.0.1:8000/
Go to doc for more information
```

## How to run tests ?
```
pytest
```

## How to create new user ?
```
visit  127.0.0.1:8000/register/
Complete form
```

Features:
 - ✔️ Serving Template
 - ✔️ Schemas
 - ✔️ Dependency Injection
 - ✔️ Password Hashing
 - ✔️ Unit Testing (What makes an app stable)
 - ✔️ Authentication login/create user/get token
 - ✔️ Authorization/Permissions
 - ✔️ Logging
 - ✔️ Throttling
