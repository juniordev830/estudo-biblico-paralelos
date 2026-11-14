import unittest
from app import run

class RelationNamesTest(unittest.TestCase):
    def test_trimmed_name_collision_is_rejected(self):
        data={'relatos':{'mateus':'Mateus 14',' mateus ':'Mateus 15','marcos':'Marcos 6'}, 'detalhes':[]}
        with self.assertRaises(ValueError):
            run(data)

    def test_unique_names_can_be_trimmed(self):
        data={'relatos':{' mateus ':'Mateus 14','marcos':'Marcos 6'}, 'detalhes':[{'item':'Detalhe','em':['mateus','marcos']}]}
        self.assertEqual(run(data)['comuns'], ['Detalhe'])
