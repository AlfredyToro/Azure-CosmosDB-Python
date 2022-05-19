#from conection import client
from createdb import database
from azure.cosmos.partition_key import PartitionKey

container_name = 'atorocontainer'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/lastName"),
    offer_throughput=400
)

container_name = 'chilecontainer'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/lastName"),
    offer_throughput=400
)