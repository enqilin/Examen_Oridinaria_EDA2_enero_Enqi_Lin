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
        self.adyacentes = arista()


class Grafo(object):
    def __init__(self,dirigido=True):
        self.inicio = None
        self.tamanio = 0
        self.dirigido = dirigido



class arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0
    def insertar_vertice(grafo , dato):
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
        return grafo

    def agregar_arista(origen, dato, destino):
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


    def insertar_arista(grafo, dato, origen, destino):
        Arista.agregar_arista(origen.adyacentes,dato,destino.info)
        if not grafo.dirigido:
            Arista.agregar_arista(destino.adyacentes,dato,origen.info)



if __name__=="__main__":
    Arista = arista()
    Arista.insertar_vertice(1)
    Arista.insertar_vertice(2)
    Arista.insertar_vertice(3)
    Arista.insertar_vertice(4)
    Arista.insertar_vertice(5)
    Arista.insertar_vertice(6)
    Arista.insertar_vertice(7)
    Arista.insertar_vertice(8)
    Arista.insertar_vertice(9)
    Arista.insertar_vertice(0)
    Arista.insertar_arista('','',8)
    Arista.insertar_arista('',1,6)
    Arista.insertar_arista('',2,7)
    Arista.insertar_arista('',2,9)
    Arista.insertar_arista('',3,4)
    Arista.insertar_arista('',3,8)
    Arista.insertar_arista('',4,3)
    Arista.insertar_arista('',4,9)
    Arista.insertar_arista('',4,0)
    Arista.insertar_arista('',6,1)
    Arista.insertar_arista('',6,7)
    Arista.insertar_arista('',6,0)
    Arista.insertar_arista('',7,2)
    Arista.insertar_arista('',7,6)
    Arista.insertar_arista('',8,1)
    Arista.insertar_arista('',8,3)
    Arista.insertar_arista('',9,2)
    Arista.insertar_arista('',9,4)
    Arista.insertar_arista('',0,4)
    Arista.insertar_arista('',0,6)