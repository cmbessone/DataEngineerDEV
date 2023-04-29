import pandas as pd
from pymongo import MongoClient

# Conectar al servidor local de MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Crear una nueva base de datos llamada "mydb"
db = client['mydb']

# Crear una nueva colección llamada "mycollection"
collection = db['mycollection']

# Insertar un documento en la colección
doc = {'name': 'John', 'age': 30, 'city': 'New York'}
inserted_id = collection.insert_one(doc).inserted_id
print(f'Document inserted with ID: {inserted_id}')

# Recuperar el documento insertado
retrieved_doc = collection.find_one({'_id': inserted_id})
print(f'Document retrieved: {retrieved_doc}')


