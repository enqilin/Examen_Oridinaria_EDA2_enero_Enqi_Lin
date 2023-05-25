"""
problema de los movimientos de caballo en ajedrez
1 ir al 6,8
2 ir al 7,9
3 ir al 4,8
4 ir al 3,9,0
5 ninguno
6 ir al 1,7,0
7 ir al 2,6
8 ir al 1,3
9 ir al 2,4
0 ir al 4,6
"""

class nodoArista(object):
    def __init__(self,info,destino):
        self.info = info
        self.destino = destino
        self.sig = None

class nodoVertice(object):
    def __init__(self,info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo(object):
    def __init__(self,dirigido=True):
        self.inicio = None
        self.tamanio = 0
        self.dirigido = dirigido

    def insertar_vertice(grafo , dato):
        nodo = nodoVertice()
        if grafo.inicio is None or dato < grafo.inicio.info:
            nodo.sig = grafo.inicio
            grafo.inicio = nodo
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while act is not None and act.info < nodo.info:
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        grafo.tamanio += 1 

    def insertar_arista(grafo, dato,origen,destino):
        Grafo.agregar_arista(origen.ayacentes,dato,destino.info)
        if not grafo.dirigido:
            Grafo.agregar_arista(destino.adyacentes,dato,origen.info)

    def agregar_arista(origen,dato,destino):
        nodo = nodoArista()
        if origen.inicio is None or origen.inicio.destino > destino:
            nodo.sig = origen.inicio
            origen.inicio = nodo
        else:
            act = origen.inicio
            ant = origen.inicio.sig
            while act.sig is not None and act.destino > nodo.destino:
                ant
                act = act.sig
            nodo.sig = act
            act.sig = nodo
        origen.tamanio += 1

class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


if __name__=="__main__":
