# bild mysql application
oc apply -f mysql-secret.yaml
oc apply -f mysql-pvc.yaml
oc apply -f mysql-deployment.yaml
oc apply -f mysql-service.yaml

# bild fastapi application
docker build -t mattiroz/fastapi-app:latest .
docker push mattiroz/fastapi-app:latest
oc apply -f fastapi-deployment.yaml
oc apply -f fastapi-service.yaml
oc apply -f fastapi-route.yaml

# create & insert db
oc cp sql/data_create.sql mysql-8489dbcf89-wwxlr:/tmp/sql.data_create.sql
oc cp sql/data_insert.sql mysql-8489dbcf89-wwxlr:/tmp/sql.data_insert.sql
oc exec -it mysql-8489dbcf89-wwxlr -- bash
mysql -u root -p
CREATE DATABASE testdb;
USE testdb;
source /tmp/sql.data_create.sql;
source /tmp/sql.data_insert.sql;