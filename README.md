<div align="center">
    <h1>Real Estate Site</h1>
    <a href="https://www.hassani-realestate.co">Visit Site</a>
    <h3>Home Page</h3>
    <img src="https://i.imgur.com/c9kYp92.png" title="Real Estate Home Page"/>
</div>

## URL
<>
</div>

# Setting up Development Environment
### Creating Virtual Environment
```
mkdir -p prj && cd prg
git clone https://github.com/HKSenior/Real-Estate-Site.git
virtualenv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

### To exit the Virtual Environment
```
deactivate
```

## Postgres Database & User Setup
### Installing PostgreSQL
<http://postgresguide.com/setup/install.html>

### Accessing PostgreSQL
```
sudo -u postgres psql
```

### Create a database
```
CREATE DATABASE {your project name};
```

### Create user
```
CREATE USER {admin name} WITH PASSWORD '{your password}';
```

### Set default encoding, tansaction isolation scheme (Recommended from Django)
```
ALTER ROLE dbadmin SET client_encoding TO 'utf8';
ALTER ROLE dbadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE dbadmin SET timezone TO 'UTC';
```

### Give User access to database
```
GRANT ALL PRIVILEGES ON DATABASE {your project name} TO {admin name};
```

### Quit out of Postgres
```
\q
```

## Collecting static files
```
python manage.py collectstatic
```

## Starting the server
```
python manage.py runserver
```

# Setting up .env config file
#### Django Configuration
- SECRET_KEY
- ALLOWED_HOSTS
- DEBUG

#### Database Configuration (PostgreSQL)
- DB_ENGINE
- DB_USER
- DB_HOST
- DB_PASSWORD
- DB_ENGINE

#### Email Configuration
- EMAIL_PORT
- EMAIL_USE_TLS
- EMAIL_FAIL_SILENTLY
- EMAIL_HOST
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD

## Future Upgrades
- [ ] Scrape real estate information from the internet to populate the listings.