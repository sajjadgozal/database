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

# Cassandra 
 docker compose up -d --build cassandra

# Elasticsearch
mkdir -p ./data/esdata
sudo chown -R 1000:1000 ./data/esdata
docker compose up -d --build elasticsearch

# Kibana 
docker compose up -d --build kibana

# Typesense
docker compose up -d --build typesense

### test 
python test_redis.py