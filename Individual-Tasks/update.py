from conection import client

container_name = 'atorocontainer'
database_name = 'atorodb'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

item = container.read_item("item3", partition_key="Widget")
item["productModel"] = "DISCONTINUED"
updated_item = container.upsert_item(item)