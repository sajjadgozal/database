### Run db locally  
## copy .env file from .env.example

# postgres db : 
docker compose up -d --build  postgres 

# mysql 
docker compose up -d --build  mysql 

# ms-sql
 docker-compose up -d --build mssql

 # Redis
 docker compose up -d --build redis


### test 
python test_redis.py