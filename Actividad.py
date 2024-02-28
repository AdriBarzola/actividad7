from typing import List, Dict

class Instrumento:
    def __init__(self, id: str, precio: float, tipo: str):
        self.id = id
        self.precio = precio
        self.tipo = tipo

    def mostrarDatos(self):
        print(f"ID: {self.id}, Precio: {self.precio}, Tipo: {self.tipo}")

class Sucursal:
    def __init__(self, nombre: str, instrumentos: List[Instrumento]):
        self.nombre = nombre
        self.instrumentos = instrumentos

    def listarInstrumentos(self):
        print(f"Instrumentos en la sucursal {self.nombre}:")
        for instrumento in self.instrumentos:
            instrumento.mostrarDatos()

    def instrumentosPorTipo(self, tipo: str) -> List[Instrumento]:
        return [instrumento for instrumento in self.instrumentos if instrumento.tipo == tipo]

    def borrarInstrumento(self, id: str):
        self.instrumentos = [instrumento for instrumento in self.instrumentos if instrumento.id != id]

    def porcInstrumentosPorTipo(self) -> Dict[str, float]:
        tipos = set([instrumento.tipo for instrumento in self.instrumentos])
        total = len(self.instrumentos)
        porcentajes = {}
        for tipo in tipos:
            cantidad_tipo = len([instrumento for instrumento in self.instrumentos if instrumento.tipo == tipo])
            porcentaje = (cantidad_tipo / total) * 100
            porcentajes[tipo] = porcentaje
        return porcentajes


if __name__ == "__main__":
    # Crear algunos instrumentos
    instrumento1 = Instrumento("001", 100.0, "Percusión")
    instrumento2 = Instrumento("002", 200.0, "Viento")
    instrumento3 = Instrumento("003", 150.0, "Cuerda")

    # Crear una sucursal con los instrumentos
    sucursal = Sucursal("Sucursal Principal", [instrumento1, instrumento2, instrumento3])

    # Parte A: Listar instrumentos
    sucursal.listarInstrumentos()

    # Parte B: Instrumentos por tipo
    print("Instrumentos de tipo Viento:")
    for instrumento in sucursal.instrumentosPorTipo("Viento"):
        instrumento.mostrarDatos()

    # Parte C: Borrar un instrumento por ID
    sucursal.borrarInstrumento("001")
    print("Instrumentos después de borrar:")
    sucursal.listarInstrumentos()

    # Parte D: Porcentaje de instrumentos por tipo
    print("Porcentaje de instrumentos por tipo:")
    porcentajes = sucursal.porcInstrumentosPorTipo()
    for tipo, porcentaje in porcentajes.items():
        print(f"{tipo}: {porcentaje}%")
