"""
Crea una clase llamada Pokeball.py que tenga los atributos peso, nombre, precio y fecha de fabricación.
 Crea el constructor de la clase. Añade en el constructor un print para informar de que la Pokeball se ha creado con éxito.

Crea el método str para visualizar por pantalla la información de las Pokeballs.

3.2 Experimentación (0,5 Puntos)
Crea algunas Pokeballs. Prueba a mostrar los datos de algunas Pokeballs ordenadas por su fecha de fabricación y a modificar algún valor, 
por ejemplo, prueba a modificar el precio de una de las Pokeballs.


"""


import csv

class Pokemon:
    def __ini__T(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo

    def clasificacion(self, PS , Ataque ,Defensa,Ataque__Especial,Defensa_Especial , Velocidad):
        super().__ini__(self,nombre,tipo):
        self.PS = PS
        self.Ataque = Ataque
        self.Defensa = Defensa
        self.Ataque__Especial = Ataque__Especial
        self.Defensa_Especial = Defensa_Especial
        self.Velocidad = Velocidad

    def __srt__(self):
        return f."{self.nombre} es de tipo {self.tipo}. "

class pokemon:
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




if __name__=="__main__":
    