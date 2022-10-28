from Repositorios.InterfaceRepositorios import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getlistarCandidatosEnMesa(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)
    def getvotosMasAltosPorPartido(self):
        query1={
                "$group": {
                    "_id": "$mesa",
                    "max": {
                        "$max": "$numero_votos"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
        pipeline=  [query1]
        return self.queryAggregation(pipeline)
    def promedioVotosEnMesa(self,id_mesa):
        query1 = {
          "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query2 = {
          "$group": {
            "_id": "$mesa",
            "promedio": {
              "$avg": "$numero_votos"
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)