#!/bin/bash

echo "Container Status"

sudo docker ps

echo

echo "Backend Health"

for port in 8081 8082 8083

do

curl -s http://localhost:$port | grep "Server Location"

done

echo

echo "Gateway Logs"

sudo docker logs application-gateway --tail 10
