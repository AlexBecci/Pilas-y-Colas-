class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise Exception("La pila está vacía.")
        return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def obtener_tamano(self):
        return len(self.elementos)

    def __str__(self):
        return str(self.elementos)

def invertir_pila(pila):
    if pila.esta_vacia():
        return
    # Desapila el elemento superior
    elemento = pila.desapilar()
    # Llama recursivamente para invertir el resto de la pila
    invertir_pila(pila)
    # Vuelve a apilar el elemento desapilado
    pila.apilar(elemento)

# Programa principal
if __name__ == "__main__":
    pila = Pila()

    # Ingreso de elementos
    for i in range(5):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        pila.apilar(numero)

    print("\nPila original:", pila)

    # Invertir la pila
    invertir_pila(pila)

    print("Pila invertida:", pila)
