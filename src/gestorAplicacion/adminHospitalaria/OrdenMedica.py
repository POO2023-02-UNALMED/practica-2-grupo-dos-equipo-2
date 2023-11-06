"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""
from src.gestorAplicacion.serviciosOfrecidos.Tratamiento import Tratamiento
from src.gestorAplicacion.sujeto.Paciente import Paciente
from src.gestorAplicacion.sujeto.Enfermedad import Enfermedad
from src.gestorAplicacion.sujeto.Medico import Medico


#Clase que generará la orden médica, aquí introduciremos todo lo necesario que tiene una orden medica
class OrdenMedica:
    #inicializador
    def __init__(self,registro,recomendaciones):
        self._paciente=Paciente()
        self._enfermedad=Enfermedad()
        self._registro=registro
        self._medico=Medico()
        self._tratamiento=Tratamiento()
        self._recomendaciones=recomendaciones

    # Getters y setters
    def getPaciente(self):
        return self._paciente
    
    def setPaciente(self, paciente):
        self._paciente=paciente

    def getEnfermedad(self):
        return self._enfermedad
    
    def setEnfermedad(self, enfermedad):
        self._enfermedad=enfermedad

    def getRegistro(self):
        return self._registro
    
    def setRegistro(self, registro):
        self._registro=registro
    
    def getMedico(self):
        return self._medico
    
    def setMedico(self, medico):
        self._medico=medico

    def getTratamiento(self):
        return self._tratamiento
    
    def setTratamiento(self, tratamiento):
        self._tratamiento=tratamiento
    
    def getRecomendaciones(self):
        return self._recomendaciones
    
    def setRecomendaciones(self, recomendaciones):
        self._recomendaciones=recomendaciones