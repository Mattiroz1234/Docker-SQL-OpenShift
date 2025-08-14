oc apply -f mysql-secret.yaml
oc apply -f mysql-pvc.yaml
oc apply -f mysql-deployment.yaml
oc apply -f mysql-service.yaml
