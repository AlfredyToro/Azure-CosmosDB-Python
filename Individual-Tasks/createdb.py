from conection import client
# Create a database
# <create_database_if_not_exists>
database_name = 'atorodb'
database = client.create_database_if_not_exists(id=database_name)
# </create_database_if_not_exists>