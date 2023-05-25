"""
Ash Ketchum, líder del equipo de entrenadores Pokemon, tiene dificultades para transmitir los mensajes al Centro Pokemon, dado que los mismos son muy largos 
y los satélites espías del Equipo Rocket los interceptan, en un lapso muy corto desde que se transmiten. Por lo cual, nos solicita desarrollar un algoritmo que 
permita comprimir los mensajes para enviarlos más rápido y no puedan ser interceptados. Contemplando los siguientes requerimientos, 
implementar un algoritmo que pueda crear un árbol de Huffman a partir de la siguiente tabla y desarrollar las funciones para comprimir y descomprimir un mensaje.

Simbolo	Frecuencia
T	    0.15
O	    0.15
A	    0.12
E	    0.10
H	    0.09
S	    0.07
P	    0.07
M	    0.07
N	    0.06
C	    0.06
D	    0.05
Z	    0.04
K	    0.03
,	    0.03

la palabra a comprimir es: hazte,con,todos,pokemon
"""


class Nodo:
    def __init__(self,valor,frecuencia):
        self.valor = valor
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self,valor,frecuencia):
        if self.raiz == None:
            self.raiz = Nodo(valor,frecuencia)
        else:
            self.insertar_aux(self.raiz,valor,frecuencia)

    def insertar_aux(self,nodo,valor,frecuencia):
        if nodo.valor > valor:
            if nodo.izquierda == None:
                nodo.izquierda = Nodo(valor,frecuencia)
            else:
                self.insertar_aux(nodo.izquierda,valor,frecuencia)
        else:
            if nodo.derecha == None:
                nodo.derecha = Nodo(valor,frecuencia)
            else:
                self.insertar_aux(nodo.derecha,valor,frecuencia)

    def imprimir(self):
        self.imprimir_aux(self.raiz)

    def imprimir_aux(self,nodo):
        if nodo != None:
            self.imprimir_aux(nodo.izquierda)
            print(nodo.valor,nodo.frecuencia)
            self.imprimir_aux(nodo.derecha)

    def buscar(self,valor):
        return self.buscar_aux(self.raiz,valor)

    def buscar_aux(self,nodo,valor):
        if nodo == None:
            return False
        elif nodo.valor == valor:
            return True
        elif nodo.valor > valor:
            return self.buscar_aux(nodo.izquierda,valor)
        else:
            return self.buscar_aux(nodo.derecha,valor)

    def buscar_frecuencia(self,valor):
        return self.buscar_frecuencia_aux(self.raiz,valor)

    def buscar_frecuencia_aux(self,nodo,valor):
        if nodo == None:
            return False
        elif nodo.valor == valor:
            return nodo.frecuencia
        elif nodo.valor > valor:
            return self.buscar_frecuencia_aux(nodo.izquierda,valor)
        else:
            return self.buscar_frecuencia_aux(nodo.derecha,valor)
        
    def buscar_codigo(self,valor):
        return self.buscar_codigo_aux(self.raiz,valor,"")

    def buscar_codigo_aux(self,nodo,valor,codigo):
        if nodo == None:
            return ""
        elif nodo.valor == valor:
            return codigo
        elif nodo.valor > valor:
            return self.buscar_codigo_aux(nodo.izquierda,valor,codigo+"0")
        else:
            return self.buscar_codigo_aux(nodo.derecha,valor,codigo+"1")
        
    def comprimir(self,mensaje):
        codigo = ""
        for letra in mensaje:
            codigo += self.buscar_codigo(letra)
        return codigo

    def descomprimir(self,codigo):
        mensaje = ""
        nodo = self.raiz
        for bit in codigo:
            if bit == "0":
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
            if nodo.izquierda == None and nodo.derecha == None:
                mensaje += nodo.valor
                nodo = self.raiz
        return mensaje

    def __str__(self):
        return self.comprimir("hazte,con,todos,pokemon")



if __name__=="__main__":
    arbol = Arbol()
    arbol.insertar("T",0.15)
    arbol.insertar("O",0.15)
    arbol.insertar("A",0.12)
    arbol.insertar("E",0.10)
    arbol.insertar("H",0.09)
    arbol.insertar("S",0.07)
    arbol.insertar("P",0.07)
    arbol.insertar("M",0.07)
    arbol.insertar("N",0.06)
    arbol.insertar("C",0.06)
    arbol.insertar("D",0.05)
    arbol.insertar("Z",0.04)
    arbol.insertar("K",0.03)
    arbol.insertar(",",0.03)
    arbol.imprimir()
    arbol.comprimir("hazte,con,todos,pokemon")
    print(arbol)