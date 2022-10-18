class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)

    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self

    def get_hijos(self):
        return self.hijos

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_datos())


def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)

    while resuelto == False and len(nodos_frontera) != 0:
        '''La búsqueda se realizará por medio de una estructura LIFO, que es una pila, y explora los nodos en profundidad, no así en anchura'''
        nodo_actual = nodos_frontera.pop()
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            '''Estructura for que hace que se creen hijos para un n numero de elementos del rompecabezas'''
            for i in range(len(estado_inicial)-1):
                hijo_datos = nodo_actual.get_datos().copy()
                temp = hijo_datos[i]
                hijo_datos[i] = hijo_datos[i + 1]
                hijo_datos[i + 1] = temp
                hijo = Nodo(hijo_datos)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)

if __name__ == "__main__":
    '''El programa solo tiene un máximo de resolución de 6 piezas en el rompecabezas considerando un tiempo prudente de espera. Con 10 piezas en
    el rompecabezas, los equipos tardan mucho en responder debido a que es una búsqueda no informada y explorará cada rama en profundidad debido
    a la estructura LIFO que se utiliza. Para que esto se solucione, se tendría que aplicar una búsqueda informada combinada con alguna heurística
    que permita desechar algunos caminos que se consideren que no será la solución'''
    estado_inicial = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nodo_solucion = bpa(estado_inicial, solucion)

    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)