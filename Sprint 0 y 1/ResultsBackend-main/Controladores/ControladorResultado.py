from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion candidato y mesa a resultado
    """
    def create(self,infoResultado,id_candidato,id_mesa):
        nuevoResultado=Resultado(infoResultado)
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        LaMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato=elCandidato
        nuevoResultado.mesa=LaMesa
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de Resultado (Candidato y mesa)
    """
    def update(self,id,infoResultado,id_candidato,id_mesa):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.numero_mesa=infoResultado["numero_mesa"]
        elResultado.id_partido = infoResultado["id_partido"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)
    def delete(self, id):
        return self.repositorioResultado.delete(id)
    "Obtener todos los candidatos en una mesa"
    def listarResultadosEnMesa(self,id_mesa):
        return self.repositorioResultado.getlistarCandidatosEnMesa(id_mesa)
    "Obtener votos mas altos por partido"
    def votosMasAltosPorPartido(self):
        return self.repositorioResultado.getvotosMasAltosPorPartido()
    "Obtener promedio de votos en mesa"
    def promedioVotosEnMesa(self,id_mesa):
        return self.repositorioResultado.promedioVotosEnMesa(id_mesa)