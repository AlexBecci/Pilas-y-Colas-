# -*- coding: utf-8 -*-
import os

class tdaPedido:
    def __init__(self, numero_pedido, nombre_cliente, producto, estado, fecha_pedido):
        self.numero_pedido = numero_pedido
        self.nombre_cliente = nombre_cliente
        self.producto = producto
        self.estado = estado
        self.fecha_pedido = fecha_pedido

    def getEstado(self):
        return self.estado

    def setEstado(self, nuevo_estado):
        self.estado = nuevo_estado

    def __str__(self):  # Método para convertir el objeto a string
        return f"{self.numero_pedido},{self.nombre_cliente},{self.producto},{self.estado},{self.fecha_pedido}"


def mostrar_menu():
    print("\n--- Sistema de Gestión de Pedidos en Línea ---\n")
    print("1. Importar Pedidos desde archivo")
    print("2. Gestionar Siguiente Pedido")
    print("3. Mostrar Todos los Pedidos")
    print("4. Generar pedidos pendientes y Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def importar_pedidos(pruta, pcola_pedidos):
    """Lee el archivo y encola hasta un máximo de 10 pedidos."""
    if not os.path.exists(pruta):
        print(f"Error: No se encuentra el archivo en la ruta {pruta}")
        return

    try:
        with open(pruta, "r") as archivo:
            for i, linea in enumerate(archivo):
                if i >= 10:  # Limitar la cola a 10 pedidos
                    print("Se alcanzó el límite de 10 pedidos. Los adicionales serán descartados.")
                    break

                linea = linea.strip()
                if not linea:
                    continue

                datos = linea.split(",")
                if len(datos) != 5:
                    print(f"Formato incorrecto en la línea: {linea}")
                    continue

                # Crear un objeto tdaPedido y encolarlo
                pedido = tdaPedido(datos[0], datos[1], datos[2], datos[3], datos[4])
                pcola_pedidos.append(pedido)
        print("Pedidos importados exitosamente.")
    except Exception as e:
        print(f"Error al importar pedidos: {e}")


def entregar_pedido(pcola_pedidos, plista_pendientes):
    """Desencola el siguiente pedido y gestiona su entrega."""
    if not pcola_pedidos:
        print("No hay más pedidos por entregar.")
        return

    # Desencolar el primer pedido
    pedido_actual = pcola_pedidos.pop(0)
    print("\nProcesando pedido:")
    print(f"Pedido N°: {pedido_actual.numero_pedido}")
    print(f"Cliente: {pedido_actual.nombre_cliente}")
    print(f"Producto: {pedido_actual.producto}")
    print(f"Estado actual: {pedido_actual.estado}")

    # Preguntar si se pudo entregar
    entregado = input("¿Pudo entregarse el pedido? (s/n): ").lower()
    if entregado == 's':
        pedido_actual.setEstado("entregado")
    else:
        pedido_actual.setEstado("no entregado")
        plista_pendientes.append(pedido_actual)

    print(f"Estado final del pedido: {pedido_actual.getEstado()}")


def mostrar_pedidos(pcola_pedidos):
    """Muestra todos los pedidos en la cola."""
    if not pcola_pedidos:
        print("No hay pedidos en la cola.")
        return

    print("\nPedidos en la cola:")
    print(f"{'Número':<10} {'Cliente':<20} {'Producto':<20} {'Estado':<15} {'Fecha':<12}")
    print("-" * 80)
    for pedido in pcola_pedidos:
        print(f"{pedido.numero_pedido:<10} {pedido.nombre_cliente:<20} {pedido.producto:<20} {pedido.estado:<15} {pedido.fecha_pedido:<12}")


def generar_reporte(plista_pendientes, pruta_pendientes):
    """Genera el archivo final con los pedidos no entregados."""
    try:
        with open(pruta_pendientes, "w") as archivo:
            for pedido in plista_pendientes:
                archivo.write(f"{pedido}\n")
        print(f"Reporte generado en {pruta_pendientes}")
    except Exception as e:
        print(f"Error al generar el reporte: {e}")


# Programa principal
def main():
    ruta_pedidos = r"C:\pyfiles\pedidos.txt"
    ruta_pendientes = r"C:\pyfiles\pedidos_pendientes.txt"
    cola_pedidos = []
    lista_pendientes = []

    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            print("\nImportando pedidos desde archivo...")
            importar_pedidos(ruta_pedidos, cola_pedidos)
        elif opcion == '2':
            print("\nEntregando siguiente pedido...")
            entregar_pedido(cola_pedidos, lista_pendientes)
        elif opcion == '3':
            print("\nMostrando todos los pedidos...")
            mostrar_pedidos(cola_pedidos)
        elif opcion == '4':
            print("\nGenerando reporte diario y finalizando el sistema.")
            generar_reporte(lista_pendientes, ruta_pendientes)
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
