#defninimos la clase turno
class Turno:
    def __init__(self,numero_turno,paciente_nombre,horario_turno,estado,edad,fecha_turno):
        self.numero_turno = numero_turno
        self.paciente_nombre = paciente_nombre
        self.horario_turno = horario_turno
        self.estado = estado
        self.edad = edad
        self.fecha_turno = fecha_turno
    
    #funcion toString para ver el objecto con sus valores de manera sencilla
    def __str__(self):
        return f'Turno {self.numero_turno} : {self.paciente_nombre} - {self.horario_turno} ({self.estado})'
    
    
    

#funcino para leer los turnos
def leer_turnos(ruta):
    turnos = []
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
           # turno = Turno(int(datos[0],datos[1],datos[2],datos[3],int(datos[4]),datos[5]))
           # Suponiendo que solo el primer elemento de cada línea debe ser un entero
            turno = Turno(int(datos[0]), datos[1], datos[2], datos[3], int(datos[4]), datos[5])
            turnos.append(turno)
    return turnos


#funcion para atender un turno
def atender_turno(cola_turnos,cola_historico):
    if not cola_turnos:
        print('No hay mas turnos pendientes.')
        return
    turno_atendido= cola_turnos.pop(0)
    turno_atendido.estado ='tomado'
    cola_historico.append(turno_atendido)
    print(f'Turno atendido: {turno_atendido}')

#funcion que muestra todo los turnos
def mostrar_turnos(cola_turnos):
    for turno in cola_turnos:
        print(turno)


#codigo main principal que consume de el archivo Turno.py

#importamos la libreria os
import os

ruta = 'turnosdeldia.txt'
ruta_historicos = 'turnoshistorico.txt'

#creamos las colas y la inizialicamos vacias 
cola_turnos = []
cola_historico =[]

#importamos los turnos iniciales
turnos_iniciales = leer_turnos(ruta)
cola_turnos.extend(turnos_iniciales)

while True:
    print('\nMenu:')
    print('1. Atender turno:')
    print('2. Mostrar todos los turnos')
    print('3. Salir')
    #ingresamos la opcion mediante inpiut
    opcion = input('Ingrese una opcion: ')
    
    if opcion=='1':
        atender_turno(cola_turnos,cola_historico)
    elif opcion =='2':
        mostrar_turnos(cola_turnos)
    elif opcion =='3':
        break
    else:
        print('Opcion Invalida')
    
#guardamos los turnos historicos en un archivo
with open(ruta_historicos, 'a') as archivo:
    for turno in cola_historico:
         archivo.write(f"{turno.numero_turno},{turno.paciente_nombre},{turno.horario_turno},{turno.estado},{turno.edad},{turno.fecha_turno}\n")