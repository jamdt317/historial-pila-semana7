import pytest

# ==========================================
# 1. TDA PILA (Implementación Manual LIFO)
# ==========================================
class Nodo:
    """Nodo individual para la estructura enlazada de la pila."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    """Estructura de datos Pila (Stack) basada en nodos enlazados."""
    def __init__(self):
        self._cuspide = None
        self._tamano = 0

    def apilar(self, elemento) -> None:
        """Agrega un elemento a la cima de la pila (Push)."""
        nuevo_nodo = Nodo(elemento)
        nuevo_nodo.siguiente = self._cuspide
        self._cuspide = nuevo_nodo
        self._tamano += 1

    def desapilar(self):
        """Elimina y retorna el elemento en la cima de la pila (Pop)."""
        if self.esta_vacia():
            raise IndexError("No se puede desapilar de una pila vacía.")
        dato = self._cuspide.dato
        self._cuspide = self._cuspide.siguiente
        self._tamano -= 1
        return dato

    def ver_cuspide(self):
        """Consulta el elemento en la cima sin eliminarlo (Peek/Top)."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")
        return self._cuspide.dato

    def esta_vacia(self) -> bool:
        """Verifica si la pila no tiene elementos."""
        return self._cuspide is None

    def cantidad_elementos(self) -> int:
        """Retorna la cantidad de elementos almacenados."""
        return self._tamano


# ==========================================
# 2. PATRÓN DE DISEÑO REPOSITORY
# ==========================================
class HistorialRepository:
    """
    Repositorio que desacopla el almacenamiento de datos (Pila) 
    de la lógica principal de la aplicación.
    """
    def __init__(self):
        self._pila_historial = Pila()

    def guardar_accion(self, accion: str) -> None:
        """Agrega una nueva acción al historial."""
        self._pila_historial.apilar(accion)

    def deshacer_ultima_accion(self) -> str:
        """Remueve y devuelve la última acción realizada."""
        return self._pila_historial.desapilar()

    def ver_ultima_accion(self) -> str:
        """Consulta la última acción sin eliminarla."""
        return self._pila_historial.ver_cuspide()

    def esta_vacio(self) -> bool:
        """Indica si no hay acciones en el historial."""
        return self._pila_historial.esta_vacia()

    def total_acciones(self) -> int:
        """Devuelve el total de acciones registradas."""
        return self._pila_historial.cantidad_elementos()


# ==========================================
# 3. PRUEBAS UNITARIAS (pytest)
# ==========================================
def test_pila_apilar_y_tamano():
    pila = Pila()
    pila.apilar("Escribir 'Hola'")
    pila.apilar("Escribir 'Mundo'")
    assert pila.cantidad_elementos() == 2
    assert pila.ver_cuspide() == "Escribir 'Mundo'"

def test_pila_desapilar():
    pila = Pila()
    pila.apilar("Acción 1")
    pila.apilar("Acción 2")
    assert pila.desapilar() == "Acción 2"
    assert pila.cantidad_elementos() == 1

def test_pila_vacia_excepcion():
    pila = Pila()
    assert pila.esta_vacia() is True
    with pytest.raises(IndexError):
        pila.desapilar()

def test_repository_guardar_y_deshacer():
    repo = HistorialRepository()
    repo.guardar_accion("Borrar párrafo")
    repo.guardar_accion("Aplicar Negrita")
    assert repo.total_acciones() == 2
    assert repo.deshacer_ultima_accion() == "Aplicar Negrita"
    assert repo.ver_ultima_accion() == "Borrar párrafo"


# ==========================================
# 4. APLICACIÓN PRINCIPAL (Demostración)
# ==========================================
def ejecucion_demostracion():
    historial = HistorialRepository()
    print("\n=== SISTEMA DE HISTORIAL Y DESHACER (SEMANA 7) ===")
    
    # 1. Agregar acciones
    print("\n1. Registrando acciones...")
    historial.guardar_accion("Escribir título: 'Informe'")
    historial.guardar_accion("Insertar imagen 'Figura 1'")
    historial.guardar_accion("Cambiar color a azul")
    
    print(f"-> Total de acciones almacenadas: {historial.total_acciones()}")
    print(f"-> Última acción realizada: '{historial.ver_ultima_accion()}'")
    
    # 2. Deshacer acción
    print("\n2. Ejecutando operación Deshacer (Undo)...")
    accion_deshecha = historial.deshacer_ultima_accion()
    print(f"-> Acción deshecha: '{accion_deshecha}'")
    print(f"-> Nueva última acción: '{historial.ver_ultima_accion()}'")
    print(f"-> Acciones restantes en historial: {historial.total_acciones()}")


if __name__ == "__main__":
    ejecucion_demostracion()