# DjangoFlix Search App - Search from a millions of movies and TV shows 🚀

## Setup

- Install Database 🗃️

```bash
sudo apt update 
sudo apt install libpq-dev postgresql postgresql-contrib
sudo service postgresql start
sudo -u postgres psql
```

- Create a database

```bash
CREATE DATABASE django_flix;
CREATE USER django_flix_user WITH PASSWORD 'html_programmer';
ALTER ROLE django_flix_user SET client_encoding TO 'utf8';
ALTER ROLE django_flix_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_flix_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE django_flix TO django_flix_user;
\q
```

- Install requirements

```bash
pip install psycopg2
```

- Generate Test Data

### 🎞️ This Command will take a while & populate the Database with 1M random movies

```bash
./manage.py generate_test_data 1000000
```
