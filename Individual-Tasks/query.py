
from conection import client
from createdb import database
import json

container_name = 'atorocontainer'
database_name = 'atorodb'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

for item in container.query_items(
    query='SELECT * FROM products p WHERE p.productModel <> "DISCONTINUED"',
    enable_cross_partition_query=True,
):
    print(json.dumps(item, indent=True))

-------

discontinued_items = container.query_items(
    query='SELECT * FROM products p WHERE p.productModel = @model AND p.productName="Widget"',
    parameters=[dict(name="@model", value="DISCONTINUED")],
)
for item in discontinued_items:
    print(json.dumps(item, indent=True))