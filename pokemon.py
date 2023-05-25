"""
Crea una clase llamada Pokemon.py que tenga los atributos nombre y tipo. Crea el constructor de la clase. Añadir en el constructor un print para informar de que el Pokemon se ha creado con éxito. 
Crear un método llamado clasificacion que clasifique a los Pokemon según su tipo de la siguiente manera:

los PS, el Ataque, la Defensa, el Ataque Especial, la Defensa Especial y la Velocidad.

1.2 Experimentación (0,5 Puntos)

Crea una lista con un numero arbitrario de objetos tipo Pokemon. Recorre los elementos de la lista, y prueba a ejecutar el método clasificacion de cada objeto que has creado.
"""


class Pokemon:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
        print("Se ha creado el pokemon con exito")

    def clasificacion(self, PS , Ataque ,Defensa,Ataque__Especial,Defensa_Especial , Velocidad):
        self.PS = PS
        self.Ataque = Ataque
        self.Defensa = Defensa
        self.Ataque__Especial = Ataque__Especial
        self.Defensa_Especial = Defensa_Especial
        self.Velocidad = Velocidad


if __name__=='__main__':
    objecto = Pokemon("charizar","fuego")
    objecto.clasificacion(64,43,23,76,53,70)
    print(objecto)