import certifi
import pymongo

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://appRegistraduria:appRegistraduria123*@cluster0.g4hhzan.mongodb.net/bd-registraduria-candidato?retryWrites=true&w=majority",tlsCAFile=ca)

baseDatos = client["bd-registraduria-candidato"]
print(baseDatos.list_collection_names())