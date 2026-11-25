import unittest
from app import run
class Estatisticas(unittest.TestCase):
    def test_por_relato(self):
        data={"relatos":{"Mateus":"Mt 5","Lucas":"Lc 6"},"detalhes":[{"item":"A","em":["Mateus","Lucas"]},{"item":"B","em":["Mateus"]}],"diagnostico":True}
        result=run(data)
        self.assertEqual(result["estatisticas"]["Lucas"]["percentual_registrado"],50.0)
        self.assertEqual(result["estatisticas"]["Mateus"]["exclusivos"],1)
        data["detalhes"]=[]
        self.assertEqual(run(data)["estatisticas"]["Lucas"]["percentual_registrado"],0.0)
