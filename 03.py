class Pila:
    def __init__(self, capacidad=100):
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

    def obtener_tamano(self):
        return len(self.elementos)
    
#Programa principal
if __name__=="__main__":
    pila = Pila()
    
    #ingreso de numeros
    while True:
        try:
            n  = int(input('Ingrese la cantidad de numeros a almacenar en la pila: '))
            if n <1:
                print('Por favor, ingrese un numero positivo')
                continue
            break
        except ValueError:
            print('Entrada Invalida. Por Favor, ingrese un numero entero valido')
    for i in range(n):
       while True:
           try:
                numero = int(input(f'Ingrese el numero {i + 1}: '))
                pila.apilar(numero)
                break # Salir del bucle 
           except ValueError:
               print('Entrada Invalida.Por favor, Ingrese un numero entero')
    
    print('\nNumeros Ingresados (desapilados):')
    
    #desapilando y mostrando los numeros
    while not pila.esta_vacia():
        print(pila.desapilar())