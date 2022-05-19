import pandas as pd 
import json
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.documents as documents
import azure.cosmos.http_constants as http_constants

print('Imported packages successfully.')


config = {
    "url": "https://cosmosdb-test-at.documents.azure.com:443/",
    "credential": "gQZPCmcyb3nIQUUGZ1J4IFzQvR7jnn7TmwjxWw12Kj7lJf0Ww6gB9Q4IXG7vQ9DXCVEisyVrovWnneNNN4c9bw=="
}

# Create the cosmos client
client = cosmos_client.CosmosClient(url=config["url"], credential={"masterKey":config["credential"]}
)

#az cosmosdb create --name cosmosdb-test-at \
#--resource-group CosmosDB-Test \
#--locations regionName=eastus \
#--subscription c5e6b62c-6f53-4cb4-aae1-3fa46fc6725e