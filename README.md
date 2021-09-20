# full_stack_example

## Instal Heroku cli
Prerequisites: 
- Heroku cli
- PostgreSQL


---
## Load Database dump (PostgreSQL)
sample database files from: https://www.postgresqltutorial.com/postgresql-sample-database/
 - extract .zip
 - convert .zip to .tar

 ```sh
 tar -czf ~/Downloads/dvdrental.tar ~/Downloads/dvdrental
 ```

 Create database
 ```sh
 psql -U postgres -c 'create database dvdrental with owner postgres';
 ```

 (May need to cd to bin folder of PostgreSQL install?)
 ```sh
 ## Mac OSx
 cd /Library/PostgreSQL/13/bin
 ```

 Use `pg_restore` to load data into database
 

 ```sh
 #load data to dvdrenatl database
 pg_restore -U postgres -d dvdrental ~/Downloads/dvdrental
 ```

Confirm tables in PostgreSQL
```sh
  psql -U postgres
  # Entrer password
  \c dvdrental
  \dt
  select count(*) from actor;
    ''' 
    output --> 
             > count
             > -------
             > 200
             > (1 row)
 ```

---

## Create Database Dump and reload (PostgreSQL)

From app folder in project directory: 
```sh
# Create dump of db
pg_dump -U postgres -Ft -b dvdrental > dvdrental.tar
```
Drop old database
```sh
# Drop old table to test reload
psql -U postgres template1 -c 'drop database dvdrental'
```
Recreate database
```sh
# Create database
psql -U postgres -c 'create database dvdrental with owner postgres';
```
Write dump to database
```sh
# load .tar file to database
pg_restore -U postgres -d dvdrental dvdrental.tar
```

Confirm tables in PostgresSQL
```sh
# start psql
psql -U postgres
# connect to database
\c dvdrental
# list database tables
\dt
# Check for data in tables
select count(*) from actor;
''' 
output --> 
             > count
             > -------
             > 200
             > (1 row)

 ```
 ### PostgreSQL resources
https://stackoverflow.com/questions/35246737/postgres-tutorial-pg-restore-archiver-input-file-does-not-appear-to-be-a-val

https://www.netguru.com/blog/how-to-dump-and-restore-postgresql-database

https://www.postgresql.org/docs/7.3/app-pgrestore.html

---
## DB Connection
app/config.py



---
## Create repo in github

include 
- Readme.md
- .gitignore

clone repo to local machine

cd into repo

----

## create virtual environment

```sh 
virtualenv venv
```

```sh 
source venv/bin/activate
```

----

## Build app

```sh 
pip install .....
pip install psycopg2-binary
```

.......

```sh 
pip freeze > requirements.txt
```


* Next, to make the `run.sh` file executable, run the following command:

  ```sh
  chmod a+x run.sh
  ```
---

## Database connection to app

Once Postgres is installed and you can connect, you’ll need to export the DATABASE_URL environment variable for your app to connect to it when running locally:
```sh
-- for Mac and Linux
export DATABASE_URL=postgres://$(whoami)
-- for Windows
set DATABASE_URL=postgres://$(whoami)
```

https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres

 it was a relatively simple project, so locally I exported from a bash file, and on Heroku I manually entered the DATABASE_URL in the Config Vars section...the database path would of course be replaced by the heroku database instead of localhost...

https://github.com/sqlalchemy/sqlalchemy/issues/6083#issuecomment-822156700

This will allow you to connect to Heroku Postgres services using SQLAlchemy >= 1.4.x


----
## Connect to Heroku 
Using github repo 

Manual deploy

## Push to main branch


---
## Prepare codebase for heroku deployment

https://devcenter.heroku.com/articles/preparing-a-codebase-for-heroku-deployment

----
## Local Postgres setup

note: psql

https://devcenter.heroku.com/articles/heroku-postgresql#local-setup

----
## Provision Heroku Postgres

https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres



## References
https://dev.to/techparida/how-to-deploy-a-flask-app-on-heroku-heb

https://codeburst.io/creating-a-full-stack-web-application-with-python-npm-webpack-and-react-8925800503d9

https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524