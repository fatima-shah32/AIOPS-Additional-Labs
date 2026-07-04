#!/bin/bash

source scripts/set_variables.sh

export COSMOS_ENDPOINT=$(az cosmosdb show \
  --name $COSMOS_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --query 'documentEndpoint' \
  --output tsv)

export COSMOS_KEY=$(az cosmosdb keys list \
  --name $COSMOS_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --type keys \
  --query 'primaryMasterKey' \
  --output tsv)

export DATABASE_NAME=$DATABASE_NAME
export CONTAINER_NAME=$CONTAINER_NAME
export RESOURCE_GROUP=$RESOURCE_GROUP
export COSMOS_ACCOUNT=$COSMOS_ACCOUNT

echo "Environment variables loaded successfully."
echo "COSMOS_ENDPOINT=$COSMOS_ENDPOINT"
echo "DATABASE_NAME=$DATABASE_NAME"
echo "CONTAINER_NAME=$CONTAINER_NAME"
