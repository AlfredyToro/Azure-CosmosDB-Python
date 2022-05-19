from conection import client

container_name = '*'
database_name = 'atorodb'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

for container in database.list_containers():
    print("Container ID: {}".format(container['id']))