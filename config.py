from pymongo import MongoClient

MONGO_URI = 'mongodb://admin:adminpass@localhost:27017/surveyDB?authSource=admin'

def get_database():
    try:
        client = MongoClient(MONGO_URI)
        client.admin.command('ping')
        print("¡Conexión exitosa a MongoDB!")
        return client.surveyDB
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")
        raise e
