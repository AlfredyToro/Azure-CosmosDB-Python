import json
from conection import client

container_name = 'atorocontainer'
database_name = 'atorodb'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

properties = database.read()
print(json.dumps(properties, indent=True))