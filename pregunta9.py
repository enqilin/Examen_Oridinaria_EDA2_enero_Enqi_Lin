

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
    def insertar_vertice(grafo,dato):
        nodo = nodoVertice(dato)
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

    def insertar_arista(grafo,dato,origen, destino):
        Grafo.agregar_arista(origen.adyacentes,dato,destino.info)
        if not grafo.dirigido:
            Grafo.agregar_arista(destino.adyacentes,dato,origen.info)
        

    def agregar_arista(origen,dato,destino):
        nodo = nodoArista(dato,destino)
        if origen.inicio is None or origen.inicio.destino > destino:

            nodo.sig = origen.inicio
            origen.inicio = nodo
        else:
            ant = origen.inicio
            act = origen.inicio.sig
            while act is not None and act.destino > nodo.destino:
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        origen.tamanio += 1




class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0