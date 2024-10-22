class Pila:
    def __init__(self,capacidad=10):
        self.capacidad = capacidad
        self.elementos =[]
    
    def vaciar(self):
        self.elementos.clear()

    def apilar(self,elemento):
        if len(self.elementos) >= self.capacidad:
            raise Exception('La Pila esta llena')
        self.elementos.append(elemento)
    
    def desapilar(self):
        if self.esta_vacia():
            raise Exception('La pila esta vacia')
        return self.elementos.pop()
    
    def top(self):
        if self.esta_vacia():
            raise Exception('La pila esta vacia')
        return self.elementos[-1]

    def clonar(self):
        nueva_pila = Pila(self.capacidad)
        nueva_pila.elementos = self.elementos.copy()
        return nueva_pila
    
    def obtener_tamano(self):
        return len(self.elementos)
    
    def esta_vacia(self):
        return len(self.elementos) ==0
    
    def esta_llena(self):
        return len(self.elementos)>=self.capacidad
    

# Ejemplo de uso
if __name__ == "__main__":
    pila = Pila(5)
    pila.apilar(1)
    pila.apilar(2)
    print(pila.top())  # Debería imprimir 2
    print(pila.obtener_tamano())  # Debería imprimir 2
    pila.desapilar()
    print(pila.obtener_tamano())  # Debería imprimir 1
    clon = pila.clonar()
    print(clon.top())  # Debería imprimir 1
    print(pila.esta_vacia())  # Debería imprimir False
    print(pila.esta_llena())   # Debería imprimir False
    pila.vaciar()
    print(pila.esta_vacia())  # Debería imprimir True