# FUNCIONANDO --> NO TOCAR PERROS

"""
Autores: Maria P. Ardila, Jose N. Duque,
Ronal Y. Castro, Daniela C. García y Leopold P. Lanard
"""
from src.gestorAplicacion.instalaciones.Hospital import Hospital
from src.gestorAplicacion.instalaciones.Banco import Banco
from src.baseDatos.serializador import Serializador
from src.baseDatos.deserializador import Deserializador
from src.gestorAplicacion.serviciosOfrecidos.Consulta import Consulta
from src.gestorAplicacion.serviciosOfrecidos.Terapia import Terapia
from src.gestorAplicacion.serviciosOfrecidos.Cirugia import Cirugia
from src.gestorAplicacion.serviciosOfrecidos.Tipo import Tipo
from src.gestorAplicacion.sujeto.Categoria import Categoria
from src.gestorAplicacion.sujeto.Especialidad import Especialidad
from src.gestorAplicacion.sujeto.Medico import Medico
from src.gestorAplicacion.sujeto.Paciente import Paciente
from src.gestorAplicacion.sujeto.Enfermedad import Enfermedad

if __name__ == "__main__":
    

    
    hospital = Deserializador.cargarHospital()
    Deserializador.deserializarAtributosEstaticos(hospital)
    print(hospital.getNombre())
    print(hospital.getCuentaBancaria().getSaldo())
    for p in hospital.getPacientes():
        print(p.getNombre())

    
