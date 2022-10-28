from flask import jsonify,request,Blueprint
from Controladores.ControladorResultado import ControladorResultado
miControladorResultado=ControladorResultado()

resultado=Blueprint('resultado', __name__)

@resultado.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)
@resultado.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@resultado.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['POST'])
def crearResultado(id_candidato,id_mesa):
    data = request.get_json()
    json=miControladorResultado.create(data,id_candidato,id_mesa)
    return jsonify(json)
@resultado.route("/resultados/<string:id_resultado>/candidato/<string:id_candidato>/mesa/<string:id_mesa>",methods=['PUT'])
def modificarResultado(id_resultado,id_candidato,id_mesa):
    data = request.get_json()
    json=miControladorResultado.update(id_resultado,data,id_candidato,id_mesa)
    return jsonify(json)
@resultado.route("/resultados/<string:id_resultado>",methods=['DELETE'])
def eliminarResultado(id_resultado):
    json=miControladorResultado.delete(id_resultado)
    return jsonify(json)
@resultado.route("/resultados/mesa/<string:id_mesa>",methods=['GET'])
def ResultadosEnMesa(id_mesa):
    json=miControladorResultado.listarResultadosEnMesa(id_mesa)
    return jsonify(json)
@resultado.route("/resultados/votos_mayores",methods=['GET'])
def getVotosMayores():
    json=miControladorResultado.votosMasAltosPorPartido()
    return jsonify(json)
@resultado.route("/resultados/promedio_votos/mesa/<string:id_mesa>",methods=['GET'])
def getpromedioVotosEnMesa(id_mesa):
    json=miControladorResultado.promedioVotosEnMesa(id_mesa)
    return jsonify(json)