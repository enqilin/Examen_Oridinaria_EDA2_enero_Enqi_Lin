"""
Crea una clase llamada Pokemon.py que tenga los atributos nombre y tipo. Crea el constructor de la clase. Añadir en el constructor un print para informar de que el Pokemon se ha creado con éxito. 
Crear un método llamado clasificacion que clasifique a los Pokemon según su tipo de la siguiente manera:

los PS, el Ataque, la Defensa, el Ataque Especial, la Defensa Especial y la Velocidad.

1.2 Experimentación (0,5 Puntos)

Crea una lista con un numero arbitrario de objetos tipo Pokemon. Recorre los elementos de la lista, y prueba a ejecutar el método clasificacion de cada objeto que has creado.
"""
import csv

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
    def to_dict(self):
        return {
            "nombre":self.nombre,
            "tipo":self.tipo,
            "PS":self.PS,
            "Ataque":self.Ataque,
            "Defensa":self.Defensa,
            "Ataque Especial":self.Ataque__Especial,
            "Defensa Especial":self.Defensa_Especial,
            "Velocidad":self.Velocidad
        }
class Pokemons:
    lista = []

    with open("pokemon.csv", "r") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for nombre, tipo, PS, Ataque, Defensa, Ataque__Especial, Defensa_Especial, Velocidad in reader:
            pokemon = Pokemon(nombre, tipo)
            pokemon.clasificacion(PS, Ataque, Defensa, Ataque__Especial, Defensa_Especial, Velocidad)
            lista.append(pokemon)


    @staticmethod
    def buscar(nombre):
        for pokemon in Pokemons.lista:
            if pokemon.nombre == nombre:
                return pokemon
    @staticmethod
    def crear(nombre,tipo,PS,Ataque,Defensa,Ataque__Especial,Defensa_Especial,Velocidad):
        pokemon = Pokemon(nombre, tipo)
        pokemon.clasificacion(PS, Ataque, Defensa, Ataque__Especial, Defensa_Especial, Velocidad)
        Pokemons.lista.append(pokemon)
        Pokemons.guadar()
        return pokemon
    @staticmethod
    def guadar():
        with open("pokemon.csv", 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for pokemon in Pokemons.lista:
                writer.writerow(pokemon.to_dict().values())


if __name__=='__main__':
    objecto = Pokemon("charizar","fuego")
    objecto.clasificacion(64,43,23,76,53,70)
    (objecto)