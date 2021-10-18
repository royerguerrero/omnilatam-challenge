# Omnilatam Challenge
A company requires a relational database to manage users, products, orders,

payments, and shipments. Please refer only to the minimum needed attributes for an e-
commerce flow.

## EcommerceFlow Project
EcommerceFlow is an online store that sells all kinds of products of premium brands, this consists of a website from where users can buy, an administrator for the staffs of the company and an api for future integrations with the application. 

[Backend Architecture](./backend_architecure.md)

[Design](https://www.figma.com/file/JNMo3L0oLzqeJ42zWjAYFL/EcommerceFlow?node-id=2%3A2)

### Run Application
First to run the application you must have the following requirements if you wish to launch the development environment with docker you can omit these requirements.

#### Requirements
- Python3
- Pip3
- PostgreSQL
- PgAdmin *optional

After ensuring that you have these requirements, you should perform the next steps

1. Creates a virtual environment -> `python3 -m venv .env`

2. Activate the virtualenv -> `source .env/bin/activate` for macos and linux, `source .env/Scripts/activate` for windows

3. Install dependence's -> `pip install -r requirements.txt`

4. Create a database in psql
```
sudo su - postgres
psql
\password postgres #pick a password for the postgres role
CREATE DATABASE ecommerceflow;
```

5. Set the settings in ecommerce_flow/settings.ini
```
[settings]
SECRET_KEY=<your_secret_key>
DEBUG=<True or False>
DATABASE_NAME=<your_database_name>
DATABASE_USER=<your_database_user>
DATABASE_PASSWORD=<your_database_password>
DATABASE_HOST=<your_database_host>
DATABASE_PORT=<your_database_port>
```
Note: Usually the db host is `localhost` and the port is `5432`

6. Run migrations and project
```
python3 manage.py migrate
python3 manage.py runserver
```

## Run Application with Docker
This is the easiest and fastest way to get your development environment.

1. Set the settings in ecommerce_flow/settings.ini
```
[settings]
SECRET_KEY=django-insecure-e74!#=*y&yy-114#&8fw9ke3e$7$-w@wb3fbi+(a-9ac60hjd
DEBUG=True
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
```

2. Build and up the services
```
docker-compose build
docker-compose up
```

### Services
- Backend -> Django `0.0.0.0:8000`
- db -> PostgreSQL 
- pgadmin -> PgAdmin `0.0.0.0:5555`

### Useful commands
- `docker-compose up` -> Start all services
- `docker-compose down` -> Stop and terminate all services
- `docker-compose exec backend bash` -> Enter in interactive mode with the backend container
