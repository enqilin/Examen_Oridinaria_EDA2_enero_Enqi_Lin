"""



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
            "Velocidad":self.Velocidad}
    def __str__(self):
        return f"{self.nombre} es de tipo {self.tipo}."

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
    objecto = Pokemon("charizard","fuego")
    objecto.clasificacion(64,43,23,76,53,70)
    print(objecto)