import unnitest
import pregunta2 as db


class test(unnitest.TestCase):
    def setUp(self):
        db.pokemon.lista = [db.Pokemon("Ratata","normal"),
                            db.Pokemon("Pikachu","electrico"),
                            db.Pokemon("Charizard","fuego")]
    
    def test_clalificacion(self):
        