import unnitest
import pregunta2 as db


class test(unnitest.TestCase):
    def setUp(self):
        db.pokemon.lista = [db.Pokemon("Ratata","normal"),