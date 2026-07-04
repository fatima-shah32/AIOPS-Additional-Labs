import os
from azure.cosmos import CosmosClient

endpoint = os.environ["COSMOS_ENDPOINT"]
key = os.environ["COSMOS_KEY"]

client = CosmosClient(endpoint,key)

database=client.get_database_client(
    os.environ["DATABASE_NAME"]
)

container=database.get_container_client(
    os.environ["CONTAINER_NAME"]
)

item={
"id":"failover-test",
"region":"global",
"message":"Failover Successful"
}

container.upsert_item(item)

result=container.read_item(
item="failover-test",
partition_key="global"
)

print("Item Retrieved Successfully")
print(result)
