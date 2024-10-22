#Escribir un programa que permita incorporar en una pila 10 elementos de tipo personal que contenga nombre, apellido y edad. Pedir por pantalla la cantidad de elementos a desapilar y mostrar los datos correspondientes.


class Personal:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad:{self.edad}"

class Pila:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.elementos = []
    
    def apilar(self, elemento):
        if len(self.elementos) >= self.capacidad:
            raise Exception("La pila está llena.")
        self.elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía.")
        return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0
    
#programa principal
if __name__ =='__main__':
    pila = Pila(capacidad=10)
    
    #Ingrso de elementos
    for i in range(10):
        nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
        apellido = input(f"Ingrese el apellido de la persona {i + 1}: ")
        edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
        
        persona = Personal(nombre,apellido,edad)
        pila.apilar(persona)
        
    #Preguntar cuantos elementos se desean desapilar
    while True:
        try:
            cantidad_a_desapilar = int(input("Ingrese la cantidad de elementos a desapilar:"))
            if cantidad_a_desapilar<1 or cantidad_a_desapilar>10:
                print('Por favor, ingresar un numero entre 1 y 10.')
                continue
            break
        except ValueError:
            print('Entrada Invalida. Ingrese un numero entero')
    
    
    #desapilando y mostrando los elementos
    print('\n Elementos desapilados:')
    for _ in range(cantidad_a_desapilar):
        if not pila.esta_vacia():
            print(pila.desapilar())
        else:
            print('No hay mas elementos en la pila')
            break # Salir del bucle si no hay mas elementos