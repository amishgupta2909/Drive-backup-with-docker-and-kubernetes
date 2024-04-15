#!/bin/bash

docker build -t backup .

kubectl apply -f pvc.yaml

kubectl apply -f cronjob.yaml

kubectl get cronjobs