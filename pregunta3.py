"""
Crea una clase llamada Pokeball.py que tenga los atributos peso, nombre, precio y fecha de fabricación.
 Crea el constructor de la clase. Añade en el constructor un print para informar de que la Pokeball se ha creado con éxito.

Crea el método str para visualizar por pantalla la información de las Pokeballs.

3.2 Experimentación (0,5 Puntos)
Crea algunas Pokeballs. Prueba a mostrar los datos de algunas Pokeballs ordenadas por su fecha de fabricación y a modificar algún valor, 
por ejemplo, prueba a modificar el precio de una de las Pokeballs.


"""



class Pokemon:
    lista = []
    def __init__(self,nombre,tipo):
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

    def __str__(self):
        return f."{self.nombre} es de tipo {self.tipo} ."

