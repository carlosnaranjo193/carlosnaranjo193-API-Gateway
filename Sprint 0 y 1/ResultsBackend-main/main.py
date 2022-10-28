from flask import Flask
from flask_cors import CORS
import json
from waitress import serve
from Routes.Mesa import mesa
from Routes.Partido import partidos
from Routes.Resultado import resultado
from Routes.Candidato import candidato
#prueba carlos pychar
app=Flask(__name__)
cors = CORS(app)

app.register_blueprint(candidato)
app.register_blueprint(partidos)
app.register_blueprint(resultado)
app.register_blueprint(mesa)

app.debug = True

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])