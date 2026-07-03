#!/bin/bash

echo "Inserting normal network traffic logs..."

curl -X POST "localhost:9200/network-traffic/_doc/1" -H 'Content-Type: application/json' -d'
{
  "@timestamp": "2025-07-10T00:00:00Z",
  "ip_address": "192.168.1.1",
  "bytes_sent": 5000,
  "bytes_received": 3000
}
'

curl -X POST "localhost:9200/network-traffic/_doc/2" -H 'Content-Type: application/json' -d'
{
  "@timestamp": "2025-07-10T00:15:00Z",
  "ip_address": "192.168.1.2",
  "bytes_sent": 5200,
  "bytes_received": 3200
}
'

curl -X POST "localhost:9200/network-traffic/_doc/3" -H 'Content-Type: application/json' -d'
{
  "@timestamp": "2025-07-10T00:30:00Z",
  "ip_address": "192.168.1.3",
  "bytes_sent": 4800,
  "bytes_received": 3100
}
'

curl -X POST "localhost:9200/network-traffic/_doc/4" -H 'Content-Type: application/json' -d'
{
  "@timestamp": "2025-07-10T00:45:00Z",
  "ip_address": "192.168.1.4",
  "bytes_sent": 5100,
  "bytes_received": 2900
}
'

echo "Inserting anomalous network traffic log..."

curl -X POST "localhost:9200/network-traffic/_doc/5" -H 'Content-Type: application/json' -d'
{
  "@timestamp": "2025-07-10T01:00:00Z",
  "ip_address": "192.168.1.100",
  "bytes_sent": 50000,
  "bytes_received": 10000
}
'

echo "Data insertion completed."
