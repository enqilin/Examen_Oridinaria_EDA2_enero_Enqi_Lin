import unnitest
import pregunta3 as db
import pokeball as pb


class test(unnitest.TestCase):
    def setUp(self):
        db.pokemon.lista = [db.Pokemon("Ratata","normal"),
                            db.Pokemon("Pikachu","electrico"),
                            db.Pokemon("Charizard","fuego")]
    
    
    def test_clalificacion(self):
        self.assertEqual(db.pokemon.lista[0].clasificacion(40,45,30,35,35,56),"Ratata es de tipo normal.")
        self.assertEqual(db.pokemon.lista[1].clasificacion(35,55,40,50,50,90),"Pikachu es de tipo electrico.")
        self.assertEqual(db.pokemon.lista[2].clasificacion(78,84,78,109,85,100),"Charizard es de tipo fuego.")

    def test_pokeball(self):
        self.assertEqual(pb.pokeball.crear("pokeball",200,100),"pokeball")
        self.assertEqual(pb.pokeball.crear("superball",600,200),"superball")
        self.assertEqual(pb.pokeball.crear("ultraball",1200,300),"ultraball")
        self.assertEqual(pb.pokeball.crear("masterball",0,0),"masterball")