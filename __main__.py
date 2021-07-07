from datetime import datetime

from seleccionestudiante.logica.Sorteo import Sorteo
from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.declarative_base import Session, engine, Base

def añadeRegistros():
        Base.metadata.create_all ( engine )
        session = Session()

        estudiante1 = Estudiante ( apellidoPaterno = "Ramos" , apellidoMaterno = "Ortega" , nombres = "Juan Carlos" , elegible = True)
        estudiante2 = Estudiante ( apellidoPaterno = "Solis" , apellidoMaterno = "Matos" , nombres = "Pedro" , elegible = True)
        estudiante3 = Estudiante ( apellidoPaterno = "Paredes" , apellidoMaterno = "Torres" , nombres = "Luis Alberto" , elegible = True)
        estudiante4 = Estudiante ( apellidoPaterno = "Garcia" , apellidoMaterno = "Mateo" , nombres = "Miguel Angel" , elegible = True)

        session.add(estudiante1)
        session.add(estudiante2)
        session.add(estudiante3)
        session.add(estudiante4)
        session.commit ( )

        asignatura1 = Asignatura ( nombreAsignatura = "Análisis y diseño de sistemas" )
        asignatura2 = Asignatura( nombreAsignatura="Pruebas de software" )

        session.add ( asignatura1 )
        session.add ( asignatura2 )
        session.commit ( )

        equipo1 = Equipo ( denominacionEquipo = "Equipo01" )
        equipo2 = Equipo ( denominacionEquipo = "Equipo02" )
        session.add ( equipo1 )
        session.add ( equipo2 )
        session.commit ( )

        actividad1 = Actividad ( denominacionActividad = "Prueba unitaría", fecha=datetime(2001, 9, 28, 00, 00, 00, 0000) )
        actividad2 = Actividad ( denominacionActividad = "TDD", fecha=datetime(2001, 9, 25, 00, 00, 0000) )
        actividad3 = Actividad ( denominacionActividad = "BDD", fecha=datetime(2001, 9, 25, 00, 00, 00, 0000) )
        session.add ( actividad1 )
        session.add ( actividad2 )
        session.add ( actividad3 )
        session.commit ( )

        equipo1.actividades = [actividad1,actividad2]
        equipo2.actividades = [actividad3]
        session.commit()

        asignatura1.estudiantes = [ estudiante1 , estudiante4 ]
        asignatura2.estudiantes = [ estudiante2 , estudiante3 ]
        session.commit()

        equipo1.estudiantes = [estudiante1, estudiante3]
        equipo2.estudiantes = [estudiante2, estudiante4]
        session.commit()

        session.close ( )

def eliminarRegistros():
        session = Session ( )

        estudiantes=session.query(Estudiante).all()
        for estudiante in estudiantes:
                session.delete(estudiante)
        session.commit()
        session.close()

        asignaturas = session.query(Asignatura).all()
        for asignatura in asignaturas :
                session.delete ( asignatura )
        session.commit (  )
        session.close ( )

        activdades = session.query(Actividad).all()
        for activdad in activdades :
                session.delete ( activdad )
        session.commit (  )
        session.close ( )

        equipos = session.query(Equipo).all()
        for equipo in equipos :
                session.delete ( equipo )
        session.commit (  )
        session.close ( )

if __name__ == '__main__':
        sorteo=Sorteo()
        sorteo.agregar_asignatura ( "Matematica discreta" )
        while True :
                print("0 Salir")
                print("1 Añadir registros")
                print("2 Elimnar registros")
                opcion = int (input("Opcion: "))
                if opcion == 0 :
                        print("Fin ...")
                        break
                elif opcion == 1 :
                        añadeRegistros()
                        print("Registros añadidos")
                elif opcion == 2 :
                        eliminarRegistros()
                        print("Registrar eliminados")
                else :
                        print("Opcion incorrecta")
                print("\n\n\n")
