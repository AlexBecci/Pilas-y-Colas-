class Fecha:
    def __init__(self,dia,mes,ano) :
        self.dia=dia
        self.mes=mes
        self.ano=ano
        

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"

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

#programa principa
if __name__ =='__main__':
    pila = Pila(capacidad=4)
    
    #ingreso de fechas
    for i in range(4):
        dia = int(input(f"Ingrese el día de la fecha {i + 1}: "))
        mes = int(input(f"Ingrese el mes de la fecha {i + 1}: "))
        ano = int(input(f"Ingrese el año de la fecha {i + 1}: "))
        fecha = Fecha(dia,mes,ano)
        pila.apilar(fecha)
        
    
    #deapilando y mostrando las fechas
    print('\n Fehcas Ingresadas (desapiladas): ')
    while not pila.esta_vacia():
        print(pila.desapilar())