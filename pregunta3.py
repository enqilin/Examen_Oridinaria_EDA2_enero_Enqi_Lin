"""



"""


import csv

class Pokemon:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def clasificacion(self, PS , Ataque ,Defensa,Ataque__Especial,Defensa_Especial , Velocidad):
        self.PS = PS
        self.Ataque = Ataque
        self.Defensa = Defensa
        self.Ataque__Especial = Ataque__Especial
        self.Defensa_Especial = Defensa_Especial
        self.Velocidad = Velocidad

    def __str__(self):
        return f"{self.nombre} es de tipo {self.tipo}."

"""class pokemon:
    lista = []
    with open('pokemon.csv', newline = '\n') as fichero:
        reader = csv.reader(fichero , delimiter= ';')
        for nombre , tipo, PS,Ataque,Defensa,Ataque__Especial,Defensa_Especial,Velocidad in reader:
            pokemon = Pokemon(nombre , tipo, PS,Ataque,Defensa,Ataque__Especial,Defensa_Especial,Velocidad)
            lista.append(pokemon)
    @staticmethod

    def crear(nombre,tipo,PS,Ataque,Defensa,Ataque__Especial,Defensa_Especial,Velocidad):
        pokemon = Pokemon(nombre,tipo)
        pokemon.clasificacion(Ataque,Defensa,Ataque__Especial,Defensa_Especial,Velocidad)
        pokemon.lista.append(pokemon)
        pokemon.guardar()
        return pokemon

    def guardar():
        with open("pokemon.csv", 'w', newline='\n') as fichero:
            writer = csv.writer(fichero,delimiter = ';')
            for pokemon in pokemon.lista:
                writer.writerow(pokemon.nombre,pokemon.tipo,pokemon.PS,pokemon.Ataque,pokemon.Defensa,pokemon.Ataque__Especial,pokemon.Defensa_Especial,pokemon.Velocidad)


"""




objecto = Pokemon("charizard","fuego")
objecto.clasificacion(64,43,23,76,53,70)
print(objecto)


"""hazte ,con ,todas, las ,pokemon"""