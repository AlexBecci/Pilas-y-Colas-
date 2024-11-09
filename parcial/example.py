# -*- coding: utf-8 -*-
class Turno:
    def __init__(self, pnumero_turno, ppaciente_nombre, phorario_turno, pestado, pedad, pfecha_turno):
        self.numero_turno = pnumero_turno
        self.paciente_nombre = ppaciente_nombre
        self.horario_turno = phorario_turno
        self.edad = pedad
        self.estado = pestado
        self.fecha_turno = pfecha_turno

    def getNumeroTurno(self):
        return self.numero_turno
    def getPacienteNombre(self):
        return self.paciente_nombre
    def getHorarioTurno(self):
        return self.horario_turno
    def getEstado(self):
        return self.estado
    def getEdad(self):
        return self.edad
    def getFechaTurno(self):
        return self.fecha_turno

    def setEstado(self,pestado):
        self.estado = pestado

    def __str__(self):  # Método para convertir el objeto a string
        return f"{self.numero_turno},{self.paciente_nombre},{self.horario_turno},{self.estado},{self.edad},{self.fecha_turno}"

def mostrar_menu():
    print("Bienvenido al Sistema de Gestión de Turnos de Pacientes\n")
    print("1. Importar Turnos desde archivo")
    print("2. Atender Siguiente Turno")
    print("3. Mostrar Turnos")
    print("4. Salir")
    # Otras opciones del menú
    opcion = input("Por favor, seleccione una opción: ")
    return opcion


def udf_importar_turnos_encola_inicial(plistaturnos,pruta):
    archivo = open(pruta, "r")
    for linea in archivo:
        linea = linea.rstrip("\n")
        cadadatodelturno = linea.split(",")
        turno = Turno(cadadatodelturno[0], #El primer dato es el número de turno
                      cadadatodelturno[1], #El segundo dato es el nombre del paciente
                      cadadatodelturno[2], #El tercer dato es el horario del turno
                      cadadatodelturno[3], #El cuarto dato es el estado del turno
                      cadadatodelturno[4], #El quinto dato es la edad del paciente
                      cadadatodelturno[5]) #El sexto dato es la fecha del turno
        plistaturnos.append(turno)

    archivo.close()

def udf_mostrar_turnos_importados(plistaturnos):
    # Imprimir encabezado de la tabla
    print(f"{'Número':<15} {'Paciente':<20} {'Horario':<10} {'Estado':<10} {'Edad':<5} {'Fecha Turno':<15}")
    # Iterar sobre cada turno en la lista de turnos
    for cadaTurno in plistaturnos:
        # Imprimir cada turno con formato tabular
        print(f"{cadaTurno.getNumeroTurno():<15} {cadaTurno.getPacienteNombre():<20} {cadaTurno.getHorarioTurno():<10} {cadaTurno.getEstado():<10} {cadaTurno.getEdad():<5} {cadaTurno.getFechaTurno():<15}")

def udf_grabar_turnos_historicos(plistaTurnosHistoricos,pruta):
    archivo = open(pruta, "w")
    for cadaTurno in plistaTurnosHistoricos:
        archivo.write(f"{cadaTurno}\n")
    archivo.close()

def udf_atender_siguiente_turno(plistaturnos):
    #Desencolar turno de la lista de turnos
    turno_desencolado = plistaturnos.pop(0)
    #Cambiar el estado del turno a 'Tomado'
    turno_desencolado.setEstado('Tomado')
    #Mostrar el turno desencolado
    print("Turno Atendido:")
    print(f"Turno N°: {turno_desencolado.getNumeroTurno()}")
    print(f"Paciente: {turno_desencolado.getPacienteNombre()}")
    print(f"Horario: {turno_desencolado.getHorarioTurno()}")
    print(f"Estado: {turno_desencolado.getEstado()}")
    print(f"Edad: {turno_desencolado.getEdad()}")
    print(f"Fecha Turno: {turno_desencolado.getFechaTurno()}")
    #Retornar el turno desencolado
    return turno_desencolado


# Programa principal
def miMain():
    ruta = r"C:\pyfiles\turnosdeldia.txt"#ruta del archivo al que queremos ir 
    ruta_historicos = r"C:\pyfiles\turnoshistoricos.txt"#ruta del archivo en historicos
    lista_turnos = []
    turnosHistoricos=[]
    while True:
        mipcion=mostrar_menu()
        if mipcion == '1':
            print("Importar Turnos desde archivo")
            udf_importar_turnos_encola_inicial(lista_turnos,ruta)
            udf_mostrar_turnos_importados(lista_turnos)
        elif mipcion == '2':
            #Control turnos x atender
            if len(lista_turnos) == 0:
                print("No hay turnos pendientes")
            else:
                print("Atender Siguiente Turno (desencola)")
                turno_atendido = udf_atender_siguiente_turno(lista_turnos)
                #El turno desencolado lo guardo en la lista de turnos historicos
                turnosHistoricos.append(turno_atendido)
                #Esa lista de historicos la mando a grabar.
                udf_grabar_turnos_historicos(turnosHistoricos,ruta_historicos)
        elif mipcion == '3':
            print("Mostrar Turnos Pendientes / Tomados / Cancelados")
            udf_mostrar_turnos_importados(lista_turnos)
        # Realizar todas las demas opciones del menu
        elif mipcion == '4':
            print("Fin del Algoritmo")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


#*-*-*--**-*-* Area Publica
miMain()