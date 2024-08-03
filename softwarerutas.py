import matplotlib.pyplot as plt

class Ruta:
    def __init__(self, nombre, tiempo_viaje, costo_operativo, frecuencia, capacidad):
        self.nombre = nombre
        self.tiempo_viaje = tiempo_viaje
        self.costo_operativo = costo_operativo
        self.frecuencia = frecuencia
        self.capacidad = capacidad

    def optimizar(self):
        # Simulación simple de optimización
        self.tiempo_viaje *= 0.85  # Reduce el tiempo de viaje en un 15%
        self.costo_operativo *= 0.90  # Reduce el costo operativo en un 10%
        self.frecuencia *= 1.25  # Aumenta la frecuencia en un 25%
        if self.capacidad < 80:
            self.capacidad *= 1.2  # Aumenta la capacidad en un 20% si es menor a 80

def ingresar_ruta():
    nombre = input("Ingrese el nombre de la ruta: ")
    tiempo_viaje = float(input("Ingrese el tiempo de viaje actual (en minutos): "))
    costo_operativo = float(input("Ingrese el costo operativo actual (por km): "))
    frecuencia = float(input("Ingrese la frecuencia actual (en minutos): "))
    capacidad = int(input("Ingrese la capacidad actual de los vehículos: "))
    return Ruta(nombre, tiempo_viaje, costo_operativo, frecuencia, capacidad)

def mostrar_resultados(rutas):
    for ruta in rutas:
        print(f"\nResultados para la ruta {ruta.nombre}:")
        print(f"Tiempo de viaje reducido: {(1 - ruta.tiempo_viaje / rutas_originales[ruta.nombre].tiempo_viaje) * 100:.1f}%")
        print(f"Costos operativos reducidos: {(1 - ruta.costo_operativo / rutas_originales[ruta.nombre].costo_operativo) * 100:.1f}%")
        print(f"Aumento en frecuencia: {(ruta.frecuencia / rutas_originales[ruta.nombre].frecuencia - 1) * 100:.1f}%")
        print(f"Cambio en capacidad de vehículos: {(ruta.capacidad / rutas_originales[ruta.nombre].capacidad - 1) * 100:.1f}%")

def graficar_resultados(rutas):
    nombres = [ruta.nombre for ruta in rutas]
    tiempo_viaje_reducido = [(1 - ruta.tiempo_viaje / rutas_originales[ruta.nombre].tiempo_viaje) * 100 for ruta in rutas]
    costos_reducidos = [(1 - ruta.costo_operativo / rutas_originales[ruta.nombre].costo_operativo) * 100 for ruta in rutas]

    fig, ax = plt.subplots(figsize=(12, 6))
    x = range(len(nombres))
    width = 0.35

    ax.bar([i - width/2 for i in x], tiempo_viaje_reducido, width, label='Tiempo de viaje reducido (%)')
    ax.bar([i + width/2 for i in x], costos_reducidos, width, label='Costos operativos reducidos (%)')

    ax.set_ylabel('Porcentaje de reducción')
    ax.set_title('Optimización de Rutas de Transporte Público')
    ax.set_xticks(x)
    ax.set_xticklabels(nombres)
    ax.legend()

    plt.tight_layout()
    plt.show()

# Programa principal
rutas = []
rutas_originales = {}
num_rutas = int(input("Ingrese el número de rutas a optimizar: "))

for _ in range(num_rutas):
    ruta = ingresar_ruta()
    rutas.append(ruta)
    rutas_originales[ruta.nombre] = Ruta(ruta.nombre, ruta.tiempo_viaje, ruta.costo_operativo, ruta.frecuencia, ruta.capacidad)

for ruta in rutas:
    ruta.optimizar()

mostrar_resultados(rutas)
graficar_resultados(rutas)