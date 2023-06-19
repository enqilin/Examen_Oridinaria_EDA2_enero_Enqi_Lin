import unittest
import pregunta3 as db
import pokeball as pb
import pokemon as p

class test(unittest.TestCase):
    def setUp(self):
        db.Pokemons.lista = [db.Pokemon("Ratata","normal"),
                            db.Pokemon("Pikachu","electrico"),
                            db.Pokemon("Charizard","fuego")]
    def test_clalificacion(self):
        self.assertEqual(db.Pokemons.lista[0].clasificacion(40,45,30,35,35,56),"Ratata es de tipo normal.")
        self.assertEqual(db.Pokemons.lista[1].clasificacion(35,55,40,50,50,90),"Pikachu es de tipo electrico.")
        self.assertEqual(db.Pokemons.lista[2].clasificacion(78,84,78,109,85,100),"Charizard es de tipo fuego.")

    def test_pokeball(self):
        self.assertEqual(pb.Pokeball("pokeball",200,100,2302),"pokeball vale 200 y pesa 100 y su de fecha de fabricacion es 2302.")
        self.assertEqual(pb.Pokeball("superball",600,200,3024),"superball vale 600 y pesa 200 y su de fecha de fabricacion es 3024.")
        self.assertEqual(pb.Pokeball("ultraball",1200,300,1203),"ultraball vale 1200 y pesa 300 y su de fecha de fabricacion es 1203.")
        self.assertEqual(pb.Pokeball("masterball",0,0,2012),"masterball vale 0 y pesa 0 y su de fecha de fabricacion es 2012. ")