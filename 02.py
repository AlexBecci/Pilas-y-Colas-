class Pila:
    def __init__(self,capacidad=10):
        self.capacidad = capacidad
        self.elementos = []

    def vaciar(self):
        self.elementos.clear()
    
    def apilar(self,elemento):
        if len(self.elementos) >= self.capacidad:
            raise Exception('La pila esta llena')
        self.elementos.append(elemento)
    
    def desapilar(self):
        if self.esta_vacia():
            raise Exception('La pila esta vacia')
        return self.elementos.pop()

    def top(self):
        if self.esta_vacia():
            raise Exception('La pila esta vacia')
        return self.elementos[-1]

    def obtener_tamano(self):
        return len(self.elementos)

    def esta_vacia(self):
        return len(self.elementos)==0
    
    def esta_llena(self):
        return len(self.elementos)>=self. capacidad

#programa
if __name__ == '__main__':
    pila = Pila(5)
    #apilando alfunos elementos
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)

    #mostrando la cantidad de elementos en la pila
    print(f"Tamaño de la pila: {pila.obtener_tamano()}")  # Debería imprimir 3

    # Desapilando dos elementos
    print(f"Elemento desapilado: {pila.desapilar()}")  # Debería imprimir 30
    print(f"Elemento desapilado: {pila.desapilar()}")  # Debería imprimir 20

    # Volviendo a imprimir el tamaño de la pila
    print(f"Tamaño de la pila después de desapilar: {pila.obtener_tamano()}")  # Debería imprimir 1