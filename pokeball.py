"""
Crea una clase llamada Pokeball.py que tenga los atributos peso, nombre, precio y fecha de fabricación. Crea el constructor de la clase.
 Añade en el constructor un print para informar de que la Pokeball se ha creado con éxito.

Crea el método str para visualizar por pantalla la información de las Pokeballs.

Crea algunas Pokeballs. Prueba a mostrar los datos de algunas Pokeballs ordenadas por su fecha de fabricación y a modificar algún valor,
 por ejemplo, prueba a modificar el precio de una de las Pokeballs.


"""
import datetime


class Pokeball:
    def __init__(self,peso,nombre,precio, datetime):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha = datetime
        print("Se ha creado la pokeball con exito")

    def __str__(self):
        return f"El {self.nombre} vale {self.precio} pesa {self.peso} y su de fecha de fabricacion es {self.fecha}."



if __name__=="__main__":
    pokeball = Pokeball(12,'superball', 1000, 2193)
    print(pokeball)
    