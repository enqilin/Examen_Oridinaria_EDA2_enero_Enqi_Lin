

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




class Arista(object):
    de